<!---
   Copyright 2017-2021 Ericsson AB and others.
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

# EiffelIssueVerifiedEvent (IV)
The EiffelIssueVerifiedEvent declares that an issue, typically a requirement, has been verified by some means. It is different from [EiffelTestCaseFinishedEvent](./EiffelTestCaseFinishedEvent.md) in that multiple test case executions may serve as the basis for a single verification or, conversely, multiple issues may be verified based on a single test case execution.

EiffelIssueVerifiedEvent has no data members, instead relying on its required link types. While "SUCCESSFUL_ISSUE", "FAILED_ISSUE", and "INCONCLUSIVE_ISSUE" are all marked as not required, at least one link of at least one of these types MUST be present in an EiffelIssueVerifiedEvent.

## Data Members

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### SUCCESSFUL_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies an issue that has been successfully verified.

### FAILED_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies an issue that has failed verification.

### INCONCLUSIVE_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies an issue for which this verification was inconclusive.

### IUT
__Required:__ Yes  
__Optional in:__ None  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the Item Under Test; in other words, the entity for which the issue has been verified.

### VERIFICATION_BASIS
__Required:__ No  
__Legal targets:__ [EiffelTestCaseFinishedEvent](../eiffel-vocabulary/EiffelTestCaseFinishedEvent.md), [EiffelTestSuiteFinishedEvent](../eiffel-vocabulary/EiffelTestSuiteFinishedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Used to declare the basis on which the verification statement(s) of this event have been issued.

### ENVIRONMENT
__Required:__ No  
__Legal targets:__ [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the environment in which the issue was verified.

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
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

## Meta
See [Meta property description](./EiffelMetaProperty.md)

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 4.1.0     | [edition-lyon](../../../tree/edition-lyon)             | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 4.0.0     | [edition-agen](../../../tree/edition-agen)             | Improved information integrity protection | (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 3.0.0     | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelIssueVerifiedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 2.0.0     | [0706840](../../../blob/070684053ceb1da5fb42d9f0ef21df816961d6bc/eiffel-vocabulary/EiffelIssueVerifiedEvent.md) | Replaced data.issues with links         |
| 1.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelIssueVerifiedEvent/simple.json)
