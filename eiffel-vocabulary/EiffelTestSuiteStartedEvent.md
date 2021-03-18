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

# EiffelTestSuiteStartedEvent (TSS)
The EiffelTestSuiteStartedEvent declares that the execution of a test suite has started. This can either be declared stand-alone or as part of an activity or other test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively.

In Eiffel, a test suite is nothing more or less than a collection of test case executions (see [EiffelTestCaseStartedEvent](./EiffelTestCaseStartedEvent.md)) and/or other test suite executions. The executed test suite may be an ad-hoc transient grouping of test cases that were executed at a particular time or place or for a particular purpose or a persistent entity tracked in a test management system - Eiffel makes no distinction or assumptions either way.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the test suite. Uniqueness is not required or checked, but is useful.

### data.categories
__Type:__ String[]  
__Required:__ No  
__Description:__ The category or categories of the test suite. This can be used to group multiple similar test suites for analysis and visualization purposes. Example usage is to categorize test suites required before release as "Pre-release tests".

### data.types
__Type:__ String[]  
__Required:__ No  
__Legal values:__ ACCESSIBILITY, BACKUP_RECOVERY, COMPATIBILITY, CONVERSION, DISASTER_RECOVERY, FUNCTIONAL, INSTALLABILITY, INTEROPERABILITY, LOCALIZATION, MAINTAINABILITY, PERFORMANCE, PORTABILITY, PROCEDURE, RELIABILITY, SECURITY, STABILITY, USABILITY  
__Description:__ The type or types of testing performed by the test suite, as [defined by ISO 29119](http://www.softwaretestingstandard.org).

### data.liveLogs
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of live log files available during execution. These shall not be presumed to be stored persistently; in other words, once the test suite has finished there is no guarantee that these links are valid. Persistently stored logs shall be (re-)declared by [EiffelTestSuiteFinishedEvent](./EiffelTestSuiteFinishedEvent.md).

#### data.liveLogs.mediaType
__Type:__ String  
__Required:__ No  
__Description:__ The [media type](https://en.wikipedia.org/wiki/Media_type) of the URI's payload. Can be used to differentiate between various representations of the same log, e.g. text/html for human consumption and text/plain or application/json for the machine-readable form.

#### data.liveLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.liveLogs.tags
__Type:__ String[]  
__Required:__ No  
__Description:__ Arbitrary tags and keywords that describe this log.

#### data.liveLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### TERC
__Required:__ No  
__Legal targets:__ [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ This link signifies that the test suite represented by this event groups all test case executions resulting from the [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md).

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
| 3.1.0     | No edition set                                         | Add `data.liveLogs.{mediaType,tags}`.   |
| 3.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelTestSuiteStartedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelTestSuiteStartedEvent/simple.json)
