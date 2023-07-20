<!---
   This file was generated from ../definitions/EiffelActivityStartedEvent/4.3.0.yml.
   See that file for a copyright notice.
--->

# EiffelActivityStartedEvent (ActS)

The EiffelActivityStartedEvent declares that a previously triggered activity (declared by [EiffelActivityTriggeredEvent](./EiffelActivityTriggeredEvent.md)) has started.

## Data Members

### data.executionUri
__Type:__ String  
__Required:__ No  
__Description:__ Any URI at which further information about the execution may be found; a typical use case is to link a CI server job execution page.

### data.liveLogs
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of live log files available during execution. These shall not be presumed to be stored persistently; in other words, once the activity has finished there is no guarantee that these links are valid. Persistently stored logs shall be (re-)declared by [EiffelActivityFinishedEvent](./EiffelActivityFinishedEvent.md).

#### data.liveLogs.mediaType
__Type:__ String  
__Required:__ No  
__Description:__ The [media type](https://en.wikipedia.org/wiki/Media_type) of the URI's payload. Can be used to differentiate between various representations of the same log, e.g. text/html for human consumption and text/plain or application/json for the machine-readable form.

#### data.liveLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.liveLogs.tags
__Type:__ String[]  
__Required:__ No  
__Description:__ Arbitrary tags and keywords that describe this log.

#### data.liveLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### ACTIVITY_EXECUTION
__Required:__ Yes  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Declares the activity execution that was started. In other words, [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md) acts as a handle for the activity execution. This differs from __CONTEXT__. In __ACTIVITY_EXECUTION__ the source carries information pertaining to the target (i.e. the activity started, finished or was canceled). In __CONTEXT__, on the other hand, the source constitutes a subset of the target (e.g. this test case was executed as part of that activity or test suite).

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

### PREVIOUS_ACTIVITY_EXECUTION
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the latest previous execution of the activity.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 4.3.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 4.2.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 4.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add `data.liveLogs.{mediaType,tags}`. |
| 4.0.0 | [edition-agen-1](../../../tree/edition-agen-1) | Bug fix in schema file (see [Issue 205](https://github.com/eiffel-community/eiffel/issues/205)) |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)) |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelActivityStartedEvent/simple.json)
