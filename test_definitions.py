# Copyright 2023-2024 Axis Communications AB and others.
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

from pathlib import Path

import pytest

import definition_loader
import generate_manifest


class DefinitionFile:
    """Helper class that loads a type definition and tracks its source
    path and desired testcase id.
    """

    def __init__(self, path: Path):
        self.path = path
        self.definition = definition_loader.load(path)
        self.id = f"{self.definition['_name']}/{self.definition['_version']}"


# Preloaded type definitions for reuse in each parametrized testcase.
DEFINITION_FILES = [p for p in Path(".").glob("definitions/*/*.yml")]
EVENT_DEFINITIONS = [
    DefinitionFile(p) for p in DEFINITION_FILES if p.parent.name.endswith("Event")
]
EVENT_DEFINITION_IDS = [d.id for d in EVENT_DEFINITIONS]
EVENT_DEFINITIONS_W_LINKS_REQUIRED = [
    d for d in EVENT_DEFINITIONS if "2020-12" in d.definition.get("$schema")
]
EVENT_DEFINITION_W_LINKS_REQUIRED_IDS = [
    d.id for d in EVENT_DEFINITIONS_W_LINKS_REQUIRED
]
OTHER_DEFINITIONS = [
    DefinitionFile(p) for p in DEFINITION_FILES if not p.parent.name.endswith("Event")
]
OTHER_DEFINITION_IDS = [d.id for d in OTHER_DEFINITIONS]


@pytest.fixture(scope="session")
def manifest():
    return generate_manifest.Manifest("event_manifest.yml")


@pytest.mark.parametrize(
    "definition_file",
    EVENT_DEFINITIONS,
    ids=EVENT_DEFINITION_IDS,
)
def test_history_table_contains_current_version(definition_file):
    event_version = definition_file.path.stem
    assert [
        entry
        for entry in definition_file.definition.get("_history", [])
        if entry.get("version") == event_version
    ], "History table entry missing"


@pytest.mark.parametrize(
    "definition_file",
    EVENT_DEFINITIONS,
    ids=EVENT_DEFINITION_IDS,
)
def test_history_table_contains_valid_release(definition_file, manifest):
    for entry in definition_file.definition.get("_history", []):
        edition = entry.get("introduced_in", None)
        if edition is not None:
            assert manifest.is_edition_tag(
                edition
            ), f"Nonexistent edition '{edition}' in history table"


@pytest.mark.parametrize(
    "definition_file",
    EVENT_DEFINITIONS,
    ids=EVENT_DEFINITION_IDS,
)
def test_history_table_matches_manifest(definition_file, manifest):
    event_type = definition_file.definition["_name"]
    for entry in definition_file.definition.get("_history", []):
        edition = entry.get("introduced_in", None)
        event_version_of_edition = entry.get("version")
        if edition is not None:
            assert manifest.is_in_edition(
                edition, event_type, event_version_of_edition
            ), f"{event_version_of_edition} not part of '{edition}' as described in history table"


@pytest.mark.parametrize(
    "definition_file",
    EVENT_DEFINITIONS + OTHER_DEFINITIONS,
    ids=EVENT_DEFINITION_IDS + OTHER_DEFINITION_IDS,
)
def test_filename_matches_type_version_fields(definition_file):
    # Compute the expected type name and version based on the filename.
    type = definition_file.path.parent.name
    version = definition_file.path.stem

    # Do they match what's in the definition?
    assert type == definition_file.definition["_name"]
    assert version == definition_file.definition["_version"]


@pytest.mark.parametrize(
    "definition_file",
    EVENT_DEFINITIONS_W_LINKS_REQUIRED,
    ids=EVENT_DEFINITION_W_LINKS_REQUIRED_IDS,
)
def test_links(definition_file, manifest):
    linktypes_in_schema = set(
        definition_file.definition.get("properties", {})
        .get("links", {})
        .get("contains", {})
        .get("properties", {})
        .get("type", {})
        .get("enum", [])
    )
    linktypes_in_definition = {
        link_type
        for link_type, link_def in definition_file.definition.get("_links", {}).items()
        if link_def.get("required", False)
    }
    assert (
        linktypes_in_schema == linktypes_in_definition
    ), f"Link types required by schema ({linktypes_in_schema}) don't match link types required by definition file ({linktypes_in_definition})"
