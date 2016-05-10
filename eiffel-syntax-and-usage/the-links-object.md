# The Links Object
The __links__ object contains trace links to other Eiffel events. These trace links by definition always reference backwards in time – it is only possible to reference an event that has already occured. The value is always a UUID or array of UUIDs, corresponding to the __meta.id__ of the target(s), on String (or String array) format.

Every trace link type has a set of possible source event types, and a set of possible target event types.

## Links Members
### links.causes
__Type:__ String[]  
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ Any  
__Description:__ Identifies one or more causes of the event occurring. SHOULD not be used in conjunction with __links.context__: individual events providing __links.causes__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __links.causes__.  

### links.context
__Type:__ String  
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ [EiffelActivityQueuedEvent](../eiffel-vocabulary/EiffelActivityQueuedEvent.md), 
[EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Description:__ Identifies a the activity or test suite of which the event constitutes a part. SHOULD not be used in conjunction with __links.causes__, see above. Note that multiple layers may be modeled using __links.context__, e.g. an activity being part of another activity.

### links.flowContext
__Type:__ String  
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### links.activityExecution
__Type:__ String  
__Required in:__ [EiffelActivityDequeuedEvent](../eiffel-vocabulary/EiffelActivityDequeuedEvent), 
[EiffelActivityStartedEvent](../eiffel-vocabulary/EiffelActivityStartedEvent), 
[EiffelActivityFinishedEvent](../eiffel-vocabulary/EiffelActivityFinishedEvent)  
__Optional in:__ None  
__Legal targets:__ [EiffelActivityQueuedEvent](../eiffel-vocabulary/EiffelActivityQueuedEvent.md)  
__Description:__ Declares the activity execution the event relates to. In other words, [EiffelActivityQueuedEvent](../eiffel-vocabulary/EiffelActivityQueuedEvent.md) acts as a handle for the activity execution. This differs from __links.context__. In __links.activityExecution__ the source carries information pertaining to the target (i.e. the activity started, finished or was dequeued). In __links.context__, on the other hand, the source constitutes a subset of the target (e.g. this test case was executed as part of that activity or test suite).

### links.previousActivityExecution
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelActivityStartedEvent](../eiffel-vocabulary/EiffelActivityStartedEvent.md)  
__Legal targets:__ [EiffelActivityQueuedEvent](../eiffel-vocabulary/EiffelActivityQueuedEvent.md)  
__Description:__ Identifies the latest previous execution of the activity.

### links.previousVersions
__Type:__ String[]  
__Required in:__ None  
__Optional in:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), 
[EiffelDocumentationCreatedEvent](../eiffel-vocabulary/EiffelDocumentationCreatedEvent.md), 
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), 
[EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md), 
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), 
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), 
[EiffelDocumentationCreatedEvent](../eiffel-vocabulary/EiffelDocumentationCreatedEvent.md), 
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), 
[EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md), 
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), 
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Description:__ Identifies the latest previous version(s) of the engineering artifact the event represents, e.g. the previous version of the artifact, the previous version of the composition etc. The target event type SHALL be the same as the source event type. In most cases a single element array is to be expected: multiple elements are intended for representing merges.

### links.composition
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Description:__ Identifies the composition from which an artifact was built.

### links.environment
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), 
[EiffelArtifactTestCaseStartedEvent](../eiffel-vocabulary/EiffelArtifactTestCaseStartedEvent.md)  
__Legal targets:__ [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)  
__Description:__ Identifies the environment in which an event occurred, e.g. in which environment an artifact was built.

### links.artifact
__Type:__ String  
__Required in:__ [EiffelArtifactPublishedEvent](../eiffel-vocabulary/EiffelArtifactPublishedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Description:__ Identifies the artifact that was published.

### links.subjects
__Type:__ String[]  
__Required in:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md),
[EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelDocumentationCreatedEvent](../eiffel-vocabulary/EiffelDocumentationCreatedEvent.md),
[EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md),
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Description:__ Identifies the subject(s) of the confidence level.

### links.elements
__Type:__ String[]  
__Required in:__ None  
__Optional in:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md),
[EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md),
[EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelDocumentationCreatedEvent](../eiffel-vocabulary/EiffelDocumentationCreatedEvent.md)  
__Description:__ Identifies elements and or sub-compositions of the composition. The latter is particularly useful for documenting large and potentially decentralized compositions, and may be used to reduce the need to repeat large compositions in which only small parts are subject to frequent change.

### links.base
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)  
__Legal targets:__ [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Description:__ Identifies the base revision of the proposed change.

### links.change
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Legal targets:__ [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)  
__Description:__ Identifies the change that was submitted.

### links.testSuiteExecution
__Type:__ String  
__Required in:__ [EiffelTestSuiteFinishedEvent](../eiffel-vocabulary/EiffelTestSuiteFinishedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Description:__ Identifies the relevant test suite execution. In other words, [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md) acts as a handle for a particular test suite execution.

### links.testCaseExecution
__Type:__ String  
__Required in:__ [EiffelTestCaseFinishedEvent](../eiffel-vocabulary/EiffelTestCaseFinishedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md)  
__Description:__ Identifies the relevant test case execution. In other words, [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md) acts as a handle for a particular test case execution.

### links.iut
__Type:__ String  
__Required in:__ [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md)  
__Optional in:__ None  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md),
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Description:__ Identifies the Item Under Test.

### links.terc
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md)  
__Legal targets:__ [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md)  
__Description:__ Identifies the Test Execution Recipe Collection dictating the execution of the test case.

### links.modifiedAnnouncement
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelAnnouncementEvent](../eiffel-vocabulary/EiffelAnnouncementEvent.md)  
__Legal targets:__ [EiffelAnnouncementEvent](../eiffel-vocabulary/EiffelAnnouncementEvent.md),
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Description:__ Identifies an announcement of which this event represents an update or modification, if any. Example usage is to declare the end to a previously announced situation.

### links.subConfidenceLevels
__Type:__ String  
__Required in:__ None  
__Optional in:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)  
__Legal targets:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md),
[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Description:__ Used in events summarizing multiple confidence levels. Example use case: the confidence level "allTestsOk" summarizes the confidence levels "unitTestsOk, "scenarioTestsOk" and "deploymentTestsOk", and consequently links to them using this field. This is intended for purely descriptive, rather than prescriptive, use.

