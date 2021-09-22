<!---
   Copyright 2020-2021 Ericsson AB and others.
   For a full list of individual contributors, please see the commit history.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
--->

# Eiffel Glossary
This a non-exhaustive, alphabetical list of terms used in the [Eiffel vocabulary](../eiffel-vocabulary/) and its documentation.

 - [Terms Used in Event Definitions](#terms-used-in-event-definitions)
   - [Activity](#activity)
   - [Artifact](#artifact)
   - [Composition](#composition)
   - [Confidence Level](#confidence-level)
   - [Domain](#domain)
   - [Environment](#environment)
   - [Event](#event)
   - [Link](#link)
   - [Source Change](#source-change)
   - [Submit](#submit)

 - [Terms Used in Documentation](#terms-used-in-documentation)
   - [Pipeline](#pipeline)

## Terms Used in Event Definitions
These terms are either part of the event names in the Eiffel Vocabulary, or they are part of parameter names or values in the events. Users of Eiffel should be able to rely on these terms to be kept, unless a major change to event types are done.

### Activity
An _activity_ is any kind of action in a CI/CD system, normally triggered by an operation done in an SCM system or by a previous activity. The Eiffel protocol declares events related to activities to describe what is going on, what has finished, when did it happen and with what outcome.

Activities are hierarchical. Activities could be whole [pipelines](#pipeline), or sequential or parallel parts thereof. Such pipeline parts could for example be build activities or test activities.

An activity could also be an SCM operation such as a manual code review or automated source change check.

Some activity types have their own specific events, such as EiffelTestCase\*Events notifying test case executions, while others are more generic and can be notified using EiffelActivity\*Events.

#### Examples of events related to activities:
- [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)
- [EiffelActivityStartedEvent](../eiffel-vocabulary/EiffelActivityStartedEvent.md)
- [EiffelActivityFinishedEvent](../eiffel-vocabulary/EiffelActivityFinishedEvent.md)
- [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md)
- [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md)
- [EiffelTestCaseFinishedEvent](../eiffel-vocabulary/EiffelTestCaseFinishedEvent.md)

### Artifact
_Artifacts_ are items or software packages generated in a CI/CD [pipeline](#pipeline), for example a built binary or a Docker image. An artifact should be possible to identify using a purl (package URL). Artifacts often refer to a [composition](#composition) stating exactly what versions of different software pieces where put together to form the artifact.

An artifact is often the subject of a test executed or a delivery performed within a CI/CD pipeline. An artifact can also be software package generated with the sole purpose to be used in a specific test scenario. For example when product software is combined with test harnesses. Such artifacts are also defined by compositions to record what versions of test harness software were used.

#### Examples of events related to artifacts:
- [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)

### Composition
A _composition_ is an immutable grouping of specific versions of [artifacts](#artifact) and/or [source changes](#source-change). It is more or less the same as what is elsewhere sometimes referred to as a _baseline_, which can be explained as being a fixed reference point used for comparison. A composition is often defined with the purpose of enabling downstream artifacts to be generated. It gives full traceability on what software pieces that were used to generate the artifact, be it a product artifact, a test harness or some other kind of generated artifact.

#### Examples of events related to compositions:
- [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)

### Confidence Level
A _confidence level_ can be achieved for an [artifact](#artifact), a [composition](#composition), or a [source change](#source-change). It can be used to annotate that the artifact, composition or source change has been tested up to a certain level, that it has reached a certain level of maturity, or that it has passed a certain criteria. Examples of confidence levels could be "smokeTestsOk", "releasable" or "released".

A confidence level can group other (sub) confidence levels of lower abstractions. For example the confidence level "allTestsOk" could summarize sub confidence levels called "unitTestsOk, "scenarioTestsOk" and "deploymentTestsOk".

Confidence levels frequently figure in automated delivery interfaces within a tiered system context: lower level tiers issue an agreed confidence level signaling that a new version is ready for integration in a higher level tier.

#### Examples of events related to confidence levels:
- [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)

### Domain

An Eiffel _domain_ is an infrastructure topological concept, which may or may not correspond to an organization or product structure. A good example would be Java packages notation, ex. com.mycompany.product.component or mycompany.site.division. Domains can be used to implement Eiffel namespaces when different companies, business units, or similar exchange Eiffel events. An Eiffel event may include a member that specifies the event's domain association.

Also, keep in mind that all names are more or less prone to change. Particularly, it is recommended to avoid organizational names or site names, as organizations tend to be volatile and development is easily relocated. Relatively speaking, product and component names tend to be more stable and are therefore encouraged, while code names may be an option. You need to decide what is the most sensible option in your case.

### Environment
An Eiffel _environment_ defines the environment in which an [activity](#activity) is executed. Could be for example a host, node, service name/uri, a Docker image or some other kind of machine configuration definition.

#### Examples of events related to environments:
- [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)

### Event
An Eiffel _event_ is a broadcast notification telling any consumer about an event occurring in the CI/CD [pipeline](#pipeline). As opposed to a _message_, that is addressed to a certain receiver, an event is not aimed at a specific consumer. An event is also _descriptive_ rather than _prescriptive_, meaning that it does not expect a certain action to happen but it instead notifies on actions performed.

An event should not carry any data that is already provided by events sent earlier in the CI/CD pipeline. Instead those earlier events should be [linked](#link) from this event, making it possible to aggregate all relevant data connected to the CI/CD pipeline execution.

More about what an event is supposed to be can be read in the [event design guidelines](./event-design-guidelines.md).

### Link
A _link_ is a directed connection between two [events](#event). With linked events you will get a directed acyclic graph of actions performed in your CI/CD [pipeline](#pipeline). Links are also semantic, as each link has a type describing the relationship between the link source and its target. Having linked events enables generic data aggregations and visualizations to be implemented. Together with the timestamps provided in each event, the directed semantic links enable the possibility to create generic pipeline measurements and other analytics compilations.

More about links can be read in the [links object documentation](./the-links-object.md).

### Source Change
A _source change_ is the unit of a review. It results in a single commit when merged to the Git repository.

#### Examples of events related to source changes:
- [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)
- [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)

### Submit
A _submit_ is the action of merging a [source change](#source-change) to its intended target branch.

#### Examples of events related to submits:
- [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)

## Terms Used in Documentation
The terms below are not used in any events in the Eiffel protocol. They are added here to enable a homogenous and easy read of the protocol documentation. These terms are subject to change without notice if a better name is found or defined elsewhere. Their names should reflect the most commonly used terms elsewhere in the industry.

### Pipeline
A _pipeline_ is an ordered set of [activities](#activity) often triggered by a [source change](#source-change) being created or [submitted](#submit).
