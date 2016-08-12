# EiffelTestSuiteFinishedEvent
The EiffelTestSuiteFinishedEvent declares that a previously started test suite (declared by [EiffelTestSuiteStartedEvent](./EiffelTestSuiteStartedEvent.md)) has finished and reports the outcome.

Note that while similar, the __data.outcome__ object is different from that of [EiffelActivityFinishedEvent](./EiffelActivityFinishedEvent.md). The outcome of the test suite reports not only the conclusion of the test suite execution - whether the tests were successfully executed - but also passes a verdict on the item or items under test. To highlight this conceptual difference, both __data.outcome.verdict__ and __data.outcome.conclusion__ are included.

## Data Members
### data.outcome
__Type:__ Object  
__Required:__ Yes  
__Description:__ The outcome of the test suite.

#### data.outcome.verdict
__Type:__ String  
__Required:__ No  
__Legal values:__ PASSED, FAILED, INCONCLUSIVE  
__Description:__ A terse standardized verdict on the item or items under test. Unlike in [EiffelTestCaseFinishedEvent](./EiffelTestCaseFinishedEvent.md), this property is optional. It offers a method to summarize the verdict of the test suite as a whole, but may be skipped.
PASSED signifies that the item or items under test successfully passed the test suite.  
FAILED signifies that the item or items under test failed to pass the test suite.  
INCONCLUSIVE signifies that the verdict of the test suite was inconclusive. This SHOULD be the case if __data.outcome.conclusion__ is not __SUCCESSFUL__, but may in combination with a __SUCCESSFUL__ conclusion be used to represent unreliability or flakiness.

#### data.outcome.conclusion
__Type:__ String  
__Required:__ No  
__Legal values:__ SUCCESSFUL, FAILED, ABORTED, TIMED_OUT, INCONCLUSIVE  
__Description:__ A terse standardized conclusion of the test suite, designed to be machine readable.  Unlike in [EiffelTestCaseFinishedEvent](./EiffelTestCaseFinishedEvent.md), this property is optional. It offers a method to summarize the conclusion of the test suite as a whole, but may be skipped.
SUCCESSFUL signifies that the test suite was successfully concluded. Note that this does not imply that the item under test passed the tests.  
FAILED signifies that the test suite could not be successfully executed. To exemplify, one or more tests failued to run due to required environments being unavailable.  
ABORTED signifies that the test suite was aborted before it could be concluded.  
TIMED_OUT signifies that the test suite did not conclude within the allowed time frame.  
INCONCLUSIVE signifies that the outcome of the test suite could not be determined.

#### data.outcome.description
__Type:__ String  
__Required:__ No  
__Description:__ A verbose description of the test suite outcome, designed to provide human readers with further information.

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
* [Simple example](../examples/events/EiffelTestSuiteFinishedEvent/simple.json)