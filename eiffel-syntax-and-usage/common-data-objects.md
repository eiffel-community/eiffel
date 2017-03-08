# Common Data Objects
Some events reference the same type of __data__ objects. Instead of describing them for each event type they have a common description here.

## Test Case Object
### data.*.testCase
__Type:__ Object  
__Required in:__ [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md), [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md)  
__Optional in:__ [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Description:__ A description of a test case.

#### data.*.testCase.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case tracker - typically a test management system.

#### data.*.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the test case.

#### data.*.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved.
