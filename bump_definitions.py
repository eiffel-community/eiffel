#!/usr/bin/env python3

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

"""Creates new versions of existing type definitions by increasing the
desired version position (major, minor, or patch) and creating a new
matching file.
"""

import argparse
import fnmatch
import re
import sys
import time
from pathlib import Path
from typing import List
from typing import Optional

import semver

import versions


def _bump_versions(
    root: Path, position: str, pattern: str, history_entry: Optional[str] = None
) -> List[Path]:
    """Find definition files in the given directory, match their types
    against the given glob pattern, and create new files with version
    bumps in the selected position. Return the paths of the created
    files.
    """
    result = []
    for typename, version in versions.latest_in_dir(root).items():
        if not fnmatch.fnmatch(typename, pattern):
            continue

        old_path = root / typename / f"{version}.yml"
        new_version = getattr(version, "bump_" + position)()
        new_path = old_path.with_name(f"{new_version}.yml")
        new_path.write_text(
            _transform_definition(
                old_path.read_text(encoding="utf-8"),
                new_version,
                history_entry=history_entry,
            ),
            encoding="utf-8",
        )
        result.append(new_path)
    return result


def _transform_definition(
    old_definition: str,
    version: semver.version.Version,
    history_entry: Optional[str] = None,
    copyright_year: int = None,
) -> str:
    """Return an updated type definition with the new version and
    copyright year patched in, and a new entry in the history table.
    """
    result = re.sub(
        r"^_version: (.*)$", f"_version: {version}", old_definition, flags=re.M
    )

    current_year = copyright_year or time.localtime(time.time()).tm_year
    for expr, repl in (
        # Replace the end year in a range.
        (
            r"^# Copyright (20\d\d)-20\d\d ",
            f"# Copyright \\1-{current_year} ",
        ),
        # Turn a single year into a range.
        (
            r"^# Copyright (20\d\d) ",
            f"# Copyright \\1-{current_year} ",
        ),
        # Transform nonsense ranges on the form 2024-2024 back into a single year.
        (
            f"^# Copyright {current_year}-{current_year} ",
            f"# Copyright {current_year} ",
        ),
    ):
        result = re.sub(expr, repl, result, flags=re.M)

    history_entry = history_entry or "PLEASE UPDATE"
    result = re.sub(
        r"^_history:$",
        f"_history:\n  - version: {version}\n    changes: {history_entry}",
        result,
        flags=re.M,
    )

    return result


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "position",
        metavar="POSITION",
        choices=("major", "minor", "patch"),
        help="the version position that should be increased",
    )
    argparser.add_argument(
        "pattern",
        metavar="TYPE_PATTERN",
        help="a glob pattern that selects which types should be bumped",
    )
    argparser.add_argument(
        "--history-entry",
        metavar="TEXT",
        help="the text that should be added to the new version's history table",
    )
    args = argparser.parse_args(sys.argv[1:])
    for path in _bump_versions(
        Path("definitions"),
        args.position,
        args.pattern,
        history_entry=args.history_entry,
    ):
        print(path)
