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

# EiffelTestCaseFinishedEvent (TCF)
The EiffelTestCaseFinishedEvent declares that a previously started test case (declared by [EiffelTestCaseStartedEvent](./EiffelTestCaseStartedEvent.md)) has finished and reports the outcome.

Note that while similar, the __data.outcome__ object is different from that of [EiffelActivityFinishedEvent](./EiffelActivityFinishedEvent.md). The outcome of the test case reports not only the conclusion of the test case execution - whether the test case was successfully executed - but also passes a verdict on the item under test. To highlight this conceptual difference, both __data.outcome.verdict__ and __data.outcome.conclusion__ are included.

Also note that unlike [EiffelTestSuiteFinishedEvent](./EiffelTestSuiteFinishedEvent.md), EiffelTestCaseFinishedEvent must report both __data.outcome.verdict__ and __data.outcome.conclusion__.

## Data Members
### data.outcome
__Type:__ Object  
__Required:__ Yes  
__Description:__ The outcome of the test case.

#### data.outcome.verdict
__Type:__ String  
__Required:__ Yes  
__Legal values:__ PASSED, FAILED, INCONCLUSIVE  
__Description:__ A terse standardized verdict on the item or items under test.  
PASSED signifies that the item or items under test successfully passed the test case.  
FAILED signifies that the item or items under test failed to pass the test case.  
INCONCLUSIVE signifies that the verdict of the test case was inconclusive. This SHOULD be the case if __data.outcome.conclusion__ is not __SUCCESSFUL__, but may in combination with a __SUCCESSFUL__ conclusion be used to represent unreliability or flakiness.

#### data.outcome.conclusion
__Type:__ String  
__Required:__ Yes  
__Legal values:__ SUCCESSFUL, FAILED, ABORTED, TIMED_OUT, INCONCLUSIVE  
__Description:__ A terse standardized conclusion of the test case, designed to be machine readable.  
SUCCESSFUL signifies that the test case was successfully concluded. Note that this does not imply that the item under test passed the tests.  
FAILED signifies that the test case could not be successfully executed. To exemplify, one or more tests failed to run due to required environments being unavailable.  
ABORTED signifies that the test case was aborted before it could be concluded.  
TIMED_OUT signifies that the test case did not conclude within the allowed time frame.  
INCONCLUSIVE signifies that the outcome of the test case could not be determined.

#### data.outcome.description
__Type:__ String  
__Required:__ No  
__Description:__ A verbose description of the test case outcome, designed to provide human readers with further information.

#### data.outcome.metrics
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of metrics collected during the test case execution. Note that while complete freedom is allowed in metrics names and value types, it is highly recommended to keep reported metrics concise and consistent. In other words, do not include excessive amounts of data (use __data.persistentLogs__ for that), and avoid unnecessary variations in value names or types over time.

##### data.outcome.metrics.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The metrics name.

##### data.outcome.metrics.value
__Type:__ Any  
__Required:__ Yes  
__Description:__ The metrics value.

### data.persistentLogs
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of persistent log files generated during execution. 

#### data.persistentLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.persistentLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 1.0.1     | Current version                                        | data.outcome.metrics.value and data.outcome.metrics.name made mandatory. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version. |


## Examples
* [Simple example](../examples/events/EiffelTestCaseFinishedEvent/simple.json)