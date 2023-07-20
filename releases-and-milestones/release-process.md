<!---
   Copyright 2022-2023 Axis Communications AB.
   For a full list of individual contributors, please see the commit history.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
--->

# Release process

This document describes the release process for Eiffel editions.

## Pre-release activities

Look up the name of the next edition in the [Versioning](../eiffel-syntax-and-usage/versioning.md) document.

GitHub [milestones](https://github.com/eiffel-community/eiffel/milestones?state=open) are used to track the proposed contents of an upcoming edition. Milestones are named "Edition \<name>", e.g. "Edition Arica". Issues, not pull requests, are added to the milestone.

## Making a release

When all issues in the scope of the edition have been closed and it's time to make the release, follow these steps:

1.  Verify that all issues in the [milestone](https://github.com/eiffel-community/eiffel/milestones?state=open) are closed.
1.  Create a pull request with the following changes (see [PR 277](https://github.com/eiffel-community/eiffel/pull/277) for reference):
    1.  Make sure history table entries with a missing `introduced_in` key get one that references the soon-to-be tag for the new edition. You can use [yq](https://mikefarah.gitbook.io/yq/) to identify these files: `for i in definitions/Eiffel*Event/*.yml ; do yq -e '._history | .[] | select(.introduced_in == null)' < $i > /dev/null 2>&1 && echo $i ; done`
    1.  Claim the edition in [versioning.md](../eiffel-syntax-and-usage/versioning.md), including a short summary of the changes in the edition.
    1.  Add an entry for the new edition to [generate_manifest.py](../generate_manifest.py). Unfortunately, this means that CI for the resulting commit won't succeed until the tag has been created (see next step).
1.  When the pull request has been merged, create and push an "edition-\<name>" annotated tag (use `git tag -a`). The tag comment could include a short version of the included changes to the protocol. Any new major versions of event types should be called out.
1.  Create a GitHub release based on the newly pushed tag. The tag comment can probably be reused as the release description.
1.  Create issue(s) for updating other repositories to reference the new edition:
    1. [eiffel-sepia](https://github.com/eiffel-community/eiffel-sepia)
1.  Announce the new edition on the eiffel-community mailing list, LinkedIn, and Slack and ask maintainers of other repositories to make necessary updates.
1.  Mark the edition's milestone as closed.
