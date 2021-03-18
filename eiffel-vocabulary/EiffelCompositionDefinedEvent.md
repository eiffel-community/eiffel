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

# EiffelCompositionDefinedEvent (CD)
The EiffelCompositionDefinedEvent declares a composition of items (artifacts, sources and other compositions) has been defined, typically with the purpose of enabling further downstream artifacts to be generated.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the composition.

### data.version
__Type:__ String  
__Required:__ No  
__Description:__ The version of the composition, if any. This is in a sense redundant, as relationships between compositions can be tracked via the __PREVIOUS_VERSION__ link type, but can be used for improved clarity and semantics.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### ELEMENT
__Required:__ No  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), 
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md), 
[EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an element and/or sub-composition of this composition. The latter is particularly useful for documenting large and potentially decentralized compositions, and may be used to reduce the need to repeat large compositions in which only small parts are subject to frequent change.

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the composition.

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
| 3.1.0     | [edition-paris](../../../tree/edition-paris)           | Added SCC as valid target for ELEMENT links (see [Issue 218](https://github.com/eiffel-community/eiffel/issues/218)) |
| 3.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelCompositionDefinedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelCompositionDefinedEvent/simple.json)
