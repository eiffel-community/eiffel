<!---
   Copyright 2017-2020 Ericsson AB and others.
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

# EiffelArtifactPublishedEvent (ArtP)
The EiffelArtifactPublishedEvent declares that a software artifact (declared by [EiffelArtifactCreatedEvent](./EiffelArtifactCreatedEvent.md)) has been published and is consequently available for retrieval at one or more locations.

## Data Members
### data.locations
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ A list of locations at which the artifact may be retrieved.

#### data.locations.name
__Type:__ String  
__Required:__ No  
__Description:__ Identifies the name of the file within the artifact for which this location provides the URI. Must correspond to a __data.fileInformation.name__ value in the [EiffelArtifactCreatedEvent](./EiffelArtifactCreatedEvent.md) connected via the __ARTIFACT__ link.

#### data.locations.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ ARTIFACTORY, NEXUS, PLAIN, OTHER  
__Description:__ The type of location. May be used by (automated) readers to understand the method of retrieval, particularly with regards to authentication.  
ARTIFACTORY signifies an [Artifactory](https://www.jfrog.com/artifactory/)  
NEXUS signifies a [Nexus](http://www.sonatype.org/nexus/)  
PLAIN signifies a plain HTTP GET request.  
OTHER signifies other methods of retrieval. Note that using this type likely requires some foreknowledge on part of the reader in order to fetch the artifact.

#### data.locations.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the artifact can be retrieved.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### ARTIFACT
__Required:__ Yes  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the artifact that was published.

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
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

## Meta
See [Meta property description](./EiffelMetaProperty.md)

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 3.2.0     | [edition-lyon](../../../tree/edition-lyon)             | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.1.0     | [edition-paris](../../../tree/edition-paris)           | Added name qualifier for artifact locations (see [Issue 248](https://github.com/eiffel-community/eiffel/issues/248)) |
| 3.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelArtifactPublishedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelArtifactPublishedEvent/simple.json)
