# Eiffel
The Eiffel framework enables technology agnostic enterprise scale continuous integration and delivery with maintained scalability, flexibility and traceability. Eiffel is based on the concept of decentralized real time messaging, both to drive the continuous integration and delivery system and to document it.

This repository contains the Eiffel framework vocabulary, descriptions, guides and schemas along with links to relevant implementation repositories.

Eiffel is licensed under the [Apache License 2.0](./LICENSE).

__IMPORTANT NOTICE:__ The contents of this repository currectly reflect a __DRAFT__. The Eiffel framework has been used in production within Ericsson for several years to great effect; what is presented here is a revision and evolution of that framework - an evolution that is currently ongoing. In other words, anything in this repository should be regarded as tentative and subject to change. It is published here to allow early access and trial and to solicit early feedback.

## Contents
1. [Introduction](./introduction/introduction.md)
1. Eiffel Syntax and Usage
   1. Eiffel Event Design Guidelines
   1. Notes on Custom Events
   1. [Event Structure](./eiffel-syntax-and-usage/event-structure.md)
   1. [The Meta Object](./eiffel-syntax-and-usage/the-meta-object.md)
   1. [The Links Object](./eiffel-syntax-and-usage/the-links-object.md)
1. The Eiffel Vocabulary
   1. [EiffelActivityTriggeredEvent](./eiffel-vocabulary/EiffelActivityTriggeredEvent.md)
   1. [EiffelActivityCanceledEvent](./eiffel-vocabulary/EiffelActivityCanceledEvent.md)
   1. [EiffelActivityStartedEvent](./eiffel-vocabulary/EiffelActivityStartedEvent.md)
   1. [EiffelActivityFinishedEvent](./eiffel-vocabulary/EiffelActivityFinishedEvent.md)
   1. [EiffelArtifactCreatedEvent](./eiffel-vocabulary/EiffelArtifactCreatedEvent.md)
   1. [EiffelArtifactPublishedEvent](./eiffel-vocabulary/EiffelArtifactPublishedEvent.md)
   1. [EiffelConfidenceLevelModifiedEvent](./eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)
   1. EiffelDocumentationCreatedEvent
   1. EiffelEnvironmentDefinedEvent
   1. EiffelCompositionDefinedEvent
   1. EiffelSourceChangeCreatedEvent
   1. EiffelSourceChangeSubmittedEvent
   1. EiffelFlowContextDefinedEvent
   1. EiffelTestCaseStartedEvent
   1. EiffelTestCaseFinishedEvent
   1. EiffelTestSuiteStartedEvent
   1. EiffelTestSuiteFinishedEvent
   1. EiffelTestExecutionRecipeCollectionCreated
   1. EiffelAnnouncementEvent
   1. EiffelConfigurationChangedEvent
1. Usage Examples
   1. [Confidence Level Joining](./usage-examples/confidence-level-joining.md)
   1. [Delivery Interface](./usage-examples/delivery-interface.md)
1. Reference Data Sets
   1. [Default](./reference-data-sets/default.md)
1. Implementations
   1. [Event Persistence](./implementations/event-persistence.md)
   1. [Event Aggregation and Analysis](./implementations/event-aggregation-and-analysis.md)
   1. Activity Orchestration
   1. Event Transport and Routing
   1. [Event Dispatch](./implementations/event-dispatch.md)
   1. [Visualization](./implementations/visualization.md)
