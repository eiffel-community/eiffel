# EiffelArtifactCreatedEvent
The EiffelArtifactCreatedEvent declares that a software artifact has been created, what its coordinates are, what it contains and how it was created.

## Data Members
### data.gav
__Type:__ Object  
__Required:__ Yes  
__Description:__ The [GAV](https://maven.apache.org/guides/mini/guide-naming-conventions.html) of the created artifact.

#### data.gav.groupId
__Type:__ String  
__Required:__ Yes  
__Description:__ The groupId of the created artifact.

#### data.gav.artifactId
__Type:__ String  
__Required:__ Yes  
__Description:__ The artifactId of the created artifact.

#### data.gav.version
__Type:__ String  
__Required:__ Yes  
__Description:__ The version of the created artifact.

### data.fileInformation
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of the artifact file contents, following the standard established by [Apache Maven](https://maven.apache.org/pom.html).

#### data.fileInformation.classifier
__Type:__ String  
__Required:__ Yes  
__Description:__ The classifier of the file within the artifact. If none, an empty string shall be used.

#### data.fileInformation.extension
__Type:__ String  
__Required:__ Yes  
__Description:__ The extension of the file within the artifact. If none, an empty string shall be used.

### data.buildCommand
__Type:__ String  
__Required:__ No  
__Description:__ The command used to build the artifact within the identified environment. Used for reproducability purposes.

## Examples
* [Simple example](https://github.com/Ericsson/eiffel-examples/blob/master/events/EiffelArtifactCreatedEvent/simple.json)