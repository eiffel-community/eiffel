# Copyright 2025 Axis Communications AB.
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

import semver

import bump_definitions


def _strip_leading_indent(s):
    return re.sub(r"^\s+", "", s, flags=re.M)


def test_transform_definition_replaces_version():
    assert (
        bump_definitions._transform_definition(
            _strip_leading_indent(
                """
                # Copyright blah
                _version: 1.0.0
                """
            ),
            semver.VersionInfo.parse("2.0.0"),
        )
        == _strip_leading_indent(
            """
            # Copyright blah
            _version: 2.0.0
            """
        )
    )


def test_transform_definition_updates_range():
    assert (
        bump_definitions._transform_definition(
            _strip_leading_indent(
                """
                # Copyright 2020-2021 Company Name, Inc.
                """
            ),
            semver.VersionInfo.parse("2.0.0"),
            copyright_year=2025,
        )
        == _strip_leading_indent(
            """
            # Copyright 2020-2025 Company Name, Inc.
            """
        )
    )


def test_transform_definition_turn_year_into_range():
    assert (
        bump_definitions._transform_definition(
            _strip_leading_indent(
                """
                # Copyright 2020 Company Name, Inc.
                """
            ),
            semver.VersionInfo.parse("2.0.0"),
            copyright_year=2025,
        )
        == _strip_leading_indent(
            """
            # Copyright 2020-2025 Company Name, Inc.
            """
        )
    )
