<!---
   Copyright 2018 Ericsson AB.
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

# Contributing to Eiffel
Thank you for contributing to the Eiffel protocol and its implementations!

The following is a set of guidelines for contributing to the Eiffel protocol or any of its implementations.

## How to Propose Changes
Anyone is welcome to propose changes to the Eiffel protocol by creating a new [Issue](https://github.com/Ericsson/eiffel/issues) ticket in GitHub. These requests may concern anything contained in the repo: changes to documentation, changes to definitions, requests for additional information, additional event types, requests for additional examples et cetera.

When posting a new issue, try to be as precise as possible and phrase your arguments for your request carefully. Keep in mind that defining a shared protocol is often an exercise in finding workable compromises between multiple and often conflicting needs. In particular, pay attention to the following:
1. What type of change is requested?
1. Why would you like to see this change?
1. Can you provide any concrete examples?
1. Which arguments in favor can you think of?
1. Which arguments against can you think of, and why are they outweighed by the arguments in favor?

Also, keep in mind that just as anyone is welcome to propose a change, anyone is welcome to disagree with and criticize that proposal.

### Closing Issues
An Issue can be closed by any member of the [Eiffel team](https://github.com/orgs/Ericsson/teams/eiffel). This can happen in various ways, for varying reasons:
1. Issues without conclusion and no activity for at least 14 days may be closed, as a mere housekeeping activity. For instance, an Issue met with requests for further clarification, but left unanswered by the original author, may simply be removed.
1. Issues may simply be rejected if found unfeasible or undesirable. In such cases they shall also be responded to, providing a polite and concise explanation as to why the proposal is rejected.
1. Issues may be closed because they are implemented. Following the successful merging of a pull request addressing an Issue, it will be closed.

## How to Contribute
While we welcome requests for changes (in the form of Issues), we absolutely love ready solutions (in the form of Pull Requests). The best requests are the ones with Pull Requests to go along with them.

Contributions can be made by anyone using the standard [GitHub Fork and Pull model](https://help.github.com/articles/about-pull-requests). When making a pull request, keep a few things in mind.
1. Always explicitly connect a pull request to an Issue. See [How to Propose Changes](./how-to-propose-changes.md) for further information.
1. Make sure you target the correct branch. If you are unsure which branch is appropriate, ask in the Issue thread.
1. Pull Requests will be publicly reviewed, criticized, and potentially rejected. Don't take it personally.

### Reviewing and Merging Pull Requests
We use the Squash and Merge model, which means that all commits in a Pull Request get squashed into a single commit in the target branch. In other words, the revision history will look like a string of single commits corresponding one-to-one with Issues.

Pull requests can be merged by members of the [Eiffel team](https://github.com/orgs/Ericsson/teams/eiffel). There is a certain protocol to adhere to, however, as well as expectations on membership.
1. All members of the Eiffel team are expected to make the effort to participate in the review of Pull Requests. Every member may not review everything in detail, but everyone can make the effort to chime in on some. Remember that expedient high quality reviews are crucial to the long term survival of any open source project.
1. Eiffel team members are strongly encouraged to participate in reviews even if they do not feel entirely qualified to assess the pull request. Looking at changes and participating in review discussions is one of the best ways to learn, and presents an excellent opportunity to ask questions. And remember, participating in a review is not the same as having to make the final decision.
1. Anyone can participate in reviews, not only Eiffel team members.
1. A Pull Request should be approved by at least two Eiffel team members (including the one doing the merging). For this to function well, the above point on participation is critical.
1. Do not feel any pressure to merge Pull Requests. Unless you feel confident about what you are doing, don't press that big green button. Instead, ask a more senior member to make the decision.
1. When squashing and merging, ensure that the description reflects the change. Detailing every individual commit in the Pull Request is unnecessary, as they are squashed anyway. Instead, describe the change as a single thing. That description should always include an Issue reference, and should focus on WHY the change was made, to provide the reader with context. See [this excellent guide](https://chris.beams.io/posts/git-commit) on writing good commit messages.

### License Management
To be accepted into the repository, contributions must be licensed under the Apache License 2.0. Consequently, a license notice shall be included in suitable comment syntax where applicable. This license notice shall state the copyright holder(s) and point to the commit history for a full list of individual contributors, on the following format:

> Copyright <Year(s)> <Copyright holder of original contribution [and others].>  
> For a full list of individual contributors, please see the commit history.

The copyright holder is either the individual contributor if they act on their own behalf, or any organization on whose behalf they contribute. When multiple copyright holders have contributed to the same file, the copyright notice shall be appended "and others". The copyright year(s) shall reflect the year(s) of contribution(s) and be updated accordingly when new contributions are made to the file. To exemplify, the copyright notice of an original contribution made by Jane Doe acting on behalf of Ericsson AB may read:

> Copyright 2018 Ericsson AB.  
> For a full list of individual contributors, please see the commit history.

When John Doe, acting on his own behalf, makes a subsequent addition to the same file, the notice will be updated accordingly:

> Copyright 2018 Ericsson AB and others.  
> For a full list of individual contributors, please see the commit history.

When John Doe makes a subsequent contribution the following year, the notice will again be updated:

> Copyright 2018-2019 Ericsson AB and others.  
> For a full list of individual contributors, please see the commit history.
