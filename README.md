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
   1. User Examples
1. The Eiffel Vocabulary
   1. [EiffelActivityQueuedEvent](./eiffel-vocabulary/EiffelActivityQueuedEvent.md)
   1. [EiffelActivityDequeuedEvent](./eiffel-vocabulary/EiffelActivityDequeuedEvent.md)
   1. EiffelActivityStartedEvent
   1. EiffelActivityFinished
   1. EiffelArtifactCreatedEvent
   1. EiffelConfidenceLevelModifiedEvent
   1. EiffelArtifactPublishedEvent
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
1. Implementations
   1. Event Persistence
   1. Event Aggregation and Analysis
   1. Activity Orchestration
   1. Event Transport and Routing
   1. Event Dispatch
   1. Visualization
