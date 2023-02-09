<!---
   This file was generated from ../definitions/EiffelArtifactPublishedEvent/3.3.0.yml.
   See that file for a copyright notice.
--->

# EiffelArtifactPublishedEvent (ArtP)

The EiffelArtifactPublishedEvent declares that a software artifact (declared by [EiffelArtifactCreatedEvent](./EiffelArtifactCreatedEvent.md)) has been published and is consequently available for retrieval at one or more locations.

## Data Members

### data.locations
__Type:__ Object[]  
__Required:__ Yes  
__Description:__ A list of locations at which the artifact may be retrieved.

#### data.locations.name
__Type:__ String  
__Required:__ No  
__Description:__ Identifies the name of the file within the artifact for which this location provides the URI. Must correspond to a __data.fileInformation.name__ value in the [EiffelArtifactCreatedEvent](./EiffelArtifactCreatedEvent.md) connected via the __ARTIFACT__ link.

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

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### ARTIFACT
__Required:__ Yes  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the artifact that was published.

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
| 3.3.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.2.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.1.0 | [edition-paris](../../../tree/edition-paris) | Added name qualifier for artifact locations (see [Issue 248](https://github.com/eiffel-community/eiffel/issues/248)) |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelArtifactPublishedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |


## Examples

* [Simple example](../examples/events/EiffelArtifactPublishedEvent/simple.json)
