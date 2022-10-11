# Event Categories

The Eiffel protocol specifies each event on its own. For convenience reasons the
protocol also provides a description on how to group them together in
categories. Use the following categories to group events together for ease of
talking about them or in reasoning. To make pictures with Eiffel events
consistent throughout the documentation we have assigned each category a color
picked from the
[Unicode's full list of geometric emojis](https://unicode.org/emoji/charts/full-emoji-list.html#geometric).

| Category     | Color |
|:-------------|:-----:|
| Activity     |  🔵   |
| Artifact     |  🔴   |
| Definition   |  🟣   |
| Notification |  🟠   |
| Source       |  🟢   |
| Test         |  🟡   |
| Verdict      |  🟤   |

The events and their categories.

| Category     | Name                                                                                                                       | Abbreviation | Color |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------|:------------:|:-----:|
| Activity     | [EiffelActivityCanceledEvent](../eiffel-vocabulary/EiffelActivityCanceledEvent.md)                                         |     ActC     |  🔵   |
| Activity     | [EiffelActivityFinishedEvent](../eiffel-vocabulary/EiffelActivityFinishedEvent.md)                                         |     ActF     |  🔵   |
| Activity     | [EiffelActivityStartedEvent](../eiffel-vocabulary/EiffelActivityStartedEvent.md)                                           |     ActS     |  🔵   |
| Activity     | [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md)                                       |     ActT     |  🔵   |
| Artifact     | [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)                                           |     ArtC     |  🔴   |
| Artifact     | [EiffelArtifactPublishedEvent](../eiffel-vocabulary/EiffelArtifactPublishedEvent.md)                                       |     ArtP     |  🔴   |
| Artifact     | [EiffelArtifactReusedEvent](../eiffel-vocabulary/EiffelArtifactReusedEvent.md)                                             |     ArtR     |  🔴   |
| Definition   | [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)                                     |     FCD      |  🟣   |
| Definition   | [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)                                     |      CD      |  🟣   |
| Definition   | [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)                                     |      ED      |  🟣   |
| Definition   | [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)                                                 |      ID      |  🟣   |
| Notification | [EiffelAnnouncementPublishedEvent](../eiffel-vocabulary/EiffelAnnouncementPublishedEvent.md)                               |     AnnP     |  🟠   |
| Source       | [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)                                   |     SCC      |  🟢   |
| Source       | [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)                               |     SCS      |  🟢   |
| Test         | [EiffelTestCaseCanceledEvent](../eiffel-vocabulary/EiffelTestCaseCanceledEvent.md)                                         |     TCC      |  🟡   |
| Test         | [EiffelTestCaseFinishedEvent](../eiffel-vocabulary/EiffelTestCaseFinishedEvent.md)                                         |     TCF      |  🟡   |
| Test         | [EiffelTestCaseStartedEvent](../eiffel-vocabulary/EiffelTestCaseStartedEvent.md)                                           |     TSS      |  🟡   |
| Test         | [EiffelTestCaseTriggeredEvent](../eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md)                                       |     TCT      |  🟡   |
| Test         | [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md) |    TERCC     |  🟡   |
| Test         | [EiffelTestSuiteFinishedEvent](../eiffel-vocabulary/EiffelTestSuiteFinishedEvent.md)                                       |     TSF      |  🟡   |
| Test         | [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)                                         |     TSS      |  🟡   |
| Verdict      | [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)                           |     CLM      |  🟤   |
| Verdict      | [EiffelIssueVerifiedEvent](../eiffel-vocabulary/EiffelIssueVerifiedEvent.md)                                               |      IV      |  🟤   |
