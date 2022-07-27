# Event Categories

The Eiffel protocol specifies each event on its own. For convenience reasons the
protocol specifies them together in categories. Use the following categories to
group events together for ease of talking about them or in reasoning. To make
pictures with Eiffel events consistent throughout the documentation we have
assigned each category a color picked from the
[Unicodes full list of geometric emoji](https://unicode.org/emoji/charts/full-emoji-list.html#geometric)

| Category     | Color |
|:-------------|:-----:|
| Activity     |  🔵   |
| Artifact     |  🔴   |
| Baseline     |  🟠   |
| Environment  |  🟣   |
| Issue        |  ⚪   |
| Notification |  ⚫   |
| Source       |  🟢   |
| Test         |  🟡   |
| Verdict      |  🟤   |

The events and their categories.

| Category     | Name                                                                                                                                                                           | Abbreviation | Color |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------:|:-----:|
| Activity     | [EiffelActivityCanceledEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelActivityCanceledEvent.md)                                         |     ActC     |  🔵   |
| Activity     | [EiffelActivityFinishedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelActivityFinishedEvent.md)                                         |     ActF     |  🔵   |
| Activity     | [EiffelActivityStartedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelActivityStartedEvent.md)                                           |     ActS     |  🔵   |
| Activity     | [EiffelActivityTriggeredEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelActivityTriggeredEvent.md)                                       |     ActT     |  🔵   |
| Artifact     | [EiffelArtifactCreatedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelArtifactCreatedEvent.md)                                           |     ArtC     |  🔴   |
| Artifact     | [EiffelArtifactPublishedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelArtifactPublishedEvent.md)                                       |     ArtP     |  🔴   |
| Artifact     | [EiffelArtifactReusedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelArtifactReusedEvent.md)                                             |     ArtR     |  🔴   |
| Baseline     | [EiffelFlowContextDefinedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)                                     |     FCD      |  🟠   |
| Baseline     | [EiffelCompositionDefinedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelCompositionDefinedEvent.md)                                     |      CD      |  🟠   |
| Environment  | [EiffelEnvironmentDefinedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)                                     |      ED      |  🟣   |
| Issue        | [EiffelIssueVerifiedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelIssueVerifiedEvent.md)                                               |      IV      |  ⚪   |
| Issue        | [EiffelIssueDefinedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelIssueDefinedEvent.md)                                                 |     IssD     |  ⚪   |
| Notification | [EiffelAnnouncementPublishedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelAnnouncementPublishedEvent.md)                               |     AnnP     |  ⚫   |
| Source       | [EiffelSourceChangeCreatedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)                                   |     SCC      |  🟢   |
| Source       | [EiffelSourceChangeSubmittedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)                               |     SCS      |  🟢   |
| Test         | [EiffelTestCaseCanceledEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelTestCaseCanceledEvent.md)                                         |     TCC      |  🟡   |
| Test         | [EiffelTestCaseFinishedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelTestCaseFinishedEvent.md)                                         |     TCF      |  🟡   |
| Test         | [EiffelTestCaseStartedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelTestCaseStartedEvent.md)                                           |     TSS      |  🟡   |
| Test         | [EiffelTestCaseTriggeredEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelTestCaseTriggeredEvent.md)                                       |     TCT      |  🟡   |
| Test         | [EiffelTestExecutionRecipeCollectionCreatedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md) |    TERCC     |  🟡   |
| Test         | [EiffelTestSuiteFinishedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelTestSuiteFinishedEvent.md)                                       |     TSF      |  🟡   |
| Test         | [EiffelTestSuiteStartedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)                                         |     TSS      |  🟡   |
| Verdict      | [EiffelConfidenceLevelModifiedEvent](https://github.com/eiffel-community/eiffel/blob/master/eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)                           |     CLM      |  🟤   |
