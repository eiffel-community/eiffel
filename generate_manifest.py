#!/usr/bin/env python3

# Copyright 2023 Axis Communications AB and others.
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import subprocess
import sys
from functools import cached_property
from typing import Dict

import semver
from ruamel import yaml

# List of tuples with the edition display names, their Git tags, and
# their release dates.
_EDITIONS = [
    ("Agen", "edition-agen", "2018-09-19"),
    ("Agen-1", "edition-agen-1", "2019-04-29"),
    ("Arica", "edition-arica", "2022-11-18"),
    ("Bordeaux", "edition-bordeaux", "2017-04-12"),
    ("Lyon", "edition-lyon", "2021-10-12"),
    ("Orizaba", "edition-orizaba", "2023-06-30"),
    ("Paris", "edition-paris", "2021-02-16"),
    ("Toulouse", "edition-toulouse", "2018-02-20"),
]


class Manifest:
    """
    Python interface as a class for reading the event_manifest.yaml file.
    """

    def __init__(self, manifest_path: str):
        with open(manifest_path) as file:
            _raw_event_manifest = yaml.YAML().load(file)

        # The manifest file is already sorted, but do we want to count on it?
        self._event_manifest = sorted(
            _raw_event_manifest,
            key=lambda _edition: _edition["release_date"])
        self._edition_tag_map = dict()
        for edition in self._event_manifest:
            self._edition_tag_map[edition['tag']] = edition

    def is_edition_tag(self, question_tag: str) -> bool:
        """
        Test if the provided tags matches any of the edition tags
        """
        return question_tag in self.tags

    @cached_property
    def tags(self):
        """
        Fetches all the tags
        """
        return [edition['tag'] for edition in self._event_manifest]

    def event_version_by_tag(self, edition: str, event: str):
        """
        Fetches the event version of the given event in the given edition
        :return: None if event not part of edition
        """
        return self._edition_tag_map[edition]['events'].get(event, None)

    def get_previous_edition_by_tag(self, edition_tag: str):
        """
        Fetches the previous edition
        :return: None if first edition
        """
        if edition_tag not in self.tags:
            raise ValueError(f"{edition_tag} not found amongst {self.tags}")

        current_edition_index = self.tags.index(edition_tag)
        if current_edition_index == 0:
            return None
        else:
            return self._event_manifest[current_edition_index - 1]

    def is_in_edition(self, edition_tag: str, event_name: str, event_version: str):
        """
        Tests if the given edition contains the given version of the event.
        Tests by comparing the range given by the current edition and the previous.
        """
        previous_edition = self.get_previous_edition_by_tag(edition_tag)
        version_of_current_edition = self.event_version_by_tag(edition_tag, event_name)
        if previous_edition is None:
            return semver.VersionInfo.parse(version_of_current_edition).compare(event_version) == 0
        else:
            version_of_previous_edition = self.event_version_by_tag(previous_edition['tag'], event_name)
            if version_of_previous_edition is None:
                version_of_previous_edition = "0.0.0"
            does_not_exceed_current_version = \
                semver.VersionInfo.parse(version_of_current_edition).compare(event_version) > -1
            does_not_subceed_previous_version = \
                semver.VersionInfo.parse(event_version).compare(version_of_previous_edition) > -1
            return does_not_exceed_current_version and does_not_subceed_previous_version


def _get_latest_schemas(tag: str) -> Dict[str, str]:
    """Given a tag, returns a mapping of the event types available in that
    tag and the latest version of each such type.
    """
    schema_file_regexp = re.compile(r"^schemas/([^/]+)/([^/]+).json$")
    latest = {}
    for schema_file in subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", tag, "--", "schemas"]
    ).splitlines():
        match = schema_file_regexp.search(schema_file.decode("utf-8"))
        if not match:
            continue
        event_type = match.group(1)
        event_version = semver.VersionInfo.parse(match.group(2))
        if event_type not in latest or latest[event_type].compare(event_version) < 0:
            latest[event_type] = event_version
    return {
        event_type: str(event_version) for event_type, event_version in latest.items()
    }


def _main():
    manifest = [
        {
            "name": name,
            "tag": tag,
            "release_date": date,
            "events": _get_latest_schemas(tag),
        }
        for name, tag, date in sorted(_EDITIONS, key=lambda edition: edition[2])
    ]

    sys.stdout.write("---\n")
    yaml_writer = yaml.YAML()
    yaml_writer.indent(mapping=2, sequence=4, offset=2)
    yaml_writer.dump(manifest, sys.stdout)


if __name__ == "__main__":
    _main()
