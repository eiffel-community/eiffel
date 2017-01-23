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

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelAnnouncementPublishedEvent/simple.json)