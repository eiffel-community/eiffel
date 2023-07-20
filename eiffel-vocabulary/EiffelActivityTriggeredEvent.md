<!---
   This file was generated from ../definitions/EiffelActivityTriggeredEvent/4.3.0.yml.
   See that file for a copyright notice.
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
__Description:__ Identifies the [activity](../eiffel-syntax-and-usage/glossary.md#activity) or test suite of which this event constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### ORIGINAL_TRIGGER
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Used when the current activity is a new attempt at completing a previous activity, typically because the previous one failed. Although this activity may have been manually triggered and thus lacks a cause that can be described with Eiffel, this link can be used to convey the second-order cause.

### PRECURSOR
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Used to declare temporal relationships between [activities](../eiffel-syntax-and-usage/glossary.md#activity) in a [pipeline](../eiffel-syntax-and-usage/glossary.md#pipeline), i.e. what other activity/activities preceded this activity. This link type applies primarily to non event-triggered activities. For more information on the usage of this link type please see [Activity Linking](../eiffel-syntax-and-usage/activity-linking.md).

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 4.3.0 | [edition-orizaba](../../../tree/edition-orizaba) | Add ORIGINAL_TRIGGER link (see [Issue 246](https://github.com/eiffel-community/eiffel/issues/246)). |
| 4.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 4.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 4.0.0 | [edition-agen-1](../../../tree/edition-agen-1) | Bug fix in schema file (see [Issue 205](https://github.com/eiffel-community/eiffel/issues/205)) |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelActivityTriggeredEvent/simple.json)
* [Example containing custom data](../examples/events/EiffelActivityTriggeredEvent/simple-customdata.json)
