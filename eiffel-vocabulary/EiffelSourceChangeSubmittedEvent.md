<!---
   Copyright 2017-2018 Ericsson AB.
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

# EiffelSourceChangeSubmittedEvent (SCS)
The EiffelSourceChangeSubmittedEvent declares that a change has been integrated into to a shared source branch of interest (e.g. "master", "dev" or "mainline") as opposed to a private or local branch. Note that it does not describe what has changed, but instead uses the __CHANGE__ link type to reference [EiffelSourceChangeCreatedEvent](./EiffelSourceChangeCreatedEvent.md).

Typical use cases for EiffelSourceChangeSubmittedEvent is to signal that a patch has passed code review and been submitted or that a feature/topic/team branch has been merged into the mainline/trunk/master. Where changes are made directly on the mainline, it is recommended to send both [EiffelSourceChangeCreatedEvent](./EiffelSourceChangeCreatedEvent.md) and EiffelSourceChangeSubmittedEvent together for information completeness.

Even though multiple types of identifiers are available (see below), the event SHOULD include one and SHALL not include more than one; changes to multiple repositories are represented by multiple events.

## Data Members
### data.submitter
__Type:__ Object  
__Required:__ No  
__Description:__ The agent (individual, group or machine) submitting the change. This is crucially different from the __data.author__ field of [EiffelSourceChangeCreatedEvent](./EiffelSourceChangeCreatedEvent.md).

#### data.submitter.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the submitter.

#### data.submitter.email
__Type:__ String  
__Required:__ No  
__Description:__ The email address of the submitter.

#### data.submitter.id
__Type:__ String  
__Required:__ No  
__Description:__ Any identity, username or alias of the submitter.

#### data.submitter.group
__Type:__ String  
__Required:__ No  
__Description:__ Any group or organization to which the submitter belongs.

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
### CHANGE
__Required:__ No  
__Legal targets:__ [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the change that was submitted.

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the submitted source change.

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.  

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md),
[EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelSourceChangeSubmittedEvent/simple.json)
