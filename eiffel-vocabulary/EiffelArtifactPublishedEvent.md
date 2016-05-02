# EiffelArtifactPublishedEvent
The EiffelArtifactPublishedEvent declares that a software artifact (declared by [EiffelArtifactCreatedEvent](./EiffelArtifactCreatedEvent.md)) has been published and is consequently available for retrieval at one or more locations.

## Data Members
### data.locations
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ A list of locations at which the artifact may be retrieved.

#### data.locations.type
__Type:__ String  
__Required:__ Yes  
__Legal values:__ ARTIFACTORY, NEXUS, PLAIN, OTHER  
__Description:__ The type of location. May be used by (automated) readers to understand the method of retrieval, particularly with regards to authentication.

#### data.locations.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the artifact can be retrieved.
