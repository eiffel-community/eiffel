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

"""The versions module contains functions for discovering definition files."""

import os
import subprocess
from pathlib import Path
from typing import Dict
from typing import Iterable

import semver


def latest_in_gitref(
    committish: str, gitdir: Path, subdir: Path
) -> Dict[str, semver.version.Version]:
    """Lists the definition files found under a given subdirectory of a
    git at a given point in time (described by a committish, e.g. a
    SHA-1, tag, or branch reference) and returns a dict that maps each
    typename (e.g. EiffelArtifactCreatedEvent) to the latest version found.
    """
    return _latest_versions(
        Path(line)
        for line in (
            subprocess.check_output(
                ["git", "ls-tree", "-r", "--name-only", committish, "--", subdir],
                cwd=gitdir,
            )
            .decode("utf-8")
            .splitlines()
        )
    )


def latest_in_dir(path: Path) -> Dict[str, semver.version.Version]:
    """Inspects the definition files found under a given path and returns
    a dict that maps each typename (e.g. EiffelArtifactCreatedEvent) to
    its latest version found.
    """
    return _latest_versions(
        Path(current) / f for current, _, files in os.walk(path) for f in files
    )


def _latest_versions(paths: Iterable[Path]) -> Dict[str, semver.version.Version]:
    """Given a list of foo/<typename>/<version>.<ext> pathnames, returns
    a dict mapping typenames to the most recent version of that type.
    """
    result = {}
    for path in paths:
        type = path.parent.name
        this_version = semver.VersionInfo.parse(Path(path.name).stem)
        if type not in result or result[type] < this_version:
            result[type] = this_version
    return result
