# EiffelActivityFinishedEvent
The EiffelActivityFinishedEvent declares that a previously queued activity (declared by [EiffelActivityQueuedEvent](./EiffelActivityQueuedEvent.md)) has finished.

## Data Members
### data.outcome
__Type:__ Object  
__Required:__ Yes  
__Description:__ The outcome of the activity.

#### data.outcome.verdict
__Type:__ String  
__Required:__ Yes  
__Legal values:__ SUCCESS, FAILURE, ERROR, ABORTED, TIMEOUT  
__Description:__ A terse standardized verdict of the activity, designed to be machine readable.

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
