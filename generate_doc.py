#!/usr/bin/env python3
"""Reads an event definition file and transforms it into a
documentation Markdown file.

Example:

    ./generate_doc.py definitions/EiffelCompositionDefinedEvent/3.2.0.yml
"""

import dataclasses
import sys
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Set

import jinja2

import definition_loader

_OUTPUT_ROOT_PATH = Path("eiffel-vocabulary")

# Optional list of field names that should be omitted from the documentation.
_SKIP_DOC_FIELDS = {"data.customData"}


@dataclasses.dataclass
class Member:
    description: str
    format: str
    legal_values: List[Any]
    name: str
    typ: str
    required: bool


def _filter_event_link(input: str) -> str:
    """Jinja2 filter that transforms an event type name to a links to
    the documentation of that event.
    """
    if input.startswith("Eiffel") and input.endswith("Event"):
        return f"[{input}](../eiffel-vocabulary/{input}.md)"
    return input


def _filter_member_heading(input: str) -> str:
    """Jinja2 filter that transforms an event member name to a section
    heading with an appropriate depth.
    """
    return (2 + input.count(".")) * "#" + " " + input


def _filter_yes_or_no(input: bool) -> str:
    """Jinja2 filter that tranforms a boolean value into either "Yes" or "No"."""
    return "Yes" if input else "No"


def _get_field_enum_values(field: Dict) -> Optional[List[Any]]:
    """Returns a list of valid enum values if the given property is an
    enum, otherwise None.
    """
    try:
        return field["enum"]
    except KeyError:
        try:
            return field["items"]["enum"]
        except KeyError:
            return None


def _get_field_type(field: Dict) -> str:
    """Returns the type of a field given its property definition. Scalar
    types are simply titlecased and array properties are expressed as
    "InnerType[]" where InnerType is the type of each item.
    """
    if "type" not in field:
        return "Any"
    if field["type"] == "array":
        return field["items"].get("type", "object").title() + "[]"
    return field["type"].title()


def _get_members(
    field_prefix: str, definitions: Dict, skip: Set[str]
) -> Dict[str, Member]:
    """Returns a dict of Member objects, keyed by the full field name
    (e.g. data.name or meta.source.name). Fields whose full name is
    included in the skip set will be omitted from the result.
    """
    result = {}
    required = definitions.get("required", [])
    for prop, prop_def in definitions.get("properties", {}).items():
        if "$ref" in prop_def:
            continue
        full_name = field_prefix + prop
        if full_name in skip:
            continue
        result[full_name] = Member(
            description=prop_def.get("_description", ""),
            format=prop_def.get("_format"),
            legal_values=_get_field_enum_values(prop_def),
            name=full_name,
            typ=_get_field_type(prop_def),
            required=prop in required,
        )
        if prop_def.get("type") == "object":
            result.update(_get_members(field_prefix + prop + ".", prop_def, skip))
        elif prop_def.get("type") == "array":
            result.update(
                _get_members(field_prefix + prop + ".", prop_def["items"], skip)
            )
    return result


def _main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    env.filters["event_link"] = _filter_event_link
    env.filters["member_heading"] = _filter_member_heading
    env.filters["yes_or_no"] = _filter_yes_or_no
    templ = env.get_template("event_docs.md.j2")

    for filename in sys.argv[1:]:
        print(filename)
        input_path = Path(filename)
        schema = definition_loader.load(input_path)
        context = {
            "type": input_path.parent.name,
            "version": input_path.stem,
            "description": schema.get("_description", ""),
            "abbrev": schema.get("_abbrev", ""),
            "links": schema.get("_links", {}),
            "data_members": _get_members(
                "data.", schema["properties"]["data"], _SKIP_DOC_FIELDS
            ),
            "meta_members": _get_members(
                "meta.", schema["properties"]["meta"], _SKIP_DOC_FIELDS
            ),
            "examples": schema.get("_examples"),
            "history": schema.get("_history"),
        }
        output_path = (_OUTPUT_ROOT_PATH / input_path.parent.name).with_suffix(".md")
        with output_path.open(mode="w") as output_file:
            output_file.write(templ.render(**context))


if __name__ == "__main__":
    _main()
