# EiffelTestCaseStartedEvent
The EiffelTestCaseStartedEvent declares that the execution of a test case has commenced. This can either be declared stand-alone or as part of an activity or test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively. 

## Data Members
### data.testCase
__Type:__ Object  
__Required:__ Yes  
__Description:__ Identification of the executed test case.

#### data.testCase.tracker
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the test case tracker - typically a test management system.

#### data.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the executed test case.

#### data.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved.

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
__Description:__ An array of live log files available during execution. These shall not be presumed to be stored persistently; in other words, once the activity has finished there is no guarantee that these links are valid. Persistently stored logs shall be (re-)declared by [EiffelActivityFinishedEvent](./EiffelActivityFinishedEvent.md).

#### data.liveLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.liveLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Examples
* [Simple example](../examples/events/EiffelTestCaseStartedEvent/simple.json)