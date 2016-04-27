# EiffelActivityQueuedEvent
The EiffelActivityQueuedEvent declares that a certain activity - typically a build, test or analysis activity - has been queued for execution. This implies that it has been triggered by some factor, and the event serves the dual purpose of identifying this triggering factor.

Many systems to not employ any queuing mechanism: an activity is simply started straight away when its triggering criteria are fulfilled. For coherence and consistency, the EiffelActivityQueuedEvent shall still be used: simply send the subsequent [EiffelActivityStartedEvent](./EiffelActivityStartedEvent.md) immediately after.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the activity. Uniqueness is not required or checked, but is useful.

### data.category
__Type:__ String  
__Required:__ No  
__Description:__ The category of the activity. This can be used to group multiple similar activities for analysis and visualization purposes. Example usage is to label the similar but unique build activities of all the components of system X as "System X Component Build" (whereas the name would be e.g. "System X Component Y Build").

### data.trigger
__Type:__ Object  
__Required:__ No  
__Description:__ The circumstances triggering the activity.

#### data.trigger.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ MANUAL, EIFFEL_EVENT, REBUILD, SOURCE_CHANGE, TIMER, OTHER  
__Description:__ The type of trigger.

#### data.trigger.description
__Type:__ String  
__Required:__ No  
__Description:__ A description of the trigger.

### data.executionType
__Type:__ String  
__Required:__ No  
__Legal values:__ MANUAL, SEMI_AUTOMATED, AUTOMATED, OTHER  
__Description:__ The type of execution (often related to, but ultimately separate from, __data.trigger.type__).

## Schema
TBD