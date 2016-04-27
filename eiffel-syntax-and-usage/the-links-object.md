# The Links Object
The __links__ object contains trace links to other Eiffel events. These trace links by definition always reference backwards in time – it is only possible to reference an event that has already occured. The value is always a UUID or array of UUIDs, corresponding to the __meta.id__ of the target(s), on String (or String array) format.

Every trace link type has a set of possible source event types, and a set of possible target event types.

## Links Members
### links.causes
__Type:__ String[]  
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ Any  
__Description:__ Identifies one or more causes of the event occurring. SHOULD not be used in conjunction with __links.context__: individual events providing __links.causes__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __links.causes__.  

### links.context
__Type:__ String  
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ [EiffelActivityQueuedEvent](../eiffel-vocabulary/EiffelActivityQueuedEvent.md), [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Description:__ Identifies a the activity or test suite of which the event constitutes a part. SHOULD not be used in conjunction with __links.causes__, see above. Note that multiple layers may be modeled using __links.context__, e.g. an activity being part of another activity.

### links.flowContext
__Type:__ String  
__Required in:__ None  
__Optional in:__ Any  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.


### More links to be added...