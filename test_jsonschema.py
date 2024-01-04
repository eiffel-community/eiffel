# Copyright 2022-2023 Axis Communications AB and others.
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
import logging

import jsonschema
import pytest

# Set up a console logger
logger = logging.getLogger("__Logger__")
console_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S%p",
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


@pytest.mark.parametrize(
    "filename",
    subprocess.check_output(["git", "ls-files", "--exclude-standard", "schemas/*.json"])
    .decode("utf-8")
    .splitlines(),
)
def test_json_schema(filename):
    with open(filename) as input_file:
        event_schema = json.loads(input_file.read())

    # Use standard validator for old ActC schemas, to cope with bug https://github.com/eiffel-community/eiffel/issues/376
    if ("ActivityCanceled" in filename) and (event_schema["properties"]["meta"]["properties"]["version"]["default"] in ["1.0.0", "1.1.0", "2.0.0", "3.0.0", "3.1.0", "3.2.0"]):
            jsonschema.Draft4Validator.check_schema(event_schema)
    else:
        stricter_metaschema = dict(
            jsonschema.Draft4Validator.META_SCHEMA, additionalProperties=False
        )
        StrictDraft4Validator = jsonschema.validators.create(
            stricter_metaschema, jsonschema.Draft4Validator.VALIDATORS, "StrictDraft4"
        )
        StrictDraft4Validator.check_schema(event_schema)
