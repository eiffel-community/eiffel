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

import json
import subprocess

import jsonschema
import pytest


@pytest.mark.parametrize(
    "filename",
    subprocess.check_output(["git", "ls-files", "--exclude-standard", "schemas/*.json"])
    .decode("utf-8")
    .splitlines(),
)
def test_json_schema(filename):
    with open(filename) as input_file:
        data = input_file.read()

    event_schema = json.loads(data)
    stricter_metaschema = dict(
        jsonschema.Draft4Validator.META_SCHEMA, additionalProperties=False
    )
    StrictDraft4Validator = jsonschema.validators.create(
        stricter_metaschema, jsonschema.Draft4Validator.VALIDATORS, "StrictDraft4"
    )
    StrictDraft4Validator.check_schema(event_schema)
