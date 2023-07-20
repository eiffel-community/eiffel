<!---
   This file was generated from ../definitions/EiffelIssueDefinedEvent/3.2.0.yml.
   See that file for a copyright notice.
--->

# EiffelIssueDefinedEvent (ID)

The EiffelIssueDefinedEvent declares that an issue has been created in some external issue management software. ID is semantically similar to [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md) and [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md).

## Data Members

### data.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ BUG, IMPROVEMENT, FEATURE, WORK_ITEM, REQUIREMENT, OTHER  
__Description:__ The type of issue.

### data.tracker
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the issue tracker. This can unfortunately not be
standardized, and is therefore context sensitive: though some trackers and ALM
tools are more popular than others, an exhaustive enumeration is impossible,
particularly when considering company specific internal solutions. Consequently
one should not rely on the name as the primary method of retrieval, but rather
__data.uri__. __data.tracker__ together with __data.id__
is still useful for analysis and traceability, however, as long as it can be
correctly interpreted.

### data.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The identity of the issue. This is tracker dependent - most
trackers have their own issue naming schemes.

### data.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ A URI that links to a document describing the issue in depth.

### data.title
__Type:__ String  
__Required:__ No  
__Description:__ A one-line title or summary of the issue. This exists mostly
for human consumption, as "Implement widget X" is much more meaningful to a
human when viewing a graph of Eiffel events than "1302". This is not meant
to be a detailed description, as such information should be accessible by
following __data.uri__.

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
__Multiple allowed:__ No  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.0.0 | [edition-agen](../../../tree/edition-agen) | Initial version |
## Examples

* [Simple example](../examples/events/EiffelIssueDefinedEvent/simple.json)
