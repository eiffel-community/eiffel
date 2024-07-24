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

"""The definition_loader module loads the YAML definition of an event
from a file and resolves any JSON references."""

from pathlib import Path
from typing import Dict
from urllib.parse import urlparse
from urllib.request import url2pathname

import jsonref
from ruamel import yaml


def load(input_path: Path) -> Dict:
    """Loads a schema definition file and returns it as a dictionary with
    all references resolved.
    """
    with input_path.open() as input_file:
        return jsonref.replace_refs(
            yaml.YAML().load(input_file),
            base_uri=input_path.resolve().as_uri(),
            loader=_yaml_loader,
        )


def _yaml_loader(uri: str) -> Dict:
    parsed_uri = urlparse(uri)
    input_path = Path(url2pathname(parsed_uri.path))
    with input_path.open() as input_file:
        # Maybe JsonRef fixes recursion on its own?
        schema = jsonref.replace_refs(
            yaml.YAML().load(input_file),
            base_uri=input_path.resolve().as_uri(),
            loader=_yaml_loader,
        )
        del schema["$schema"]
        return schema
