<!---
   Copyright 2017 Ericsson AB.
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

# Confidence Level Joining Example
This example illustrates how [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md) can be used to capture and summarize a larger body of lower level results, such as test suite verdicts, effectively _joining_ multiple flows in the continuous integration and delivery system.

A JSON array of all events used in this example can be found [here](../examples/flows/confidence-level-joining/events.json).

## Introduction
A common use case in continuous integration and delivery systems is to join many separate (and disparate) tests into a larger entity, providing a stamp of approval to the item under test. In Eiffel, such stamps are provided by [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md). This not only serves the purpose of raising the level of abstraction, thereby facilitating analysis and release decisions, but also provides a pragmatic extension point of the production pipeline: an external listener (e.g. a product looking to integrate the item under test) is not interested in tracking individual test case results, particularly as they may well change over time or even from execution to execution, but simply wants to know "Is this artifact good enough for me to pick up?".

## Event Graph
![alt text](./confidence-level-joining.svg "Event Graph of Confidence Level Joining Example")

## Event-by-Event Explanation
### ArtC1
The [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md) is central in this example. It declares that a new artifact has been created, and (largely via links) documents how and from what it was built. At the time of this event we still know very little about the artifact: it has unique coordinates (its purl identity), but where to fetch it or whether it is any good remains to be seen.

### CDef1
An [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md) detailing a composition of items (such as source code revisions and other artifacts), from which the artifact declared by __ArtC1__ was built. The elements of the composition, the reason for defining the composition et cetera are excluded in this example.

### EDef1
An [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md) describing the environment in which the artifact declared by __ArtC1__ was built.

### ArtP1
The [EiffelArtifactPublishedEvent](../eiffel-vocabulary/EiffelArtifactPublishedEvent.md) declaring that the created artifact now has been published, and consequently may be fetched. Since __ArtC1__ itself declares the purl identity, the artifact _may_ be fetched using only that information (assuming a binary repository supporting this, such as Artifactory), but it is still recommended practice to explicitly declare when and where the artifact can be retrieved, in order to avoid outages or timing issues.

### ActT1, ActT2, ActS1, ActS2, ActF1, ActF2
A set of [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), [EiffelActivityStartedEvent](../eiffel-vocabulary/EiffelActivityStartedEvent.md), [EiffelActivityFinishedEvent](../eiffel-vocabulary/EiffelActivityFinishedEvent.md) reporting on the lifecycle of two independent activity executions being caused by the publication of the artifact. Note that the EiffelActivityStartedEvents and EiffelActivityFinishedEvents are "dead ends" in the graph: in this example, nothing occurs as a direct cause of the activity starting or finishing (although such a setup is, of course, entirely possible) and the work being done within the activity refers directly to the EiffelActivityTriggeredEvent as its context. This shows how, in one sense, this type of lifecycle events is superfluous: for the core functionality of this example it is perfectly possible to cut them out and let the EiffelTestCaseStartedEvents refer directly to __ArtP1__ as their cause. Activity events do provide important contextual information, however, as they allow monitoring of e.g. system performance, bottlenecks, queue times and execution durations. They also serve the purpose of clustering work; in this example, __ActT1__ and __ActT2__ may represent activities executed at wildly different times, at different locations and by different organizations.

### TCT1, TCT2, TCT3, TCT4
[EiffelTestCaseTriggeredEvents](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md) declaring that, as part of their respective activities, test cases have been triggered for execution. In this example only a very small number of test cases are executed - in reality, these events tend to be very numerous. Note that the cause of the execution can be traced to __ArtC1__ via __CONTEXT__ and __CAUSE__ links. This is not enough to unambiguously identify the item under test, however: it is entirely conceivable that the immediate cause for executing the test is completely independent from the item under test. Consequently the __IUT__  link is used to reference __ArtC1__ directly.

### TCS1, TCS2, TCS3, TCS4
[EiffelTestCaseStartedEvents](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md) declaring that the previously triggered test case executions have commenced.

### TCF1, TCF2, TCF3, TCF4
[EiffelTestCaseFinishedEvents](../eiffel-vocabulary/EiffelTestCaseFinishedEvent.md) reporting the verdict of their respective test case executions.

### CLM1
The [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md) that summarizes all of the test case executions under a single headline. Note that the algorithm for determining this confidence level may be simple or relatively complex, but an important point of the event is that this algorithm is evaluated close to those tests, affording separation of concerns for users (human or automated) who simply want to know whether the relevant tests worked, whichever those tests happened to be at that point in time. This way the nitty gritty details are abstracted away. It doesn't end there, however: while not included in this example, __CLM1__ may in turn be but a building block of subsequent, even higher level EiffelConfidenceLevelModifiedEvents.
