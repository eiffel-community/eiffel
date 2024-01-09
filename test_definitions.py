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
        self.id = str(Path(path.parent.name) / path.stem)


# Preloaded type definitions for reuse in each parametrized testcase.
EVENT_DEFINITIONS = [
    DefinitionFile(p) for p in Path(".").glob("definitions/Eiffel*Event/*.yml")
]
EVENT_DEFINITION_IDS = [d.id for d in EVENT_DEFINITIONS]


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
    event_type = definition_file.path.parent.name
    for entry in definition_file.definition.get("_history", []):
        edition = entry.get("introduced_in", None)
        event_version_of_edition = entry.get("version")
        if edition is not None:
            assert manifest.is_in_edition(
                edition, event_type, event_version_of_edition
            ), f"{event_version_of_edition} not part of '{edition}' as described in history table"
