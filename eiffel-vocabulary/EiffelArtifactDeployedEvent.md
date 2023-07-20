<!---
   This file was generated from ../definitions/EiffelArtifactDeployedEvent/0.1.0.yml.
   See that file for a copyright notice.
--->

# EiffelArtifactDeployedEvent (ArtD)
> :warning: This event type is currently at version 0.1.0 and is therefore experimental. Until it has reached version 1.0.0 it may undergo any number of backwards incompatible changes. It might also be deprecated and never reach 1.0.0.

The EiffelArtifactDeployedEvent states that a software artifact had been deployed into a specified environment or that the configuration of the artifact has been changed. The exact meaning of an artifact deployment is implementation-defined. Progressive deployments like e.g. canaries can be described with an EiffelArtifactDeployedEvent every time the deployment advances or a single EiffelArtifactDeployedEvent once the artifact has been fully deployed.

## Data Members

### data.description
__Type:__ String  
__Required:__ No  
__Description:__ Any human readable information information about this deployment.

### data.uri
__Type:__ String  
__Format:__ URI  
__Required:__ No  
__Description:__ A URI identifying the deployment description.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### ARTIFACT
__Required:__ Yes  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the artifact that has been deployed. This link type targets an experimental event and may be removed in a future version of this event (see [Versioning](../eiffel-syntax-and-usage/versioning.md) for details).

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.

### CONFIGURATION
__Required:__ No  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the configuration used to deploy the artifact identified with the ARTIFACT link, if the configuration isn't included in the artifact itself. This configuration could be a deployment script, a runbook specification, a helm chart or some other description of how the artifact is started or upgraded in the target environment. This link type targets an experimental event and may be removed in a future version of this event (see [Versioning](../eiffel-syntax-and-usage/versioning.md) for details).

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### ENVIRONMENT
__Required:__ Yes  
__Legal targets:__ [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the environment into which this artifact was deployed.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 0.1.0 | [edition-orizaba](../../../tree/edition-orizaba) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelArtifactDeployedEvent/simple.json)
