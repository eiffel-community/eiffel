# Copyright 2016-2024 Ericsson AB and others.
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

import sys
from pathlib import Path
from shutil import copyfile

import versions

"""
Finds the latest versions of schemas found under <input_folder>, with
the following expectations:
- Folder structure is <input_folder>/EVENT_NAME/VERSION.json
- VERSION is semver compliant

Copies the latest version of each event type as <output_folder>/EVENT_NAME.json
"""


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} input_folder output_folder")
        sys.exit(-1)

    input_folder = Path(sys.argv[1])
    output_folder = Path(sys.argv[2])

    output_folder.mkdir(exist_ok=True)

    for type, version in versions.latest_in_dir(input_folder).items():
        input_file = input_folder / type / f"{version}.json"
        output_file = output_folder / f"{type}.json"
        copyfile(input_file, output_file)
        print(f"{input_file} => {output_file}")


if __name__ == "__main__":
    main()
