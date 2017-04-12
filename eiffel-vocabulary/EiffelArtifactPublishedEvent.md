<!---
   Copyright 2017 Ericsson AB.
   For a full list of individual contributors, please see the commit history.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
--->

# EiffelArtifactPublishedEvent (ArtP)
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
ARTIFACTORY signifies an [Artifactory](https://www.jfrog.com/artifactory/)  
NEXUS signifies a [Nexus](http://www.sonatype.org/nexus/)  
PLAIN signifies a plain HTTP GET request.  
OTHER signifies other methods of retrieval. Note that using this type likely requires some foreknowledge on part of the reader in order to fetch the artifact.

#### data.locations.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the artifact can be retrieved.

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelArtifactPublishedEvent/simple.json)