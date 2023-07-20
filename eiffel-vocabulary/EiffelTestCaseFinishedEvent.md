<!---
   This file was generated from ../definitions/EiffelTestCaseFinishedEvent/3.3.0.yml.
   See that file for a copyright notice.
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

#### data.persistentLogs.mediaType
__Type:__ String  
__Required:__ No  
__Description:__ The [media type](https://en.wikipedia.org/wiki/Media_type) of the URI's payload. Can be used to differentiate between various representations of the same log, e.g. text/html for human consumption and text/plain or application/json for the machine-readable form.

#### data.persistentLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.persistentLogs.tags
__Type:__ String[]  
__Required:__ No  
__Description:__ Arbitrary tags and keywords that describe this log.

#### data.persistentLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### TEST_CASE_EXECUTION
__Required:__ Yes  
__Legal targets:__ [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the relevant test case execution. In other words, [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md) acts as a handle for a particular test case execution. This differs from __CONTEXT__. In __TEST_CASE_EXECUTION__ the source carries information pertaining to the target (i.e. the test case execution started, finished or was canceled). In __CONTEXT__, on the other hand, the source constitutes a subset of the target (e.g. this test case was executed as part of that activity or test suite).

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.3.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.2.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add `data.persistentLogs.{mediaType,tags}`. |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.1 | [edition-toulouse](../../../tree/edition-toulouse) | data.outcome.metrics.value and data.outcome.metrics.name made mandatory. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelTestCaseFinishedEvent/simple.json)
