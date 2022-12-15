<!---
   This file was generated from ../definitions/EiffelTestExecutionRecipeCollectionCreatedEvent/4.3.0.yml.
   See that file for a copyright notice.
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
__Description:__ A UUID identifying the unique execution. Note that this is different from the id of a test case, in two ways. First, a test case is a (presumably) persistent entity, whereas an execution is transient in nature. Second, a test case may be executed any number of times in any given recipe collection.

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
__Description:__ The unique identity of the test case to be executed.

###### data.batches.recipes.testCase.version
__Type:__ String  
__Required:__ No  
__Description:__ The unique version of the identified test case to be executed. Where this property is not used it is assumed that test cases are not version controlled.

###### data.batches.recipes.testCase.uri
__Type:__ String  
__Required:__ No  
__Description:__ A location where a description of the test case can be retrieved. To the extent that multiple versions of the same test case co-exist, this property SHALL identify the exact version to be executed.

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

##### data.batches.dependencies.dependent
__Type:__ String  
__Required:__ Yes  
__Description:__ The UUID of the dependent execution (__data.batches.recipes.id__), i.e. the execution that shall be performed only after that of the dependency.

##### data.batches.dependencies.dependency
__Type:__ String  
__Required:__ Yes  
__Description:__ The UUID of the dependency execution (__data.batches.recipes.id__), i.e. the execution that shall be performed prior to that of the dependent.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
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
__Format:__ UNIX Epoch time, in milliseconds.  
__Required:__ Yes  
__Description:__ The event creation timestamp.

### meta.tags
__Type:__ String[]  
__Format:__ Free text  
__Required:__ No  
__Description:__ Any tags or keywords associated with the events, for searchability purposes.

### meta.source
__Type:__ Object  
__Required:__ No  
__Description:__ A description of the source of the event. This object is primarily for traceability purposes, and while optional, some form of identification of the source is __HIGHLY RECOMMENDED__. It offers multiple methods of identifying the source of the event, techniques which may be select from based on the technology domain and needs in any particular use case.

#### meta.source.domainId
__Type:__ String  
__Format:__ Free text  
__Required:__ No  
__Description:__ Identifies the [domain](../eiffel-syntax-and-usage/glossary.md#domain) that produced an event.

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
__Type:__ String  
__Format:__ [purl specification](https://github.com/package-url/purl-spec)  
__Required:__ No  
__Description:__ The identity of the serializer software used to construct the event, in [purl format](https://github.com/package-url/purl-spec).

#### meta.source.uri
__Type:__ String  
__Format:__ URI  
__Required:__ No  
__Description:__ The URI of, related to or describing the event sender.

### meta.security
__Type:__ Object  
__Required:__ No  
__Description:__ An optional object for enclosing security related information, particularly supporting data integrity. See [Security](../eiffel-syntax-and-usage/security.md) for further information.

#### meta.security.authorIdentity
__Type:__ String  
__Format:__ [Distinguished Name](https://tools.ietf.org/html/rfc2253)  
__Required:__ Yes  
__Description:__ The identity of the author of the event. This property is intended to enable the recipient to identify the author of the event contents and/or look up the appropriate public key for decrypting the __meta.security.integrityProtection.signature__ value and thereby verifying author identity and data integrity.

#### meta.security.integrityProtection
__Type:__ Object  
__Required:__ No  
__Description:__ An optional object for enabling information integrity protection via cryptographic signing. To generate a correct __meta.security.integrityProtection__ object:
  1. Generate the entire event, but with the
     __meta.security.integrityProtection.signature__ value set to
     an empty string.
  1. Serialize the event on
     [Canonical JSON Form](https://tools.ietf.org/html/draft-staykov-hu-json-canonical-form-00).
  1. Generate the signature using the
     __meta.security.integrityProtection.alg__ algorithm.
  1. Set the __meta.security.integrityProtection.signature__ value to
     the resulting signature while maintaining Canonical JSON Form.
To verify the integrity of the event, the consumer then resets __meta.security.integrityProtection.signature__ to an empty string and ensures Canonical JSON Form before verifying the signature.

##### meta.security.integrityProtection.signature
__Type:__ String  
__Required:__ Yes  
__Description:__ The signature produced by the signing algorithm.

##### meta.security.integrityProtection.alg
__Type:__ String  
__Format:__ [A valid JWA RFC 7518 alg parameter value](https://tools.ietf.org/html/rfc7518#section-3.1), excluding "none"    
__Required:__ Yes  
__Description:__ The cryptographic algorithm used to digitally sign the event. If no signing is performed, the __meta.security.integrityProtection__ SHALL be omitted rather than setting __meta.security.integrityProtection.alg__ to "none".

##### meta.security.integrityProtection.publicKey
__Type:__ String  
__Required:__ No  
__Description:__ The producer of the event may include the relevant public key for convenience, rather than relying a separate key distribution mechanism. Note that this property, along with the rest of the event, is encompassed by the integrity protection offered via __meta.security.integrityProtection__.

#### meta.security.sequenceProtection
__Type:__ Object[]  
__Required:__ No  
__Description:__ An optional object for enabling verification of intact event sequences in a distributed environment, thereby protecting against data loss, race conditions and replay attacks. It allows event publishers to state the order in which they produce a certain set of events. In other words, it cannot provide any global guarantees as to event sequencing, but rather per-publisher guarantees. Every object in the array represents a named sequence of which this event forms a part. For every event including a given named sequence, the publisher SHALL increment __meta.security.sequenceProtection.position__ by 1. The first event produced in a given named sequence SHALL numbered 1.

##### meta.security.sequenceProtection.sequenceName
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the sequence. There MUST not be two identical __meta.security.sequenceProtection.sequenceName__ values in the same event.

##### meta.security.sequenceProtection.position
__Type:__ Integer  
__Required:__ Yes  
__Description:__ The number of the event within the named sequence.

### meta.schemaUri
__Type:__ String  
__Format:__ URI  
__Required:__ No  
__Description:__ A URI pointing at a location from where the schema used when creating this event can be retrieved. It can be used to parse event data for validation and extraction purposes, for example. Note, that the schema on that URI should be considered immutable.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 4.3.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 4.2.0 | No edition set | Add missing testCase.version member (see [Issue 288](https://github.com/eiffel-community/eiffel/issues/288)). |
| 4.1.1 | [edition-lyon](../../../tree/edition-lyon) | Add missing validation pattern to links.target member (see [Issue 271](https://github.com/eiffel-community/eiffel/issues/271)). |
| 4.1.0 | No edition set | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 4.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 3.0.0 | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 2.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 2.0.0 | [f92e001](../../../blob/f92e001c88d1139a62f8ace976958e0a30d8f9c5/eiffel-vocabulary/EiffelTestExecutionRecipeCollectionCreatedEvent.md) | Changed syntax of data.batches.recipes.constraints from an uncontrolled object to a list of key-value pairs to comply with design guidelines. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |


## Examples

* [Example using data.batches](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batches.json)
* [Example using data.batches (1.0.0 syntax)](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batches-1.0.0.json)
* [Example using data.batchesUri](../examples/events/EiffelTestExecutionRecipeCollectionCreatedEvent/batchesUri.json)
