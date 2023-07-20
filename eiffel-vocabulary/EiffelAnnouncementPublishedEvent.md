<!---
   This file was generated from ../definitions/EiffelAnnouncementPublishedEvent/3.2.0.yml.
   See that file for a copyright notice.
--->

# EiffelAnnouncementPublishedEvent (AnnP)

The EiffelAnnouncementPublishedEvent represents an announcement, technically regarding any topic but typically used to communicate any incidents or status updates regarding the continuous integration and delivery pipeline. This information can then be favorably displayed in visualization and dashboarding applications.

## Data Members

### data.heading
__Type:__ String  
__Required:__ Yes  
__Description:__ The heading of the announcement.

### data.body
__Type:__ String  
__Required:__ Yes  
__Description:__ The body of the announcement.

### data.uri
__Type:__ String  
__Required:__ No  
__Description:__ A URI where further information can be obtained, if applicable.

### data.severity
__Type:__ String  
__Required:__ Yes  
__Legal values:__ MINOR, MAJOR, CRITICAL, BLOCKER, CLOSED, CANCELED  
__Description:__ The severity of the announcement. The CLOSED and CANCELED values SHOULD only be used when following up a previous announcement, i.e. in conjunction with a __MODIFIED_ANNOUNCEMENT__ link.

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

### MODIFIED_ANNOUNCEMENT
__Required:__ No  
__Legal targets:__ [EiffelAnnouncementPublishedEvent](../eiffel-vocabulary/EiffelAnnouncementPublishedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies an announcement of which this event represents an update or modification, if any. Example usage is to declare the end to a previously announced situation.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelAnnouncementPublishedEvent/simple.json)
