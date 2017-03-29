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

# EiffelActivityTriggeredEvent (ActT)
The EiffelActivityTriggeredEvent declares that a certain activity - typically a build, test or analysis activity - has been triggered by some factor. Note that this is crucially different from the activity execution having _started_ (as declared by [EiffelActivityStartedEvent](./EiffelActivityStartedEvent.md)).

In a situation where execution follows immediately upon triggering these two events should be sent together. Where that is not the case (e.g. due to queuing) the time delta between EiffelActivityTriggeredEvent and EiffelActivityStartedEvent constitutes the queue time.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the activity. Uniqueness is not required or checked, but is useful.

### data.categories
__Type:__ String[]  
__Required:__ No  
__Description:__ Any categorization of the activity. This can be used to group multiple similar activities for analysis and visualization purposes. Example usage is to label the similar but unique build activities of all the components of system X as "System X Component Build" (whereas the name would be e.g. "System X Component Y Build").

### data.triggers
__Type:__ Object[]  
__Required:__ No  
__Description:__ The circumstances triggering the activity.

#### data.triggers.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ MANUAL, EIFFEL_EVENT, SOURCE_CHANGE, TIMER, OTHER  
__Description:__ The type of trigger.  
MANUAL signifies that the activity was manually triggered.  
EIFFEL_EVENT signifies that the activity was triggered by one or more Eiffel events. These events should be represented via __CAUSE__ links.  
SOURCE_CHANGE signifies that the activity was triggered as a consequence of a detected source change __not__ represented by Eiffel events.  
TIMER signifies that the activity was triggered by a timer.  
OTHER signifies any other triggering cause.

#### data.triggers.description
__Type:__ String  
__Required:__ No  
__Description:__ A description of the trigger.

### data.executionType
__Type:__ String  
__Required:__ No  
__Legal values:__ MANUAL, SEMI_AUTOMATED, AUTOMATED, OTHER  
__Description:__ The type of execution (often related to, but ultimately separate from, __data.triggers.type__).

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelActivityTriggeredEvent/simple.json)
* [Example containing custom data](../examples/events/EiffelActivityTriggeredEvent/simple-customdata.json)