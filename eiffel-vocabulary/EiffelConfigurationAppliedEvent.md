# EiffelConfigurationAppliedEvent
The EiffelConfigurationAppliedEvent signifies that the configuration of an item, typically an actor within the continuous integration and delivery pipeline, has changed.

The event itself does not declare what the change is, only that it has been applied to an item. To identify the actual configuration source, the dedicated __CONFIGURATION_SOURCE__ link type is used, as described in the documentation of [the links object](../eiffel-syntax-and-usage/the-links-object.md).

## Data Members
### data.items
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ The item or items to which configuration has been applied

#### data.item.type
__Type:__ String  
__Required:__ No  
__Description:__ The type of configured item.

#### data.item.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the configured item.

#### data.item.uri
__Type:__ String  
__Required:__ No  
__Description:__ The URI of the configured item.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelConfigurationAppliedEvent/simple.json)