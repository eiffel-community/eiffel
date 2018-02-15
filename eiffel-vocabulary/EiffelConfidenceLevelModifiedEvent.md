<!---
   Copyright 2017-2018 Ericsson AB.
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

# EiffelConfidenceLevelModifiedEvent (CLM)
The EiffelConfidenceLevelModifiedEvent declares that an entity has achieved (or failed to achieve) a certain level of confidence, or in a broader sense to annotate it as being applicable or relevant to a certain case (e.g. fit for release to a certain customer segment or having passed certain criteria. This is particularly useful for promoting various engineering artifacts, such as product revisions, through the continuous integration and delivery pipeline.

Confidence levels may operate at high or low levels of abstraction - ranging from "smokeTestsOk" to "releasable" or "released" - and they may group other confidence levels of lower abstraction levels. They may also be general or very niched, e.g. "releasable" or "reseabableToCustomerX". Confidence levels frequently figure in automated delivery interfaces within a tiered system context: lower level tiers issue an agreed confidence level signaling that a new version is ready for integration in a higher level tier.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the confidence level. It is recommended for confidence level names to conform with camelCase formatting, in line with the format of key names of the Eiffel protocol as a whole.

### data.value
__Type:__ String  
__Required:__ Yes  
__Legal values:__ SUCCESS, FAILURE, INCONCLUSIVE  
__Description:__ The value of the confidence level.  
SUCCESS signifies that the confidence level has been successfully achieved.  
FAILURE signifies that the confidence level could not be achieved.
INCONCLUSIVE signifies that achievement of the confidence level could not be determined.

### data.issuer
__Type:__ Object  
__Required:__ No  
__Description:__ The individual or entity issuing the confidence level.

#### data.issuer.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the issuer.

#### data.issuer.email
__Type:__ String  
__Required:__ No  
__Description:__ The e-mail address of the issuer.

#### data.issuer.id
__Type:__ String  
__Required:__ No  
__Description:__ Any identity, alias or handle of the issuer, such as a corporate id or username.

#### data.issuer.group
__Type:__ String  
__Required:__ No  
__Description:__ Any group, such as a development team, committee or test group, to which the issuer belongs.

## Links
### SUBJECT
__Required:__ Yes  
__Optional in:__ None  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md),
[EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md),
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a subject of the confidence level; in other words, what the confidence level applies to.

### SUB_CONFIDENCE_LEVEL
__Required:__ No  
__Legal targets:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)
__Multiple allowed:__ Yes  
__Description:__ Used in events summarizing multiple confidence levels. Example use case: the confidence level "allTestsOk" summarizes the confidence levels "unitTestsOk, "scenarioTestsOk" and "deploymentTestsOk", and consequently links to them via __SUB_CONFIDENCE_LEVEL__. This is intended for purely descriptive, rather than prescriptive, use.

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.  

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md),
[EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelConfidenceLevelModifiedEvent/simple.json)
