<!---
   This file was generated from ../definitions/EiffelCompositionDefinedEvent/3.3.0.yml.
   See that file for a copyright notice.
--->

# EiffelCompositionDefinedEvent (CD)

The EiffelCompositionDefinedEvent declares a composition of items (artifacts, sources and other compositions) has been defined, typically with the purpose of enabling further downstream artifacts to be generated.

## Data Members

### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the composition.

### data.version
__Type:__ String  
__Required:__ No  
__Description:__ The version of the composition, if any. This is in a sense redundant, as relationships between compositions can be tracked via the __PREVIOUS_VERSION__ link type, but can be used for improved clarity and semantics.

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

### ELEMENT
__Required:__ No  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an element and/or sub-composition of this composition. The latter is particularly useful for documenting large and potentially decentralized compositions, and may be used to reduce the need to repeat large compositions in which only small parts are subject to frequent change.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the composition.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.3.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.2.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.1.0 | [edition-paris](../../../tree/edition-paris) | Added SCC as valid target for ELEMENT links (see [Issue 218](https://github.com/eiffel-community/eiffel/issues/218)) |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelCompositionDefinedEvent/simple.json)
