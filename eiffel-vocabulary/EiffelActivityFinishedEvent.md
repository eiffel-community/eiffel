# EiffelActivityFinishedEvent
The EiffelActivityFinishedEvent declares that a previously started activity (declared by [EiffelActivityTriggeredEvent](./EiffelActivityTriggeredEvent.md) followed by [EiffelActivityStartedEvent](./EiffelActivityStartedEvent.md)) has finished.

## Data Members
### data.outcome
__Type:__ Object  
__Required:__ Yes  
__Description:__ The outcome of the activity.

#### data.outcome.verdict
__Type:__ String  
__Required:__ Yes  
__Legal values:__ SUCCESS, ???, ????, ABORTED, TIMEOUT, INCONCLUSIVE  
__Description:__ A terse standardized verdict of the activity, designed to be machine readable.  
SUCCESS signifies that the activity was concluded and the outcome matched expectations.  
??? signifies that the activity was concluded, but the outcome did not match expectations. To exemplify, a compilation job was successfully invoked, but compilation failed.  
???? signifies that the activity could not be successfully executed. To exemplify, a compilation could not be invoked, e.g. due to misconfiguration or environment issues.  
ABORTED signifies that the activity was aborted before it could be concluded.  
TIMEOUT signifies that the activity did not conclude within the allowed time frame.  
INCONCLUSIVE signifies that the outcome of the activity could not be determined.

#### data.outcome.description
__Type:__ String  
__Required:__ No  
__Description:__ A verbose description of the activity outcome, designed to provide human readers with further information.

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
* [Simple example](https://github.com/Ericsson/eiffel-examples/blob/master/events/EiffelActivityFinishedEvent/simple.json)