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

import subprocess
from pathlib import Path

import pytest
import semver

import versions


class Git:
    """Simple class for running Git commands in a given directory."""

    def __init__(self, path: Path):
        self.path = path
        self.command("init")
        # "git commit" requires that we identify ourselves.
        self.command("config", "user.name", "John Doe")
        self.command("config", "user.email", "john@example.com")

    def command(self, *args: str) -> None:
        subprocess.check_call(["git"] + list(args), cwd=self.path)


@pytest.fixture
def tmp_git(tmp_path):
    """Injects a Git instance rooted in a temporary directory."""
    yield Git(tmp_path)


def create_files(base_path: Path, *args: str) -> None:
    for p in args:
        fullpath = base_path / p
        fullpath.parent.mkdir(parents=True, exist_ok=True)
        fullpath.touch()


def test_latest_in_gitref(tmp_git):
    # Create a bunch of files in the git, commit them, and tag that commit.
    create_files(
        tmp_git.path,
        "subdir_c/6.0.0.json",
        "definitions/subdir_a/1.0.0.json",
        "definitions/subdir_a/2.0.0.json",
        "definitions/subdir_b/3.0.0.json",
        "definitions/subdir_b/4.0.0.json",
    )
    tmp_git.command("add", "-A")
    tmp_git.command("commit", "-m", "Initial set of files")
    tmp_git.command("tag", "v1.0.0")

    # Add an additional file and delete one of the original files.
    (tmp_git.path / "definitions/subdir_b/5.0.0.json").touch()
    tmp_git.command("rm", "definitions/subdir_a/2.0.0.json")
    tmp_git.command("add", "-A")
    tmp_git.command("commit", "-m", "Make changes")

    # Make sure the results we get are consistent with the original
    # contents of the git.
    assert versions.latest_in_gitref("v1.0.0", tmp_git.path, "definitions") == {
        "subdir_a": semver.VersionInfo.parse("2.0.0"),
        "subdir_b": semver.VersionInfo.parse("4.0.0"),
    }


def test_latest_in_dir(tmp_path):
    create_files(
        tmp_path,
        "subdir_c/6.0.0.json",
        "definitions/subdir_a/1.0.0.json",
        "definitions/subdir_a/2.0.0.json",
        "definitions/subdir_b/3.0.0.json",
        "definitions/subdir_b/4.0.0.json",
    )

    assert versions.latest_in_dir(tmp_path / "definitions") == {
        "subdir_a": semver.VersionInfo.parse("2.0.0"),
        "subdir_b": semver.VersionInfo.parse("4.0.0"),
    }
