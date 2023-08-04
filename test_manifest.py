# Copyright 2023 Ericsson AB.
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


import pytest

from generate_manifest import Manifest


@pytest.fixture(scope="session")
def manifest():
    return Manifest("event_manifest.yml")


def test_get_edition_tags(manifest):
    assert manifest.tags == [
        "edition-bordeaux",
        "edition-toulouse",
        "edition-agen",
        "edition-agen-1",
        "edition-paris",
        "edition-lyon",
        "edition-arica",
        "edition-orizaba",
    ]


def test_edition_tag(manifest):
    assert manifest.is_edition_tag("edition-bordeaux") is True


def test_not_edition_tag(manifest):
    assert manifest.is_edition_tag("edition-foo") is False


def test_event_version(manifest):
    assert (
        manifest.event_version_by_tag("edition-agen", "EiffelActivityTriggeredEvent")
        == "3.0.0"
    )


def test_get_previous_edition(manifest):
    assert (
        manifest.get_previous_edition_by_tag("edition-agen")["tag"]
        == "edition-toulouse"
    )


def test_get_previous_edition_of_first_edition(manifest):
    assert manifest.get_previous_edition_by_tag("edition-bordeaux") is None


def test_is_event_version_part_of_edition(manifest):
    assert (
        manifest.is_in_edition("edition-agen", "EiffelActivityTriggeredEvent", "2.0.0")
        is True
    )
    assert (
        manifest.is_in_edition("edition-agen", "EiffelActivityTriggeredEvent", "3.0.0")
        is True
    )
    assert (
        manifest.is_in_edition("edition-agen", "EiffelActivityTriggeredEvent", "4.0.0")
        is False
    )


def test_is_new_event_version_part_of_edition(manifest):
    assert (
        manifest.is_in_edition("edition-agen", "EiffelIssueDefinedEvent", "3.0.0")
        is True
    )


def test_is_event_version_part_of_first_edition(manifest):
    assert (
        manifest.is_in_edition(
            "edition-bordeaux", "EiffelActivityTriggeredEvent", "2.0.0"
        )
        is False
    )


def test_is_event_version_part_of_nonexistent_edition(manifest):
    with pytest.raises(ValueError, match=r".*not found amongst.*"):
        manifest.is_in_edition("edition-foo", "EiffelActivityTriggeredEvent", "2.0.0")
