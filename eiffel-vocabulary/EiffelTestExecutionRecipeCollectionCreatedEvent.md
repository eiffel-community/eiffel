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

# EiffelTestExecutionRecipeCollectionCreatedEvent (TERCC)
The EiffelTestExecutionRecipeCollectionCreatedEvent declares that a collection of test execution recipes has been created. In order to clarify what that means, several concepts need to be explained.

Just as Eiffel is an opinionated protocol, EiffelTestExecutionRecipeCollectionCreatedEvent is an opinionated event, and to a certain extent that opinion goes against the grain of traditional test management. This event assumes that activity configurations and test scope definitions are two separate things. To exemplify, when one's CI server triggers the Acceptance Test activity in the pipeline, there is nothing in that activity that says which tests to execute where or with what parameters: that is a separate concern. Instead, it will query a test selection service for that information. This information is encapsulated by the EiffelTestExecutionRecipeCollectionCreatedEvent, which contains all the information needed to configure and execute the tests.

How the test selection service generates the recipe collection is, from the point of view of the Eiffel protocol, irrelevant. It may very well be from a statically defined list of test cases, or from an elaborate test selection algorithm weighing together a host of factors to determine the optimal set of test cases to execute at any particular time, or a combination of the two.

The __data__ object consists of two main parts. __data.selectionStrategy__ identifies the strategy used to select the test cases and generate the recipe collection, while __data.batches__ or __data.batchesUri__ contain or reference, respectively, the recipes. The recipes are grouped in batches, which are used to control the order of execution of test cases. Every batch has a priority to let the test executor order them in sequence, but within each batch no assumptions are made as to the execution order the test cases. This way the recipe collection can either allow the executor a high degree of freedom in scheduling the test executions, and/or prescribe the exact sequential order in which they must be executed. Each event SHALL include one and only one of __data.batches__ and __data.batchesUri__.

Finally, each recipe (__data.batches.recipes__) consists of two parts: the test case to execute, and the constraints of that execution. The EiffelTestExecutionRecipeCollectionCreatedEvent does not control the syntax of these constraints, as the nature of such constraints are highly dependent on technology domain and test execution framework. That being said, there are three questions that typically need to be answered: what is the item under test, in what kind of environment is it to be tested, and what are the test parameters? Note the distinction between test case and test execution: it is perfectly legal for a single test case to appear multiple times within the same EiffelTestExecutionRecipeCollectionCreatedEvent, but (presumably) with different constraints.

## Data Members
### data.selectionStrategy
__Type:__ Object  
__Required:__ Yes  
__Description:__ The strategy used to select the test cases and generate the recipe collection.

#### data.selectionStrategy.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the selection strategy that generated the test execution recipe collection.

#### data.selectionStrategy.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the selection strategy that generated the test execution recipe collection.

#### data.selectionStrategy.uri
__Type:__ String  
__Required:__ No  
__Description:__ The URI at which the the selection strategy that generated the test execution recipe collection can be retrieved.

### data.batchesUri
__Type:__ String  
__Required:__ No  
__Description:__ A URI at which at which the array of test execution batches can be fetched. The format of the document at this URI SHALL be on the format prescribed by __data.batches__ (i.e. ``` [ { "name": "Batch 1", ...}, {...}] ```). Each event SHALL include one and only one of __data.batches__ and __data.batchesUri__.

### data.batches
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of batches of recipes. Each event SHALL include one and only one of __data.batches__ and __data.batchesUri__. In the interest of keeping message sizes small, it is recommended to use __data.batches__ only for limited numbers of test cases (on the order of ten executions). For larger numbers of executions, __data.batchesUri__ SHOULD be used instead.

#### data.batches.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the recipe batch.

#### data.batches.priority
__Type:__ Integer  
__Required:__ Yes  
__Description:__ The execution priority of the batch, as compared to other batches in the collection. A lower value SHALL be interpreted as a higher priority.

#### data.batches.recipes
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ The collection of test execution recipes within the batch.

##### data.batches.recipes.id
__Type:__ String  
__Required:__ Yes  
__Description:__ A UUID identifying the unique execution. Note that this is different from the id of a test case, in two ways. First, a test case is a (presumably) persistnent entity, whereas an execution is transient in nature. Second, a test case may be executed any number of times in any given recipe collection.

##### data.batches.recipes.testCase
__Type:__ Object  
__Required:__ Yes  
__Description:__ The test case to be executed in this execution recipe.

###### data.batches.recipes.testCase.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case tracker - typically a test management system.

###### data.batches.recipes.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the test case to be executed.

###### data.batches.recipes.testCase.version
__Type:__ String  
__Required:__ No  
__Description:__ The unique version of the identified test case to be executed. Where this property is not used it is assumed that test cases are not version controlled.

###### data.batches.recipes.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved. To the extent that multiple versions of the same test case co-exist, this property SHALL identify the exact version to be executed.

##### data.batches.recipes.constraints
__Type:__ Object[]  
__Required:__ No  
__Description:__ Any constraints of the execution. The nature of such constraints is highly dependent on technology domain and test execution framework. Consequently, there are no pre-defined or required constraints. Instead, this property is a list of key-value pairs on the same format as [data.customData](../customization/custom-data.md). That being said, there are three questions that typically need to be answered: what is the item under test, in what kind of environment is it to be tested, and what are the test parameters?

###### data.batches.recipes.constraints.key
__Type:__ String  
__Required:__ Yes  
__Description:__ The key name of constraint.

###### data.batches.recipes.constraints.value
__Type:__ Any  
__Required:__ Yes  
__Description:__ The value of the constraint.

#### data.batches.dependencies
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of test case execution dependencies. Ideally, test cases are atomic and can be executed in isolation. In cases where a test case assumes that another test case has been executed previously in the same environment, however, this property can be used to specify that. It serves as an instruction to the test executor to place two executions subsequent to one another in the same environment.

##### data.batches.dependencies.dependency
__Type:__ String  
__Required:__ Yes  
__Description:__ The UUID of the dependency execution (__data.batches.recipes.id__), i.e. the execution that shall be performed prior to that of the dependent.

##### data.batches.dependencies.dependent
__Type:__ String  
__Required:__ Yes  
__Description:__ The UUID of the dependent execution (__data.batches.recipes.id__), i.e. the execution that shall be performed only after that of the dependency.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

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
| 4.2.0     | No edition set                                         | Add missing testCase.version member (see [Issue 288](https://github.com/eiffel-community/eiffel/issues/288)). |
| 4.1.1     | [edition-lyon](../../../tree/edition-lyon)             | Add missing validation pattern to links.target member (see [Issue 271](https://github.com/eiffel-community/eiffel/issues/271)). |
| 4.1.0     | No edition set                                         | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 4.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 3.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 2.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 2.0.0     | [f92e001](../../../blob/f92e001c88d1139a62f8ace976958e0a30d8f9c5/eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md) | Changed syntax of data.batches.recipes.constraints from an uncontrolled object to a list of key-value pairs to comply with design guidelines. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Example using data.batches](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batches.json)
* [Example using data.batches (1.0.0 syntax)](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batches-1.0.0.json)
* [Example using data.batchesUri](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batchesUri.json)
