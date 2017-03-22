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

# EiffelFlowContextDefined (FCD)
The EiffelFlowContextDefined describes the context of other events, answering questions such as "Which project is change part of?" or "Which track does artifact belong to?". In this way it offers a method of classifying and structuring one's continuous integration and delivery system and thereby facilitaring traceability and searchability. 

The nature of the described context can vary. The event consequently offers a high degree of flexibility in its description, and none of its member fields are mandatory. Instead they can picked and mixed to fit the situation.

## Data Members
### data.product
__Type:__ String  
__Required:__ No  
__Description:__ A product context which other events can relate to (e.g. "This activity is part of the Product X continuous integration system.").

### data.project
__Type:__ String  
__Required:__ No  
__Description:__ A project context which other events can relate to (e.g. "This test is part of the Killer Feature project.").

### data.program
__Type:__ String  
__Required:__ No  
__Description:__ A program context which other events can relate to (e.g. "This source change was made for the Zero Bugs program.").

### data.track
__Type:__ String  
__Required:__ No  
__Description:__ A track context which other events can relate to (e.g. "This feature was implemented in the Customer X Adaptations track.").

### data.version
__Type:__ String  
__Required:__ No  
__Description:__ A version context which other events can relate to. This member SHOULD be used in tandem with one of the other optional members - a version by itself is not very informative.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelFlowContextDefinedEvent/simple.json)