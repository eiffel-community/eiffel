<!---
   Copyright 2017 Ericsson AB.

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

# EiffelTestCaseStartedEvent (TCS)
The EiffelTestCaseStartedEvent declares that the execution of a test case has commenced. This can either be declared stand-alone or as part of an activity or test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively. 

## Data Members
### data.testCase
__Type:__ Object  
__Required:__ Yes  
__Description:__ Identification of the executed test case.

#### data.testCase.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case tracker - typically a test management system.

#### data.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the executed test case.

#### data.testCase.version
__Type:__ String  
__Required:__ No  
__Description:__ The unique version of the executed test case identity. Where this property is not used it is assumed that test cases are not version controlled.

#### data.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved. To the extent that multiple versions of the same test case co-exist, this property SHALL identify the exact version executed.

### data.executor
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case executor, if applicable. This property can be used to identify tests executed by a particular test framework.

### data.recipeId
__Type:__ String  
__Required:__ No  
__Description:__ If this test case execution was the result of an Execution Recipe, as defined by an [EiffelTestExecutionRecipeCollectionCreatedEvent](./EiffelTestExecutionRecipeCollectionCreatedEvent.md), this UUID SHALL match the relevant __data.batches.recipes.id__ in that event.

### data.parameters
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of parameters passed to the test case execution.

#### data.parameters.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the parameter.

#### data.parameters.value
__Type:__ String  
__Required:__ Yes  
__Description:__ The value of the parameter.

### data.executionType
__Type:__ String  
__Required:__ No  
__Legal values:__ MANUAL, SEMI_AUTOMATED, AUTOMATED, OTHER  
__Description:__ The type of test case execution.

### data.liveLogs
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of live log files available during execution. These shall not be presumed to be stored persistently; in other words, once the test case execution has finished there is no guarantee that these links are valid. Persistently stored logs shall be (re-)declared by [EiffelTestCaseFinishedEvent](./EiffelTestCaseFinishedEvent.md).

#### data.liveLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.liveLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelTestCaseStartedEvent/simple.json)