<!---
   Copyright 2017-2018 Ericsson AB.
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

# EiffelTestExecutionRecipeCollectionCreatedEvent (TERCC)
The EiffelTestExecutionRecipeCollectionCreatedEvent declares that a collection of test execution recipes has been created. In order to clarify what that means, several concepts need to be explained.

Just as Eiffel is an opinionated protocol, EiffelTestExecutionRecipeCollectionCreatedEvent is an opinionated event, and to a certain extent that opinion goes against the grain of traditional test management. This event assumes that activity configurations and test scope definitions are two separate things. To exemplify, when one's CI server triggers the Acceptance Test activity in the pipeline, there is nothing in that activity that says which tests to execute where or with what parameters: that is a separate concern. Instead, it will query a test selection service for that information. This information is encapsulated by the EiffelTestExecutionRecipeCollectionCreatedEvent, which contains all the information needed to configure and execute the tests.

How the test selection service generates the recipe collection is, from the point of view of the Eiffel protocol, irrelevant. It may very well be from a statically defined list of test cases, or from an elaborate test selection algorithm weighing together a host of factors to determine the optimal set of test cases to execute at any particular time, or a combination of the two.

The __data__ object consists of two main parts. __data.selectionStrategy__ identifies the strategy used to select the test cases and generate the recipe collection, while __data.batches__ or __data.batchesUri__ contain or reference, respectively, the recipes. The recipes are grouped in batches, which are used to control the order of execution of test cases. Every batch has a priority to let the test executor order them in sequence, but within each batch no assumptions are made as to the execution order the test cases. This way the recipe collection can either allow the executor a high degree of freedom in scheduling the test executions, and/or prescribe the exact sequential order in which they must be executed. Each event SHALL include one and only one of __data.batches__ and __data.batchesUri__.

Finally, each recipe (__data.batches.recipes__) consists of two parts: the test case to execute, and the constraints of that execution. The EiffelTestExecutionRecipeCollectionCreatedEvent does not control the syntax of these constraints, as the nature of such constraints are highly dependent on technology domain and test execution framework. That being said, there are three questions that typically need to be answered: what is the item under test, in what kind of environment is it to be tested, and what are the test parameters? Note the distinction between test case and test execution: it is perfectly legal for a single test case to appear multiple times within the same EiffelTestExecutionRecipeCollectionCreatedEvent, but (presumably) with different constraints.

## Data Members
### data.selectionStrategy
__Type:__ Object  
__Required:__ Yes  
__Description:__ The strategy used to select the test cases and generate the recipe collection.

#### data.selectionStrategy.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the selection strategy that generated the test execution recipe collection.

#### data.selectionStrategy.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the selection strategy that generated the test execution recipe collection.

#### data.selectionStrategy.uri
__Type:__ String  
__Required:__ No  
__Description:__ The URI at which the the selection strategy that generated the test execution recipe collection can be retrieved.

### data.batchesUri
__Type:__ String  
__Required:__ No  
__Description:__ A URI at which at which the array of test execution batches can be fetched. The format of the document at this URI SHALL be on the format prescribed by __data.batches__ (i.e. ``` [ { "name": "Batch 1", ...}, {...}] ```). Each event SHALL include one and only one of __data.batches__ and __data.batchesUri__.

### data.batches
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of batches of recipes. Each event SHALL include one and only one of __data.batches__ and __data.batchesUri__. In the interest of keeping message sizes small, it is recommended to use __data.batches__ only for limited numbers of test cases (on the order of ten executions). For larger numbers of executions, __data.batchesUri__ SHOULD be used instead.

#### data.batches.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the recipe batch.

#### data.batches.priority
__Type:__ Integer  
__Required:__ Yes  
__Description:__ The execution priority of the batch, as compared to other batches in the collection. A lower value SHALL be interpreted as a higher priority.

#### data.batches.recipes
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ The collection of test execution recipes within the batch.

##### data.batches.recipes.id
__Type:__ String  
__Required:__ Yes  
__Description:__ A UUID identifying the unique execution. Note that this is different from the id of a test case, in two ways. First, a test case is a (presumably) persistnent entity, whereas an execution is transient in nature. Second, a test case may be executed any number of times in any given recipe collection.

##### data.batches.recipes.testCase
__Type:__ Object  
__Required:__ Yes  
__Description:__ The test case to be executed in this execution recipe.

###### data.batches.recipes.testCase.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the test case tracker - typically a test management system.

###### data.batches.recipes.testCase.id
__Type:__ String  
__Required:__ Yes  
__Description:__ The unique identity of the test case.

###### data.batches.recipes.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved.

##### data.batches.recipes.constraints
__Type:__ Object[]  
__Required:__ No  
__Description:__ Any constraints of the execution. The nature of such constraints is highly dependent on technology domain and test execution framework. Consequently, there are no pre-defined or required constraints. Instead, this property is a list of key-value pairs on the same format as [data.customData](../customization/custom-data.md). That being said, there are three questions that typically need to be answered: what is the item under test, in what kind of environment is it to be tested, and what are the test parameters?

###### data.batches.recipes.constraints.key
__Type:__ String  
__Required:__ Yes  
__Description:__ The key name of constraint.

###### data.batches.recipes.constraints.value
__Type:__ Any  
__Required:__ Yes  
__Description:__ The value of the constraint.

#### data.batches.dependencies
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of test case execution dependencies. Ideally, test cases are atomic and can be executed in isolation. In cases where a test case assumes that another test case has been executed previously in the same environment, however, this property can be used to specify that. It serves as an instruction to the test executor to place two executions subsequent to one another in the same environment.

