# EiffelSourceChangeCreatedEvent
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

### data.issues
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of issues addressed by the change.

#### data.issues.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ BUG, IMPROVEMENT, FEATURE, WORK_ITEM, REQUIREMENT, OTHER  
__Description:__ The type of issue.
  
#### data.issues.tracker
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the issue tracker. This can unfortunately not be standardized, and is therefore context sensitive: though some trackers and ALM tools are more popular than others, an exhaustive enumeration is impossible, particularly when considering company specific internal solutions. Consequently one should not rely on the name as the primary method of retrieval, but rather __data.issues.uri__. __data.issues.tracker__ together with __data.issues.id__ is still useful for analysis and traceability, however, as long as it can be correctly interpreted.

#### data.issues.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The identity of the issue. This is tracker dependent - most trackers have their own issue naming schemes.

#### data.issues.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the issue.

#### data.issues.transition
__Type:__ String  
__Required:__ Yes  
__Legal values:__ RESOLVED, PARTIAL, REMOVED  
__Description:__ The new state of the issue: does the change resolve it, partially resolve it or remove it?

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

#### data.ccCompositeIdentifier.vob
__Type:__ String  
__Required:__ Yes  
__Description:__ The ClearCase VOB name.

#### data.ccCompositeIdentifier.branch
__Type:__ String  
__Required:__ Yes  
__Description:__ The branch of the change.

#### data.ccCompositeIdentifier.configSpecPath
__Type:__ String  
__Required:__ Yes  
__Description:__ Path to the relevant config spec.

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

### data.gerritIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a Gerrit patch.

#### data.gerritIdentifier.changeId
__Type:__ String  
__Required:__ Yes  
__Description:__ The Change-Id of the patch.

#### data.gerritIdentifier.patchSet
__Type:__ Integer  
__Required:__ Yes  
__Description:__ The Patch Set number.

#### data.gerritIdentifier.project
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the Gerrit project.

#### data.gerritIdentifier.branch
__Type:__ String  
__Required:__ Yes  
__Description:__ The branch of the patch.

#### data.gerritIdentifier.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the Gerrit change summary.

## Examples
* [Simple example](https://github.com/Ericsson/eiffel-examples/blob/master/events/EiffelSourceChangeCreatedEvent/simple.json)