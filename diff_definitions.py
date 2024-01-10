#!/usr/bin/env python3

# Copyright 2024 Axis Communications AB.
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

"""Context-sensitive diffing of Eiffel type definitions. Compares the
current workspace's latest type versions with the ones from a specified
base, and prints diff commands. For example, if the current commit has
added v4.3.0 of ActT and the given base had v4.2.0 as its latest version,
you'll get the following output:

diff -u definitions/EiffelActivityTriggeredEvent/4.2.0.yml definitions/EiffelActivityTriggeredEvent/4.3.0.yml
diff -u schemas/EiffelActivityTriggeredEvent/4.2.0.json schemas/EiffelActivityTriggeredEvent/4.3.0.json

By default, the base of the comparison is origin/master, but any commit
reference can be given as an argument.
"""

import sys
from pathlib import Path

import versions


def _main():
    base = "origin/master"
    if len(sys.argv) > 2:
        print(f"Usage: python {sys.argv[0]} [ base ]")
        sys.exit(-1)
    elif len(sys.argv) == 2:
        base = sys.argv[1]

    base_defs = versions.latest_in_gitref(base, ".", Path("definitions"))
    workspace_defs = versions.latest_in_dir(Path("definitions"))
    for type, workspace_version in sorted(workspace_defs.items()):
        base_version = base_defs.get(type)
        if not base_version:
            print(f"diff -u /dev/null definitions/{type}/{workspace_version}.yml")
            print(f"diff -u /dev/null schemas/{type}/{workspace_version}.json")
        elif base_version != workspace_version:
            print(
                f"diff -u definitions/{type}/{base_version}.yml definitions/{type}/{workspace_version}.yml"
            )
            print(
                f"diff -u schemas/{type}/{base_version}.json schemas/{type}/{workspace_version}.json"
            )


if __name__ == "__main__":
    _main()
