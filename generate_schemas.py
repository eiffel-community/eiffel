#!/usr/bin/env python3

# Copyright 2022 Axis Communications AB.
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

"""Reads an event definition file and transforms it into a flat
schema file with all JSON references resolved and inlined.

Example:

    ./generate_schemas.py definitions/EiffelCompositionDefinedEvent/3.2.0.yml
"""

import json
import sys
from pathlib import Path
from typing import Dict

import definition_loader

_OUTPUT_ROOT_PATH = Path("schemas")


def _strip_extra_keys(data: Dict) -> None:
    """Recursively remove all dict keys that begin with an underscore."""
    for key in list(data.keys()):
        if key.startswith("_"):
            del data[key]
            continue
        if isinstance(data[key], dict):
            _strip_extra_keys(data[key])


def _main():
    for filename in sys.argv[1:]:
        print(filename)
        input_path = Path(filename)
        event_def = definition_loader.load(input_path)

        # At this point the event has been flattened to contain
        # the generic meta definition from one of the files in
        # definitions/EiffelMetaProperty. Patch the definitions of
        # meta.type and meta.version based on the event type and version.
        meta_type = input_path.parent.name
        meta_version = input_path.stem
        meta_properties = event_def["properties"]["meta"]["properties"]
        meta_properties["type"]["enum"] = [meta_type]
        meta_properties["version"]["enum"] = [meta_version]
        meta_properties["version"]["default"] = meta_version

        _strip_extra_keys(event_def)

        output_path = (
            _OUTPUT_ROOT_PATH / input_path.parent.name / input_path.name
        ).with_suffix(".json")
        with output_path.open(mode="w") as output_file:
            json.dump(event_def, output_file, indent=2)
            output_file.write("\n")


if __name__ == "__main__":
    _main()
