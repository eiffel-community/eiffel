<!---
   This file was generated from ../definitions/EiffelEnvironmentDefinedEvent/3.3.0.yml.
   See that file for a copyright notice.
--->

# EiffelEnvironmentDefinedEvent (ED)

The EiffelEnvironmentDefinedEvent declares an environment which may be referenced from other events in order to secure traceability to the conditions under which an artifact was created or a test was executed. Depending on the technology domain, the nature of an environment varies greatly however: it may be a virtual image, a complete mechatronic system of millions of independent parts, or anything in between. Consequently, a concise yet complete and generic syntax for describing any environment is futile.

From Eiffel's point of view, however, the prioritized concern is not _description_ of the environment, but rather unambiguous _identification_ of it. Consequently, the EiffelEnvironmentDefinedEvent syntax offers several alternatives to be selected from depending on the use case at hand: an environment may be described using __data.image__, __data.host__ or __data.uri__, or a __RUNTIME_ENVIRONMENT__ link to another event that provides a more comprehensive description. Unless a link of the latter kind is used exactly one of these properties SHOULD be included in any one event. In certain situations where an actual description of the environment is deemed redundant or its nature is implicit, the event MAY be used without any of these properties or a RUNTIME_ENVIRONMENT link; it should be noted, however, that _explicit_ practices are always encouraged over _implicit_ ones.

## Data Members

### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the environment.

### data.version
__Type:__ String  
__Required:__ No  
__Description:__ The version of the environment, if any. This is in a sense redundant, as relationships between environments can be tracked via the __PREVIOUS_VERSION__ link type, but can be used for improved clarity and semantics.

### data.image
__Type:__ String  
__Required:__ No  
__Description:__ A string identifying e.g. a [Docker](https://www.docker.com/) image that defines this environment. Use of this member is discouraged. Prefer using the less ambiguous RUNTIME_ENVIRONMENT link type.

### data.host
__Type:__ Object  
__Required:__ No  
__Description:__ An object identifying a host. This object is included for pragmatic reasons, as this method of environment identification is often used in practice. It is discouraged, however, as it is highly unreliable both in terms of consistency and traceability. Consistency because consecutive executions on the same host may produce different results, as there are no inherent guarantees that it will stay the same over time. Traceability because when analyzing the historical record you want a static description of the environment _as it was at the time of execution_, not a pointer to a dynamic entity which may or may not have changed since then (and may or may not have changed again the next time you inspect it).

#### data.host.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The hostname.

#### data.host.user
__Type:__ String  
__Required:__ Yes  
__Description:__ The user name on the host.

### data.uri
__Type:__ String  
__Required:__ No  
__Description:__ A URI identifying the environment description. This is the catch-all method of environment descriptions. Eiffel does not concern itself with the format or nature of the description, but merely points to its location.

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

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the environment.

### RUNTIME_ENVIRONMENT
__Required:__ No  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a description of a runtime environment within which an activity has taken place. The target event could e.g. identify a [Docker](https://www.docker.com/) image, a JVM distribution archive, or a composition of operating system packages that were installed on the host system. This link type has the same purpose as the `data.image` member but allows richer and less ambiguous descriptions.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.3.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.2.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Added RUNTIME_ENVIRONMENT link type. |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [URI example](../examples/events/EiffelEnvironmentDefinedEvent/uri.json)
* [Host example](../examples/events/EiffelEnvironmentDefinedEvent/host.json)
* [Image example](../examples/events/EiffelEnvironmentDefinedEvent/image.json)
* [RUNTIME_ENVIRONMENT link example](../examples/events/EiffelEnvironmentDefinedEvent/runtime-env-link.json)
