# EiffelDocumentationCreatedEvent
The EiffelDocumentationCreatedEvent signifies that a documentation item (or a new version of a documentation item) has been created. This is intended for situations where documentation is not stored and treated as any other source (in which case [EiffelSourceChangeCreatedEvent](EiffelSourceChangeCreatedEvent.md) and [EiffelSourceChangeSubmittedEvent](EiffelSourceChangeSubmittedEvent.md) SHOULD be used instead of EiffelDocumentationCreatedEvent).

While the mandatory properties of the event are technology agnostic, optional properties can be used to add further detail supporting specific documentation systems, e.g. enabling automated documentation assembly.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the documentation item.

### data.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the documentation item can be retrieved.

### data.ditaTopicId
__Type:__ String  
__Required:__ No  
__Description:__ Assuming a [DITA](http://dita.xml.org) documentation system, this property can be used to define the __id__ of the documentation __topic__. This can then be used for automated assembly of a DITA __book__.

### data.ditaRev
__Type:__ String  
__Required:__ No  
__Description:__ Assuming a [DITA](http://dita.xml.org) documentation system, this property can be used to define __rev__ attribute of the __topic__ represented by this documentation item.

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelDocumentationCreatedEvent/simple.json)