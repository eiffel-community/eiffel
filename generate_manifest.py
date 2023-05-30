#!/usr/bin/env python3

# Copyright 2023 Axis Communications AB.
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
    ("Paris", "edition-paris", "2021-02-16"),
    ("Toulouse", "edition-toulouse", "2018-02-20"),
]


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
