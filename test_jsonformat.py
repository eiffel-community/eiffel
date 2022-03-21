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

import pytest


@pytest.mark.parametrize(
    "filename",
    subprocess.check_output(["git", "ls-files", "--exclude-standard", "*.json"])
    .decode("utf-8")
    .splitlines(),
)
def test_json_file_has_canonical_format(filename):
    with open(filename) as input_file:
        data = input_file.read()
    reformatted = json.dumps(json.loads(data), indent=2) + "\n"

    assert reformatted == data
