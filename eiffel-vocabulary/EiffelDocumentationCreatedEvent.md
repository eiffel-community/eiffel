# EiffelDocumentationCreatedEvent
The EiffelDocumentationCreatedEvent signifies that a documentation item (or a new version of a documentation item) has been created. The event itself does not identify the location of the documentation, but rather relies on [EiffelSourceChangeSubmittedEvent](./[EiffelSourceChangeSubmittedEvent].md), similarly to e.g. [EiffelConfigurationAppliedEvent](./[EiffelConfigurationAppliedEvent].md) using the __DOCUMENTATION_SOURCE__ link type. While it is recommended practice to use source code management systems for storing documentation, this information model is still applicable as long as the document can be accessed via a URI.

While the mandatory properties of the event are technology agnostic, optional properties can be used to add further detail supporting specific documentation systems, e.g. enabling automated documentation assembly.

## Data Members
### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the documentation item.

### data.path
__Type:__ String  
__Required:__ No  
__Description:__ A relative path identifying the file(s) of the documentation item within an SCM system, if applicable. To exemplify, if the documentation is available in a Git repository (as identified via the linked [EiffelSourceChangeSubmittedEvent](./[EiffelSourceChangeSubmittedEvent].md)), this property can be used to point to the exact location (e.g. "/documentation/myFile.txt").

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