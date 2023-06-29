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
currently available types with the ones from a specified base and
prints diff commands. For example, if the current commit has added
v4.3.0 of ActT you'll get the following output:

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

    earlier = versions.latest_in_gitref(base, ".", Path("definitions"))
    current = versions.latest_in_dir(Path("definitions"))
    for type, current_version in sorted(current.items()):
        earlier_version = earlier.get(type)
        if not earlier_version:
            print(f"diff -u /dev/null definitions/{type}/{current_version}.yml")
            print(f"diff -u /dev/null schemas/{type}/{current_version}.json")
        elif earlier_version != current_version:
            print(
                f"diff -u definitions/{type}/{earlier_version}.yml definitions/{type}/{current_version}.yml"
            )
            print(
                f"diff -u schemas/{type}/{earlier_version}.json schemas/{type}/{current_version}.json"
            )


if __name__ == "__main__":
    _main()
