# How to Contribute

Contributions can be made by anyone using the standard [GitHub Fork and Pull model](https://help.github.com/articles/about-pull-requests). When making a pull request, keep a few things in mind.
1. Always explicitly connect a pull request to an Issue. See [How to Propose Changes](./how-to-propose-changes.md) for further information.
1. Make sure you target the correct branch. If you are unsure which branch is appropriate, ask in the Issue thread.
1. Pull Requests will be publicly reviewed, criticized, and potentially rejected. Don't take it personally.

## Reviewing and Merging Pull Requests
We use the Squash and Merge model, which means that all commits in a Pull Request get squashed into a single commit in the target branch. In other words, the revision history will look like a string of single commits corresponding one-to-one with Issues.

Pull requests can be merged by members of the [Eiffel team](https://github.com/orgs/Ericsson/teams/eiffel). There is a certain protocol to adhere to, however, as well as expectations on membership.
1. All members of the Eiffel team are expected to make the effort to participate in the review of Pull Requests. Every member may not review everything in detail, but everyone can make the effort to chime in on some. Remember that expedient high quality reviews are crucial to the long term survival of any open source project.
1. Eiffel team members are strongly encouraged to participate in reviews even if they do not feel entirely qualified to assess the pull request. Looking at changes and participating in review discussions is one of the best ways to learn, and presents an excellent opportunity to ask questions. And remember, participating in a review is not the same as having to make the final decision.
1. Anyone can participate in reviews, not only Eiffel team members.
1. A Pull Request should be approved by at least two Eiffel team members (including the one doing the merging). For this to function well, the above point on participation is critical.
1. Do not feel any pressure to merge Pull Requests. Unless you feel confident about what you are doing, don't press that big green button. Instead, ask a more senior member to make the decision.
1. When squashing and merging, ensure that the description reflects the change. Detailing every individual commit in the Pull Request is unnecessary, as they are squashed anyway. Instead, describe the change as a single thing. That description should always include an Issue reference. A lot of the time a descriptive title and an Issue reference is all that is needed.