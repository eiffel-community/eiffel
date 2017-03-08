# Event Structure
Eiffel events are represented as JSON objects. These JSON objects contain three required members: __meta__, __data__ and __links__.

## meta
__Type:__ Object  
__Required:__ Yes  
__Description:__ This object contains fields common to all event types: meta-data describing the event itself. It is described in detail [here](./the-meta-object.md).

## data
__Type:__ Object  
__Required:__ Yes  
__Description:__ This object contains all fields specific to the event type - the payload of the event - including trace links to non-Eiffel entities. It is described in detail per event type. Some common data objects referenced by several Eiffel events are defined [here](./common-data-objects.md).

## links
__Type:__ Object  
__Required:__ Yes  
__Description:__ This object contains all trace links to other Eiffel events. It is described in detail [here](./the-links-object.md).
