<!---
   This file was generated from ../definitions/EiffelTestCaseTriggeredEvent/3.5.0.yml.
   See that file for a copyright notice.
--->

# EiffelTestCaseTriggeredEvent (TCT)

The EiffelTestCaseTriggeredEvent declares that the execution of a test case has been triggered, but not yet started. This can either be declared stand-alone or as part of an activity or test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively.

This event is used to communicate intent, and thereby serves a similar purpose to that of [EiffelActivityTriggeredEvent](./EiffelActivityTriggeredEvent.md). A triggered test case execution is expected to either be started (represented by [EiffelTestCaseStartedEvent](./EiffelTestCaseStartedEvent.md)) or canceled (represented by [EiffelTestCaseCanceledEvent](./EiffelTestCaseCanceledEvent.md)). Consequently, any delay between triggering and execution can be assumed to imply queuing time (e.g. waiting for available test resources) and monitored as such.

## Data Members

### data.testCase
__Type:__ Object  
__Required:__ Yes  
__Description:__ Identification of the test case to be executed.

#### data.testCase.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case tracker - typically a test management system.

#### data.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the test case to be executed.

#### data.testCase.version
__Type:__ String  
__Required:__ No  
__Description:__ The unique version of the identified test case to be executed. Where this property is not used it is assumed that test cases are not version controlled.

#### data.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved. To the extent that multiple versions of the same test case co-exist, this property SHALL identify the exact version to be executed.

### data.recipeId
__Type:__ String  
__Required:__ No  
__Description:__ If triggering this test case execution was the result of an Execution Recipe, as defined by an [EiffelTestExecutionRecipeCollectionCreatedEvent](./EiffelTestExecutionRecipeCollectionCreatedEvent.md), this UUID SHALL match the relevant __data.batches.recipes.id__ in that event.

### data.triggers
__Type:__ Object[]  
__Required:__ No  
__Description:__ The circumstances triggering the test case execution.

#### data.triggers.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ MANUAL, EIFFEL_EVENT, SOURCE_CHANGE, TIMER, OTHER  
__Description:__ The type of trigger.
MANUAL signifies that the test case execution was manually triggered.  
EIFFEL_EVENT signifies that the test case execution was triggered by one or more Eiffel events. These events should be represented via __CAUSE__ links.  
SOURCE_CHANGE signifies that the test case execution was triggered as a consequence of a detected source change __not__ represented by Eiffel events.  
TIMER signifies that the test case execution was triggered by a timer.  
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

### data.parameters
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of parameters to be passed to the test case execution.

#### data.parameters.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the parameter.

#### data.parameters.value
__Type:__ String  
__Required:__ Yes  
__Description:__ The value of the parameter.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### IUT
__Required:__ Yes  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), [EiffelArtifactDeployedEvent](../eiffel-vocabulary/EiffelArtifactDeployedEvent.md), [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the Item Under Test; in other words, the entity that is about to be tested.

### ORIGINAL_TRIGGER
__Required:__ No  
__Legal targets:__ [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Used when the current test case execution is a new attempt at completing a previous test case execution, typically because the previous one failed. Although this activity may have been manually triggered and thus lacks a cause that can be described with Eiffel, this link can be used to convey the second-order cause.

### PRECURSOR
__Required:__ No  
__Legal targets:__ [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Used to declare temporal relationships between [activities](../eiffel-syntax-and-usage/glossary.md#activity) in a [pipeline](../eiffel-syntax-and-usage/glossary.md#pipeline), i.e. what other activity/activities preceded this activity. This link type applies primarily to non event-triggered activities. For more information on the usage of this link type please see [Activity Linking](../eiffel-syntax-and-usage/activity-linking.md).

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.5.0 | [edition-orizaba](../../../tree/edition-orizaba) | Add ORIGINAL_TRIGGER link (see [Issue 246](https://github.com/eiffel-community/eiffel/issues/246)). |
| 3.4.0 | [edition-orizaba](../../../tree/edition-orizaba) | Add artifact deployed event as legal IUT target (see [Issue 239](https://github.com/eiffel-community/eiffel/issues/239)). |
| 3.3.0 | [edition-orizaba](../../../tree/edition-orizaba) | Add SCS and SCC as legal target for IUT in TCT (see [Issue 317](https://github.com/eiffel-community/eiffel/issues/317)). |
| 3.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelTestCaseTriggeredEvent/simple.json)
* [Simple example using pre-3.0.0 meta.security object](../examples/events/EiffelTestCaseTriggeredEvent/simple-2.0.0.json)
