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

# The Links Object
The __links__ object is an array of trace links to other Eiffel events. These trace links by definition always reference backwards in time – it is only possible to reference an event that has already occured. Each trace link is a tuple consisting of a type and a UUID corresponding to the __meta.id__ of the target event, on String format.

Some link types allow multiple trace links, whereas others only allow one.

Example syntax of a simple __links__ object:

    "links": [
      {"type": "CAUSE", "target": "8f3e0f94-5d11-46e7-ae02-91efa15d2329"},
      {"type": "COMPOSITION", "target": "43ee71d2-6d91-496a-b9cf-d121ff1d1bcf"}
    ]

## Legal Link Types
### CAUSE
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.  

### CONTEXT
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), 
[EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which the event constitutes a part. SHOULD not be used in conjunction with __CAUSE__, see above. Note that multiple layers may be modeled using __CONTEXT__, e.g. an activity being part of another activity.

### FLOW_CONTEXT
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### ACTIVITY_EXECUTION
__Required in:__ [EiffelActivityCanceledEvent](../eiffel-vocabulary/EiffelActivityCanceledEvent.md), 
[EiffelActivityStartedEvent](../eiffel-vocabulary/EiffelActivityStartedEvent.md), 
[EiffelActivityFinishedEvent](../eiffel-vocabulary/EiffelActivityFinishedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Declares the activity execution the event relates to. In other words, [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md) acts as a handle for the activity execution. This differs from __CONTEXT__. In __ACTIVITY_EXECUTION__ the source carries information pertaining to the target (i.e. the activity started, finished or was canceled). In __CONTEXT__, on the other hand, the source constitutes a subset of the target (e.g. this test case was executed as part of that activity or test suite).

### PREVIOUS_ACTIVITY_EXECUTION
__Required in:__ None  
__Optional in:__ [EiffelActivityStartedEvent](../eiffel-vocabulary/EiffelActivityStartedEvent.md)  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the latest previous execution of the activity.

### PREVIOUS_VERSION
__Required in:__ None  
__Optional in:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), 
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), 
[EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md), 
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), 
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), 
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), 
[EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md), 
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), 
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the engineering artifact the event represents, e.g. the previous version of the artifact, the previous version of the composition etc. The target event type SHALL be the same as the source event type.

### COMPOSITION
__Required in:__ [EiffelArtifactReusedEvent](../eiffel-vocabulary/EiffelArtifactReusedEvent.md)  
__Optional in:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the composition from which an artifact declared by [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md) was built, or the composition for which an already existing artifact is declared reused by [EiffelArtifactReusedEvent](../eiffel-vocabulary/EiffelArtifactReusedEvent.md).

### ENVIRONMENT
__Required in:__ None  
__Optional in:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), 
[EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md), 
[EiffelIssueVerifiedEvent](../eiffel-vocabulary/EiffelIssueVerifiedEvent.md)  
__Legal targets:__ [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the environment in which an event occurred, e.g. in which environment an artifact was built or an issue was verified.

### ARTIFACT
__Required in:__ [EiffelArtifactPublishedEvent](../eiffel-vocabulary/EiffelArtifactPublishedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the artifact that was published.

### SUBJECT
__Required in:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md),
[EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md),
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a subject of the confidence level.

### ELEMENT
__Required in:__ None  
__Optional in:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md),
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md),
[EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an element and/or sub-composition of the composition. The latter is particularly useful for documenting large and potentially decentralized compositions, and may be used to reduce the need to repeat large compositions in which only small parts are subject to frequent change.

### BASE
__Required in:__ None  
__Optional in:__ [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)  
__Legal targets:__ [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the base revision of the proposed change.

### CHANGE
__Required in:__ None  
__Optional in:__ [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Legal targets:__ [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the change that was submitted.

### TEST_SUITE_EXECUTION
__Required in:__ [EiffelTestSuiteFinishedEvent](../eiffel-vocabulary/EiffelTestSuiteFinishedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the relevant test suite execution. In other words, [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md) acts as a handle for a particular test suite execution.

### TEST_CASE_EXECUTION
__Required in:__ [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md), [EiffelTestCaseFinishedEvent](../eiffel-vocabulary/EiffelTestCaseFinishedEvent.md), [EiffelTestCaseCanceledEvent](../eiffel-vocabulary/EiffelTestCaseCanceledEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the relevant test case execution. In other words, [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md) acts as a handle for a particular test case execution. This differs from __CONTEXT__. In __TEST_CASE_EXECUTION__ the source carries information pertaining to the target (i.e. the test case execution started, finished or was canceled). In __CONTEXT__, on the other hand, the source constitutes a subset of the target (e.g. this test case was executed as part of that activity or test suite).

### IUT
__Required in:__ [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md), 
[EiffelIssueVerifiedEvent](../eiffel-vocabulary/EiffelIssueVerifiedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the Item Under Test: what is about to be tested and/or has been verified to address an issue, respectively.

### TERC
__Required in:__ None  
__Optional in:__ [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Legal targets:__ [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ When declared in an [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md), this link signifies that the test suite groups all test case executions resulting from the [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md).

### MODIFIED_ANNOUNCEMENT
__Required in:__ None  
__Optional in:__ [EiffelAnnouncementPublishedEvent](../eiffel-vocabulary/EiffelAnnouncementPublishedEvent.md)  
__Legal targets:__ [EiffelAnnouncementPublishedEvent](../eiffel-vocabulary/EiffelAnnouncementPublishedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies an announcement of which this event represents an update or modification, if any. Example usage is to declare the end to a previously announced situation.

### SUB_CONFIDENCE_LEVEL
__Required in:__ None  
__Optional in:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)  
__Legal targets:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Used in events summarizing multiple confidence levels. Example use case: the confidence level "allTestsOk" summarizes the confidence levels "unitTestsOk, "scenarioTestsOk" and "deploymentTestsOk", and consequently links to them via __SUB_CONFIDENCE_LEVEL__. This is intended for purely descriptive, rather than prescriptive, use.

### REUSED_ARTIFACT
__Required in:__ [EiffelArtifactReusedEvent](../eiffel-vocabulary/EiffelArtifactReusedEvent.md)    
__Optional in:__ None  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ This link identifies the [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md) that is reused; in other words, the artifact that is not rebuilt for a given composition.

### VERIFICATION_BASIS
__Required in:__ None  
__Optional in:__ [EiffelIssueVerifiedEvent](../eiffel-vocabulary/EiffelIssueVerifiedEvent.md)  
__Legal targets:__ [EiffelTestCaseFinishedEvent](../eiffel-vocabulary/EiffelTestCaseFinishedEvent.md), [EiffelTestSuiteFinishedEvent](../eiffel-vocabulary/EiffelTestSuiteFinishedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Used to declare the basis on which the verification statement(s) of [EiffelIssueVerifiedEvent](../eiffel-vocabulary/EiffelIssueVerifiedEvent.md) have been issued.
