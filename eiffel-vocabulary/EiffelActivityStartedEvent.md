# EiffelActivityStartedEvent
The EiffelActivityStartedEvent declares that a triggered queued activity (declared by [EiffelActivityTriggeredEvent](./EiffelActivityTriggeredEvent.md)) has started.

## Data Members
### data.executionUri
__Type:__ String  
__Required:__ No  
__Description:__ Any URI at which further information about the execution may be found; a typical use case is to link a CI server job execution page.

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
* [Simple example](https://github.com/Ericsson/eiffel-examples/blob/master/events/EiffelActivityStartedEvent/simple.json)