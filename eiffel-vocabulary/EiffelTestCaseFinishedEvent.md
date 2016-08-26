# EiffelTestCaseFinishedEvent
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

## Examples
* [Simple example](../examples/events/EiffelTestCaseFinishedEvent/simple.json)