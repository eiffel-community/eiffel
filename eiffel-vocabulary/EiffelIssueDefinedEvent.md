<!---
   Copyright 2018 Jaden Young
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

# EiffelIssueDefinedEvent (ID)
The EiffelIssueDefinedEvent declares that an issue has been created in some
external issue management software. ID is semantically similar to
[EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)
and [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md).

## Data Members

### data.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ BUG, IMPROVEMENT, FEATURE, WORK_ITEM, REQUIREMENT, OTHER  
__Description:__ The type of issue.  

### data.tracker
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the issue tracker. This can unfortunately not be
standardized, and is therefore context sensitive: though some trackers and ALM
tools are more popular than others, an exhaustive enumeration is impossible,
particularly when considering company specific internal solutions. Consequently
one should not rely on the name as the primary method of retrieval, but rather
__data.uri__. __data.tracker__ together with __data.id__
is still useful for analysis and traceability, however, as long as it can be
correctly interpreted.

### data.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The identity of the issue. This is tracker dependent - most
trackers have their own issue naming schemes.  

### data.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ A URI that links to a document describing the issue in depth.

### data.title
__Type:__ String  
__Required:__ No  
__Description:__ A one-line title or summary of the issue. This exists mostly
for human consumption, as "Implement widget X" is much more meaningful to a
human when viewing a graph of Eiffel events than "1302". This is not meant
to be a detailed description, as such information should be accessible by
following __data.uri__.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

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

## Meta
See [Meta property description](./eiffel-syntax-and-usage/the-meta-object.md)

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 3.1.0     | [edition-lyon](../../../tree/edition-lyon)             | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelIssueDefinedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.0.0     | [0706840](../../../blob/070684053ceb1da5fb42d9f0ef21df816961d6bc/eiffel-vocabulary/EiffelIssueDefinedEvent.md) | Initial version                         |

## Examples
* [Simple example](../examples/events/EiffelIssueDefinedEvent/simple.json)
