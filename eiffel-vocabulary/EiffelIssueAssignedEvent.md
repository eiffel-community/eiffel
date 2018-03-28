<!---
   Copyright 2017 Jaden Young
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

# EiffelIssueAssignedEvent (IA)
The EiffelIssueAssignedEvent declares that an issue defined by an
[EiffelIssueDefinedEvent](./EiffelIssueDefinedEvent.md) has been assigned to a
contributor. The fields of an __assignee__ in this event are intended to mirror
the fields of an __author__ in
[EiffelSourceChangeCreatedEvent](./EiffelSourceChangeCreatedEvent.md) to
facilitate traceability.

## Data Members

### data.assignees
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ A list of people this issue is assigned to.

#### data.assignees.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the assignee.

#### data.assignees.email
__Type:__ String  
__Required:__ No  
__Description:__ The email address of the assignee.

#### data.assignees.id
__Type:__ String  
__Required:__ No  
__Description:__ Any identity, username or alias of the assignee.

#### data.assignees.group
__Type:__ String  
__Required:__ No  
__Description:__ Any group or organization to which the assignee belongs.

## Links

### ISSUE
__Required:__ Yes  
__Legal targets:__ [EiffelIssueDefinedEvent](./EiffelIssueDefinedEvent)  
__Multiple allowed:__ No    
__Description:__ Identifies the issue to which contributors are being assigned.

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be
used in conjunction with __CONTEXT__: individual events providing __CAUSE__
within a larger context gives rise to ambiguity. It is instead recommended to
let the root event of the context declare __CAUSE__.

### CONTEXT
__Required:__ No  
__Legal targets:__
[EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md),
[EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event
constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__
[EiffelFlowContextDefinedEvent](./EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the flow context of the event: which is the
continuous integration and delivery flow in which this occurred – e.g. which
product, project, track or version this is applicable to.

## Meta Members
### meta.id
__Type:__ String  
__Format:__ [UUID](http://tools.ietf.org/html/rfc4122)  
__Required:__ Yes  
__Description:__ The unique identity of the event, generated at event
creation.

### meta.type
__Type:__ String  
__Format:__ An event type name  
__Required:__ Yes  
__Description:__ The type of event. This field is required by the recipient
of the event, as each event type has a specific meaning and a specific set of
members in the __data__ and __links__ objects.

### meta.version
__Type:__ String  
__Format:__ [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html)  
__Required:__ Yes  
__Description:__ The version of the event type. This field is required by the
recipient of the event to interpret the contents. Please see
[Versioning](../eiffel-syntax-and-usage/versioning.md) for more information.

### meta.time
__Type:__ Integer  
__Format:__ Milliseconds since epoch.  
__Required:__ Yes  
__Description:__ The event creation timestamp.

### meta.tags
__Type:__ String[]  
__Format:__ Free text  
__Required:__ No  
__Description:__ Any tags or keywords associated with the events, for
searchability purposes.

### meta.source
__Type:__ Object  
__Format:__  
__Required:__ No  
__Description:__ A description of the source of the event. This object is
primarily for traceability purposes, and while optional, some form of
identification of the source is __HIGHLY RECOMMENDED__. It offers multiple
methods of identifying the source of the event, techniques which may be
select from based on the technology domain and needs in any particular use
case.

#### meta.source.domainId
__Type:__ String  
__Format:__ Free text  
__Required:__ No  
__Description:__ Identifies the domain that produced an event. A domain is an
infrastructure topological concept, which may or may not corresponds to an
organization or product structures. A good example would be Java packages
notation, ex. com.mycompany.product.component or mycompany.site.division.
Also, keep in mind that all names are more or less prone to change.
Particularly, it is recommended to avoid organizational names or site names,
as organizations tend to be volatile and development is easily relocated.
Relatively speaking, product and component names tend to be more stable and
are therefore encouraged, while code names may be an option. You need to
decide what is the most sensible option in your case.

#### meta.source.host
__Type:__ String  
__Format:__ Hostname  
__Required:__ No  
__Description:__ The hostname of the event sender.

#### meta.source.name
__Type:__ String  
__Format:__ Free text  
__Required:__ No  
__Description:__ The name of the event sender.

#### meta.source.serializer
__Type:__ Object  
__Format:__   
__Required:__ No  
__Description:__ The
[GAV](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
coordinates of the serializer software used to construct the event.

##### meta.source.serializer.groupId
__Type:__ String  
__Format:__ groupId  
__Required:__ Yes  
__Description:__ The groupId of the serializer software.

##### meta.source.serializer.artifactId
__Type:__ String  
__Format:__ artifactId  
__Required:__ Yes  
__Description:__ The artifactId of the serializer software.

##### meta.source.serializer.version
__Type:__ String  
__Format:__ version  
__Required:__ Yes  
__Description:__ The version of the serializer software.

#### meta.source.uri
__Type:__ String  
__Format:__ URI  
__Required:__ No  
__Description:__ The URI of, related to or describing the event sender.

### meta.security
__Type:__ Object  
__Format:__  
__Required:__ No  
__Description:__ An optional object for enclosing security related
information, particularly supporting data integrity. See
[Security](../eiffel-syntax-and-usage/security.md) for further information.

#### meta.security.sdm
__Type:__ Object  
__Format:__  
__Required:__ No  
__Description:__ An optional object for properties supporting the [Strong
Distribution Model](http://www.cryptnet.net/fdp/crypto/strong_distro.html).
Note that this only addressed the _integrity_ of the Eiffel event, not its
_confidentiality_ or _availability_.

##### meta.security.sdm.authorIdentity
__Type:__ String  
__Format:__  
__Required:__ Yes  
__Description:__ The identity of the author of the event. This property is
intended to enable the recipient to look up the appropriate public key for
decrypting the digest and thereby verifying author identity and data
integrity. The format of the author identity varies depending on the key
infrastructure solution used. Note that this requires the presence of a
Trusted Authority (TA) which the recipient can query for the correct public
key. The identity and location of the TA must never be included in the event
itself, as this would compromise the security of the solution.

##### meta.security.sdm.encryptedDigest
__Type:__ String  
__Format:__  
__Required:__ Yes  
__Description:__ The encrypted digest. The cryptographic hash function and
the decryption algorithm to use, similarly to the Trusted Authority (TA),
must be known to the recipient. Note that the digest of the entire event is
affected by the value of this property. For this reason the input to the hash
function SHALL be the entire event unaltered in all parts except for this
property, which SHALL be replaced by an empty string.

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 1.0.0     | Current version                                        | Initial version.                        |

## Examples

