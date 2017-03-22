<!---
   Copyright 2017 Ericsson AB.

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

# EiffelActivityCanceledEvent (ActC)
The EiffelActivityCanceledEvent signals that a previously triggered activity execution has been canceled _before it has started_. This is typically used in queuing situations where a queued execution is dequeued. It is recommended that __CAUSE__ links be used to indicate the reason.

## Data Members
### data.reason
__Type:__ String  
__Required:__ No  
__Description:__ Any human readable information as to the reason for dequeueing.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelActivityCanceledEvent/simple.json)