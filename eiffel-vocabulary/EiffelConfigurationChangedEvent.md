# EiffelConfigurationChangedEvent
The EiffelConfigurationChangedEvent signifies that the configuration of an item, typically an actor within the continuous integration and delivery pipeline, has changed.

Similarly to [EiffelDocumentationCreatedEvent](EiffelDocumentationCreatedEvent.md), this event is intended for situations where configuration is not stored and treated as any other source (in which case [EiffelSourceChangeCreatedEvent](EiffelSourceChangeCreatedEvent.md) and [EiffelSourceChangeSubmittedEvent](EiffelSourceChangeSubmittedEvent.md) SHOULD be used instead of EiffelConfigurationChangedEvent).

## Data Members
### data.item
__Type:__ Object  
__Required:__ Yes  
__Description:__ The item the configuration of which has changed.

#### data.item.type
__Type:__ String  
__Required:__ No  
__Description:__ The type of reconfigured item.

#### data.item.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the reconfigured item.

#### data.item.uri
__Type:__ String  
__Required:__ No  
__Description:__ The URI of the reconfigured item.

### data.configuration
__Type:__ Object  
__Required:__ Yes  
__Description:__ The changed configuration.

#### data.configuration.change
__Type:__ String  
__Required:__ Yes  
__Legal values:__ CREATED, MODIFIED, DELETED
__Description:__ The type of change made to the configuration.

#### data.configuration.uri
__Type:__ String  
__Required:__ No  
__Description:__ The URI of the configuration (not to be confused with __data.item.uri__, which points at the configured item rather than the configuration).

#### data.configuration.dump
__Type:__ String  
__Required:__ No  
__Description:__ A dump of the configuration. In case of very large configurations it is not recommended to include them in the event itself, but rather to use __data.configuration.uri__ to reference them.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelConfigurationChangedEvent/simple.json)