##### data.batches.dependencies.dependency
__Type:__ String  
__Required:__ Yes  
__Description:__ The UUID of the dependency execution (__data.batches.recipes.id__), i.e. the execution that shall be performed prior to that of the dependent.

##### data.batches.dependencies.dependent
__Type:__ String  
__Required:__ Yes  
__Description:__ The UUID of the dependent execution (__data.batches.recipes.id__), i.e. the execution that shall be performed only after that of the dependency.

## Links
### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.  

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md),
[EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

## Meta Members
### meta.id
__Type:__ String  
__Format:__ [UUID](http://tools.ietf.org/html/rfc4122)  
__Required:__ Yes  
__Description:__ The unique identity of the event, generated at event creation.

### meta.type
__Type:__ String  
__Format:__ An event type name  
__Required:__ Yes  
__Description:__ The type of event. This field is required by the recipient of the event, as each event type has a specific meaning and a specific set of members in the __data__ and __links__ objects.

### meta.version
__Type:__ String  
__Format:__ [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html)  
__Required:__ Yes  
__Description:__ The version of the event type. This field is required by the recipient of the event to interpret the contents. Please see [Versioning](../eiffel-syntax-and-usage/versioning.md) for more information.

### meta.time
__Type:__ Integer  
__Format:__ Milliseconds since epoch.  
__Required:__ Yes  
__Description:__ The event creation timestamp.

### meta.tags
__Type:__ String[]  
__Format:__ Free text  
__Required:__ No  
__Description:__ Any tags or keywords associated with the events, for searchability purposes.

### meta.source
__Type:__ Object  
__Format:__  
__Required:__ No  
__Description:__ A description of the source of the event. This object is primarily for traceability purposes, and while optional, some form of identification of the source is __HIGHLY RECOMMENDED__. It offers multiple methods of identifying the source of the event, techniques which may be select from based on the technology domain and needs in any particular use case.

#### meta.source.domainId
__Type:__ String  
__Format:__ Free text  
__Required:__ No  
__Description:__ Identifies the domain that produced an event. A domain is an infrastructure topological concept, which may or may not corresponds to an organization or product structures. A good example would be Java packages notation, ex. com.mycompany.product.component or mycompany.site.division. Also, keep in mind that all names are more or less prone to change. Particularly, it is recommended to avoid organizational names or site names, as organizations tend to be volatile and development is easily relocated. Relatively speaking, product and component names tend to be more stable and are therefore encouraged, while code names may be an option. You need to decide what is the most sensible option in your case.

#### meta.source.host
__Type:__ String  
__Format:__ Hostname  
__Required:__ No  
__Description:__ The hostname of the event sender.

#### meta.source.name
__Type:__ String  
__Format:__ Free text  
__Required:__ No  
__Description:__ The name of the event sender.

#### meta.source.serializer
__Type:__ Object  
__Format:__   
__Required:__ No  
__Description:__ The [GAV](https://maven.apache.org/guides/mini/guide-naming-conventions.html) coordinates of the serializer software used to construct the event.

##### meta.source.serializer.groupId
__Type:__ String  
__Format:__ groupId  
__Required:__ Yes  
__Description:__ The groupId of the serializer software.

##### meta.source.serializer.artifactId
__Type:__ String  
__Format:__ artifactId  
__Required:__ Yes  
__Description:__ The artifactId of the serializer software.

##### meta.source.serializer.version
__Type:__ String  
__Format:__ version  
__Required:__ Yes  
__Description:__ The version of the serializer software.

#### meta.source.uri
__Type:__ String  
__Format:__ URI  
__Required:__ No  
__Description:__ The URI of, related to or describing the event sender.

### meta.security
__Type:__ Object  
__Format:__  
__Required:__ No  
__Description:__ An optional object for enclosing security related information, particularly supporting data integrity. See [Security](../eiffel-syntax-and-usage/security.md) for further information.

#### meta.security.sdm
__Type:__ Object  
__Format:__  
__Required:__ No  
__Description:__ An optional object for properties supporting the [Strong Distribution Model](http://www.cryptnet.net/fdp/crypto/strong_distro.html). Note that this only addressed the _integrity_ of the Eiffel event, not its _confidentiality_ or _availability_.

##### meta.security.sdm.authorIdentity
__Type:__ String  
__Format:__  
__Required:__ Yes  
__Description:__ The identity of the author of the event. This property is intended to enable the recipient to look up the appropriate public key for decrypting the digest and thereby verifying author identity and data integrity. The format of the author identity varies depending on the key infrastructure solution used. Note that this requires the presence of a Trusted Authority (TA) which the recipient can query for the correct public key. The identity and location of the TA must never be included in the event itself, as this would compromise the security of the solution.

##### meta.security.sdm.encryptedDigest
__Type:__ String  
__Format:__  
__Required:__ Yes  
__Description:__ The encrypted digest. The cryptographic hash function and the decryption algorithm to use, similarly to the Trusted Authority (TA), must be known to the recipient. Note that the digest of the entire event is affected by the value of this property. For this reason the input to the hash function SHALL be the entire event unaltered in all parts except for this property, which SHALL be replaced by an empty string.

## Version History
| Version   | Introduced in                                          | Changes                                 |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 2.0.0     | Current version.                                       | Changed syntax of data.batches.recipes.constraints from an uncontrolled object to a list of key-value pairs to comply with design guidelines. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Example using data.batches](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batches.json)
* [Example using data.batches (1.0.0 syntax)](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batches-1.0.0.json)
* [Example using data.batchesUri](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batchesUri.json)
