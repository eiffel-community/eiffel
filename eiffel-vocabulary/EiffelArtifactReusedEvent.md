<!---
   This file was generated from ../definitions/EiffelArtifactReusedEvent/3.2.0.yml.
   See that file for a copyright notice.
--->

# EiffelArtifactReusedEvent (ArtR)

The EiffelArtifactReusedEvent declares that an identified [EiffelArtifactCreatedEvent](./EiffelArtifactCreatedEvent.md) has been _reused_ for an identified [EiffelCompositionDefinedEvent](./EiffelCompositionDefinedEvent.md). This means that it is logically equivalent to an artifact that would have been built from that composition, and can be used for build avoidance (see the [Build Avoidance Usage Example](../usage-examples/build-avoidance.md) for more information).

The event has no data members, but solely relies on its two required link types __REUSED_ARTIFACT__ and __COMPOSITION__ (see below).

## Data Members

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.

### COMPOSITION
__Required:__ Yes  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the composition for which an already existing artifact (identified by __REUSED_ARTIFACT__) is declared reused.

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

### REUSED_ARTIFACT
__Required:__ Yes  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ This link identifies the [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md) that is reused for the composition identified by __COMPOSITION__; in other words, the artifact that is not rebuilt for a that composition.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelArtifactReusedEvent/simple.json)
