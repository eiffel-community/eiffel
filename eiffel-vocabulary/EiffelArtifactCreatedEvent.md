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

### data.requiresImplementation
__Type:__ String  
__Required:__ No  
__Legal values:__ NONE, ANY, EXACTLY_ONE, AT_LEAST_ONE
__Description:__ Defines whether this artifact requires an implementing artifact. This is typically used for interfaces requiring some backend implementation, although the interface does not presume to define _which_ implementation. Implicitly interpreted as "ANY" if undefined.  
NONE signifies that there SHALL no implementations of this artifact. In other words, a composition containing another artifact identifying it in __data.implements__ would be illegal.
ANY signifies that there may or may not be implementations of this artifact.
EXACTLY_ONE signifies that a legal composition must contain one and only one implementation of this artifact.
AT_LEAST_ONE signifies that a legal composition must contain one or more implementations of this artifact.

### data.implements
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of [GAVs](https://maven.apache.org/guides/mini/guide-naming-conventions.html) this artifact implements. The typical use case of this is to identify interfaces implemented by this artifact.

#### data.implements.groupId
__Type:__ String  
__Required:__ Yes  
__Description:__ The groupId of the implemented artifact.

#### data.implements.artifactId
__Type:__ String  
__Required:__ Yes  
__Description:__ The artifactId of the implemented artifact.

#### data.implements.version
__Type:__ String  
__Required:__ Yes  
__Description:__ The version of the implemented artifact. Note that [version range notation](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN402) is supported.

### data.dependsOn
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of [GAVs](https://maven.apache.org/guides/mini/guide-naming-conventions.html) this artifact depends on.

#### data.dependsOn.groupId
__Type:__ String  
__Required:__ Yes  
__Description:__ The groupId of the dependency.

#### data.dependsOn.artifactId
__Type:__ String  
__Required:__ Yes  
__Description:__ The artifactId of the dependency.

#### data.dependsOn.version
__Type:__ String  
__Required:__ Yes  
__Description:__ The version of the dependency. Note that [version range notation](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN402) is supported.

## Examples
* [Simple example](../examples/events/EiffelArtifactCreatedEvent/simple.json)
* [Interface example](../examples/events/EiffelArtifactCreatedEvent/interface.json)
* [Backend example](../examples/events/EiffelArtifactCreatedEvent/backend.json)
* [Dependent example](../examples/events/EiffelArtifactCreatedEvent/dependent.json)