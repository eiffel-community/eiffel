<!---
   Copyright 2017 Ericsson AB.
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

# EiffelTestCaseStartedEvent (TCS)
The EiffelTestCaseStartedEvent declares that the execution of a test case has commenced. This event SHALL be preceded by a [EiffelTestCaseTriggeredEvent](./EiffelTestCaseTriggeredEvent.md), and appropriately linked to via __TEST_CASE_EXECUTION__.

## Data Members
### data.executor
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case executor, if applicable. This property can be used to identify tests executed by a particular test framework.

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