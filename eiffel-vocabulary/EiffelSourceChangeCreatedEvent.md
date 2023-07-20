<!---
   This file was generated from ../definitions/EiffelSourceChangeCreatedEvent/4.2.0.yml.
   See that file for a copyright notice.
--->

# EiffelSourceChangeCreatedEvent (SCC)

The EiffelSourceChangeCreatedEvent declares that a change to sources has been made, but not yet submitted (see [EiffelSourceChangeSubmittedEvent](./EiffelSourceChangeSubmittedEvent.md)). This can be used to represent a change done on a private branch, undergoing review or made in a forked repository. Unlike EiffelSourceChangeSubmittedEvent, EiffelSourceChangeCreatedEvent _describes the change_ in terms of who authored it and which issues it addressed.

Where changes are integrated (or "submitted") directly on a shared branch of interest (e.g. "master", "dev" or "mainline") both EiffelSourceChangeCreatedEvent and EiffelSourceChangeSubmittedEvent are sent together.

## Data Members

### data.author
__Type:__ Object  
__Required:__ No  
__Description:__ The author of the change.

#### data.author.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the author.

#### data.author.email
__Type:__ String  
__Required:__ No  
__Description:__ The email address of the author.

#### data.author.id
__Type:__ String  
__Required:__ No  
__Description:__ Any identity, username or alias of the author.

#### data.author.group
__Type:__ String  
__Required:__ No  
__Description:__ Any group or organization to which the contributor belongs.

### data.change
__Type:__ Object  
__Required:__ No  
__Description:__ A summary of the change.

#### data.change.insertions
__Type:__ Integer  
__Required:__ No  
__Description:__ The number of inserted lines in the change.

#### data.change.deletions
__Type:__ Integer  
__Required:__ No  
__Description:__ The number of deleted lines in the change.

#### data.change.files
__Type:__ String  
__Required:__ No  
__Description:__ A URI to a list of files changed, on JSON String array format.

#### data.change.details
__Type:__ String  
__Required:__ No  
__Description:__ A URI to further details about the change. These details are not assumed to be on any standardized format, and may be intended for human and/or machine consumption. Examples include e.g. Gerrit patch set descriptions or GitHub commit pages. It is recommended to also include __data.change.tracker__ to provide a hint as to the nature of the linked details.

#### data.change.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the tracker, if any, of the change. Examples include e.g. Gerrit or GitHub.

#### data.change.id
__Type:__ String  
__Required:__ No  
__Description:__ The unique identity, if any, of the change (apart from what is expressed in the identifier object). Examples include e.g. Gerrit Change-Ids or GitHub Pull Requests. It is recommended to also include __data.change.tracker__ to provide a hint as to the nature of the identity.

### data.gitIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a Git change.

#### data.gitIdentifier.commitId
__Type:__ String  
__Required:__ Yes  
__Description:__ The commit identity (hash) of the change.

#### data.gitIdentifier.branch
__Type:__ String  
__Required:__ No  
__Description:__ The name of the branch where the change was made.

#### data.gitIdentifier.repoName
__Type:__ String  
__Required:__ No  
__Description:__ The name of the repository containing the change.

#### data.gitIdentifier.repoUri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the repository containing the change.

### data.svnIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a Subversion change.

#### data.svnIdentifier.revision
__Type:__ Integer  
__Required:__ Yes  
__Description:__ The revision of the change.

#### data.svnIdentifier.directory
__Type:__ String  
__Required:__ Yes  
__Description:__ The directory (branch/tag) of the change.

#### data.svnIdentifier.repoName
__Type:__ String  
__Required:__ No  
__Description:__ The name of the repository containing the change.

#### data.svnIdentifier.repoUri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the repository containing the change.

### data.ccCompositeIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a composite ClearCase change – in other words, not single file commit, but analogous of repository-wide commits of e.g. SVN or Git.

#### data.ccCompositeIdentifier.vobs
__Type:__ String[]  
__Required:__ Yes  
__Description:__ The names of the changed ClearCase VOBs.

#### data.ccCompositeIdentifier.branch
__Type:__ String  
__Required:__ Yes  
__Description:__ The branch of the change.

#### data.ccCompositeIdentifier.configSpec
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the relevant ClearCase config spec.

### data.hgIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a Mercurial change.

#### data.hgIdentifier.commitId
__Type:__ String  
__Required:__ Yes  
__Description:__ The commit identity (hash) of the change.

#### data.hgIdentifier.branch
__Type:__ String  
__Required:__ No  
__Description:__ The branch of the change.

#### data.hgIdentifier.repoName
__Type:__ String  
__Required:__ No  
__Description:__ The name of the repo.

#### data.hgIdentifier.repoUri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the repo.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### BASE
__Required:__ No  
__Legal targets:__ [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the base revision of the created source change.

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### DERESOLVED_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an issue which was previously resolved, but that this SCC claims it has made changes to warrant removing the resolved status. For example, if an issue "Feature X" was resolved, but this SCC removed the implementation that led to "Feature X" being resolved, that issue should no longer be considered resolved.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### PARTIALLY_RESOLVED_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an issue that this event partially resolves. That is, this SCC introduces some change that has advanced an issue towards a resolved state, but not completely resolved.

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the created source change.

### RESOLVED_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an issue that this SCC is claiming it has done enough to resolve. This is not an authoritative resolution, only a claim. The issue may or may not change status as a consequence this, e.g. through a [successful verification](../eiffel-vocabular/EiffelIssueVerifiedEvent.md) or a manual update on the issue tracker.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 4.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 4.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 4.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Replaced data.issues with links |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelSourceChangeCreatedEvent/simple.json)
