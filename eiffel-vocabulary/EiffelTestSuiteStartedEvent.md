<!---
   This file was generated from ../definitions/EiffelTestSuiteStartedEvent/3.4.0.yml.
   See that file for a copyright notice.
--->

# EiffelTestSuiteStartedEvent (TSS)

The EiffelTestSuiteStartedEvent declares that the execution of a test suite has started. This can either be declared stand-alone or as part of an activity or other test suite, using either a __CAUSE__ or a __CONTEXT__ link type, respectively.

In Eiffel, a test suite is nothing more or less than a collection of test case executions (see [EiffelTestCaseStartedEvent](./EiffelTestCaseStartedEvent.md)) and/or other test suite executions. The executed test suite may be an ad-hoc transient grouping of test cases that were executed at a particular time or place or for a particular purpose or a persistent entity tracked in a test management system - Eiffel makes no distinction or assumptions either way.

## Data Members

### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the test suite. Uniqueness is not required or checked, but is useful.

### data.categories
__Type:__ String[]  
__Required:__ No  
__Description:__ The category or categories of the test suite. This can be used to group multiple similar test suites for analysis and visualization purposes. Example usage is to categorize test suites required before release as "Pre-release tests".

### data.types
__Type:__ String[]  
__Required:__ No  
__Legal values:__ ACCESSIBILITY, BACKUP_RECOVERY, COMPATIBILITY, CONVERSION, DISASTER_RECOVERY, FUNCTIONAL, INSTALLABILITY, INTEROPERABILITY, LOCALIZATION, MAINTAINABILITY, PERFORMANCE, PORTABILITY, PROCEDURE, RELIABILITY, SECURITY, STABILITY, USABILITY  
__Description:__ The type or types of testing performed by the test suite, as [defined by ISO 29119](http://www.softwaretestingstandard.org).

### data.liveLogs
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of live log files available during execution. These shall not be presumed to be stored persistently; in other words, once the test suite has finished there is no guarantee that these links are valid. Persistently stored logs shall be (re-)declared by [EiffelTestSuiteFinishedEvent](./EiffelTestSuiteFinishedEvent.md).

#### data.liveLogs.mediaType
__Type:__ String  
__Required:__ No  
__Description:__ The [media type](https://en.wikipedia.org/wiki/Media_type) of the URI's payload. Can be used to differentiate between various representations of the same log, e.g. text/html for human consumption and text/plain or application/json for the machine-readable form.

#### data.liveLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.liveLogs.tags
__Type:__ String[]  
__Required:__ No  
__Description:__ Arbitrary tags and keywords that describe this log.

#### data.liveLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

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

### ORIGINAL_TRIGGER
__Required:__ No  
__Legal targets:__ [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Used when the current test suite execution is a new attempt at completing a previous test suite execution, typically because the previous one failed. Although this activity may have been manually triggered and thus lacks a cause that can be described with Eiffel, this link can be used to convey the second-order cause.

### PRECURSOR
__Required:__ No  
__Legal targets:__ [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Used to declare temporal relationships between [activities](../eiffel-syntax-and-usage/glossary.md#activity) in a [pipeline](../eiffel-syntax-and-usage/glossary.md#pipeline), i.e. what other activity/activities preceded this activity. This link type applies primarily to non event-triggered activities. For more information on the usage of this link type please see [Activity Linking](../eiffel-syntax-and-usage/activity-linking.md).

### TERC
__Required:__ No  
__Legal targets:__ [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ This link signifies that the test suite represented by this event groups all test case executions resulting from the [EiffelTestExecutionRecipeCollectionCreatedEvent](../eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md).

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.4.0 | [edition-orizaba](../../../tree/edition-orizaba) | Add ORIGINAL_TRIGGER link (see [Issue 246](https://github.com/eiffel-community/eiffel/issues/246)). |
| 3.3.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.2.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add `data.liveLogs.{mediaType,tags}`. |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelTestSuiteStartedEvent/simple.json)
