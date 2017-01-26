# EiffelCompositionDefinedEvent (CD)
The EiffelCompositionDefinedEvent declares a composition of items (artifacts, sources and other compositions) has been defined, typically with the purpose of enabling further downstream artifacts to be generated.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the composition.

### data.version
__Type:__ String  
__Required:__ No  
__Description:__ The version of the composition, if any. This is in a sense redundant, as relationships between compositions can be tracked via the __PREVIOUS_VERSION__ link type, but can be used for improved clarity and semantics.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelCompositionDefinedEvent/simple.json)