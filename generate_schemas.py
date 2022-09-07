#!/usr/bin/env python3
"""Reads an event definition file and transforms it into a flat
schema file with all JSON references resolved and inlined.

Example:

    ./generate_schema.py definitions/EiffelCompositionDefinedEvent/3.2.0.yml
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
