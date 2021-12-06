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

# EiffelTestCaseTriggeredEvent (TCT)
The EiffelTestCaseTriggeredEvent declares that the execution of a test case has been triggered, but not yet started. This can either be declared stand-alone or as part of an activity or test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively.

This event is used to communicate intent, and thereby serves a similar purpose to that of [EiffelActivityTriggeredEvent](./EiffelActivityTriggeredEvent.md). A triggered test case execution is expected to either be started (represented by [EiffelTestCaseStartedEvent](./EiffelTestCaseStartedEvent.md)) or canceled (represented by [EiffelTestCaseCanceledEvent](./EiffelTestCaseCanceledEvent.md)). Consequently, any delay between triggering and execution can be assumed to imply queuing time (e.g. waiting for available test resources) and monitored as such.

## Data Members
### data.testCase
__Type:__ Object  
__Required:__ Yes  
__Description:__ Identification of the test case to be executed.

#### data.testCase.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case tracker - typically a test management system.

#### data.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the test case to be executed.

#### data.testCase.version
__Type:__ String  
__Required:__ No  
__Description:__ The unique version of the identified test case to be executed. Where this property is not used it is assumed that test cases are not version controlled.

#### data.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved. To the extent that multiple versions of the same test case co-exist, this property SHALL identify the exact version to be executed.

### data.recipeId
__Type:__ String  
__Required:__ No  
__Description:__ If triggering this test case execution was the result of an Execution Recipe, as defined by an [EiffelTestExecutionRecipeCollectionCreatedEvent](./EiffelTestExecutionRecipeCollectionCreatedEvent.md), this UUID SHALL match the relevant __data.batches.recipes.id__ in that event.

### data.triggers
__Type:__ Object[]  
__Required:__ No  
__Description:__ The circumstances triggering the test case execution.

#### data.triggers.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ MANUAL, EIFFEL_EVENT, SOURCE_CHANGE, TIMER, OTHER  
__Description:__ The type of trigger.  
MANUAL signifies that the test case execution was manually triggered.  
EIFFEL_EVENT signifies that the test case execution was triggered by one or more Eiffel events. These events should be represented via __CAUSE__ links.  
SOURCE_CHANGE signifies that the test case execution was triggered as a consequence of a detected source change __not__ represented by Eiffel events.  
TIMER signifies that the test case execution was triggered by a timer.  
OTHER signifies any other triggering cause.

#### data.triggers.description
__Type:__ String  
__Required:__ No  
__Description:__ A description of the trigger.

### data.executionType
__Type:__ String  
__Required:__ No  
__Legal values:__ MANUAL, SEMI_AUTOMATED, AUTOMATED, OTHER  
__Description:__ The type of execution (often related to, but ultimately separate from, __data.triggers.type__).

### data.parameters
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of parameters to be passed to the test case execution.

#### data.parameters.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the parameter.

#### data.parameters.value
__Type:__ String  
__Required:__ Yes  
__Description:__ The value of the parameter.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### IUT
__Required:__ Yes  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the Item Under Test; in other words, the entity that is about to be tested.

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
See [Meta property description](./eiffel-syntax-and-usage/the-meta-object.md)

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 3.1.0     | [edition-lyon](../../../tree/edition-lyon)             | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelTestCaseTriggeredEvent/simple.json)
* [Simple example using pre-3.0.0 meta.security object](../examples/events/EiffelTestCaseTriggeredEvent/simple-2.0.0.json)
