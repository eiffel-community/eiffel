<!---
   Copyright 2017-2021 Ericsson AB and others.
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

# EiffelArtifactCreatedEvent (ArtC)
The EiffelArtifactCreatedEvent declares that a software artifact has been created, what its coordinates are, what it contains and how it was created.

## Data Members
### data.identity
__Type:__ String  
__Format:__ [purl specification](https://github.com/package-url/purl-spec)  
__Required:__ Yes  
__Description:__ The identity of the created artifact, in [purl format](https://github.com/package-url/purl-spec).

### data.fileInformation
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of the artifact file contents. This information is optional and, when included, MAY include a complete or incomplete list of contents. In other words, it may be used to highlight only particular files of interest, such as launcher binaries or other entry-points.

#### data.fileInformation.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name (including relative path from the root of the artifact) on syntax appropriate for the artifact packaging type.

#### data.fileInformation.tags
__Type:__ String[]  
__Required:__ No  
__Description:__ Any tags associated with the file, to support navigation and identification of items of interest.

### data.buildCommand
__Type:__ String  
__Required:__ No  
__Description:__ The command used to build the artifact within the identified environment. Used for reproducability purposes.

### data.requiresImplementation
__Type:__ String  
__Required:__ No  
__Legal values:__ NONE, ANY, EXACTLY_ONE, AT_LEAST_ONE  
__Description:__ Defines whether this artifact requires an implementing artifact. This is typically used for interfaces requiring some backend implementation, although the interface does not presume to define _which_ implementation. Implicitly interpreted as "ANY" if undefined.  
NONE signifies that there SHALL no implementations of this artifact. In other words, a composition containing another artifact identifying it in __data.implements__ would be illegal.  
ANY signifies that there may or may not be implementations of this artifact.  
EXACTLY_ONE signifies that a legal composition must contain one and only one implementation of this artifact.  
AT_LEAST_ONE signifies that a legal composition must contain one or more implementations of this artifact.

### data.implements
__Type:__ String[]  
__Format:__ [purl specification](https://github.com/package-url/purl-spec)  
__Required:__ No  
__Description:__ An array of [purl identified](https://github.com/package-url/purl-spec) entities this artifact implements. The typical use case of this is to identify interfaces implemented by this artifact. While not included in the purl specification itself, the Eiffel protocol allows version range notation according to [Maven syntax](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN402) to be used for the version component of the package identity. Note that the purl specification always requires the version component to be percent-encoded.

### data.dependsOn
__Type:__ String[]  
__Format:__ [purl specification](https://github.com/package-url/purl-spec)  
__Required:__ No  
__Description:__ An array of [purl identified](https://github.com/package-url/purl-spec) entities this artifact depends on. While not included in the purl specification itself, the Eiffel protocol allows version range notation according to [Maven syntax](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN402) to be used for the version component of the package identity. Note that the purl specification always requires the version component to be percent-encoded.

### data.name
__Type:__ String  
__Required:__ No  
__Description:__ Any (colloquial) name of the artifact. Unlike __data.identity__, this is not intended as an unambiguous identifier of the artifact, but as a descriptive and human readable name.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### COMPOSITION
__Required:__ No  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the composition from which this artifact was built.

### ENVIRONMENT
__Required:__ No  
__Legal targets:__ [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the environment in which this artifact was built.

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the artifact the event represents.

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
| 3.1.0     | [edition-lyon](../../../tree/edition-lyon)             | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelArtifactCreatedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelArtifactCreatedEvent/simple.json)
* [Interface example](../examples/events/EiffelArtifactCreatedEvent/interface.json)
* [Backend example](../examples/events/EiffelArtifactCreatedEvent/backend.json)
* [Dependent example](../examples/events/EiffelArtifactCreatedEvent/dependent.json)
