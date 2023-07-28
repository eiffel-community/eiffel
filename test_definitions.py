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

import pathlib
import pytest
import definition_loader
import generate_manifest


@pytest.fixture(scope='session')
def manifest():
    return generate_manifest.Manifest("event_manifest.yml")


@pytest.mark.parametrize(
    "event_definition_path",
    pathlib.Path(".").glob("definitions/Eiffel*Event/*.yml"),
)
def test_history_table_contains_current_version(event_definition_path):
    definition = definition_loader.load(event_definition_path)
    event_type = event_definition_path.parent.name
    event_version = event_definition_path.stem
    assert [
        entry
        for entry in definition.get("_history", [])
        if entry.get("version") == event_version
    ], f"History table entry missing for {event_type} {event_version}"


@pytest.mark.parametrize(
    "event_definition_path",
    pathlib.Path(".").glob("definitions/Eiffel*Event/*.yml"),
)
def test_history_table_contains_valid_release(event_definition_path, manifest):
    event_type = event_definition_path.parent.name
    event_version = event_definition_path.stem
    definition = definition_loader.load(event_definition_path)
    for entry in definition.get("_history", []):
        edition = entry.get("introduced_in", None)
        if edition is not None:
            assert manifest.is_edition_tag(edition), \
                f"Nonexistent edition '{edition}' in history table for {event_type} {event_version}"


@pytest.mark.parametrize(
    "event_definition_path",
    pathlib.Path(".").glob("definitions/Eiffel*Event/*.yml"),
)
def test_history_table_matches_manifest(event_definition_path, manifest):
    event_type = event_definition_path.parent.name
    event_version = event_definition_path.stem
    definition = definition_loader.load(event_definition_path)
    for entry in definition.get("_history", []):
        edition = entry.get("introduced_in", None)
        event_version_of_edition = entry.get("version")
        if edition is not None:
            assert manifest.is_in_edition(edition, event_type, event_version_of_edition), \
                f"{event_version_of_edition} not part of '{edition}' as describe in history table for {event_type} {event_version}"
