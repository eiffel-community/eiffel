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

# Mapping of friendly edition names to their Git tags.
_EDITIONS = {
    "Agen": "edition-agen",
    "Agen-1": "edition-agen-1",
    "Arica": "edition-arica",
    "Bordeaux": "edition-bordeaux",
    "Lyon": "edition-lyon",
    "Paris": "edition-paris",
    "Toulouse": "edition-toulouse",
}


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
    manifest = []
    for name in sorted(_EDITIONS):
        entry = {
            "name": name,
            "tag": _EDITIONS[name],
            "events": _get_latest_schemas(_EDITIONS[name]),
        }
        manifest.append(entry)

    sys.stdout.write("---\n")
    yaml_writer = yaml.YAML()
    yaml_writer.indent(mapping=2, sequence=4, offset=2)
    yaml_writer.dump(manifest, sys.stdout)


if __name__ == "__main__":
    _main()
