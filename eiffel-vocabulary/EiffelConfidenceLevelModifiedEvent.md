<!---
   This file was generated from ../definitions/EiffelConfidenceLevelModifiedEvent/3.2.0.yml.
   See that file for a copyright notice.
--->

# EiffelConfidenceLevelModifiedEvent (CLM)

The EiffelConfidenceLevelModifiedEvent declares that an entity has achieved (or failed to achieve) a certain level of confidence, or in a broader sense to annotate it as being applicable or relevant to a certain case (e.g. fit for release to a certain customer segment or having passed certain criteria). This is particularly useful for promoting various engineering artifacts, such as product revisions, through the continuous integration and delivery pipeline.

Confidence levels may operate at high or low levels of abstraction - ranging from "smokeTestsOk" to "releasable" or "released" - and they may group other confidence levels of lower abstraction levels. They may also be general or very niched, e.g. "releasable" or "releasableToCustomerX". Confidence levels frequently figure in automated delivery interfaces within a tiered system context: lower level tiers issue an agreed confidence level signaling that a new version is ready for integration in a higher level tier.

## Data Members

### data.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the confidence level. It is recommended for confidence level names to conform with camelCase formatting, in line with the format of key names of the Eiffel protocol as a whole.

### data.value
__Type:__ String  
__Required:__ Yes  
__Legal values:__ SUCCESS, FAILURE, INCONCLUSIVE  
__Description:__ The value of the confidence level.
SUCCESS signifies that the confidence level has been successfully achieved.  
FAILURE signifies that the confidence level could not be achieved.
INCONCLUSIVE signifies that achievement of the confidence level could not be determined.

### data.issuer
__Type:__ Object  
__Required:__ No  
__Description:__ The individual or entity issuing the confidence level.

#### data.issuer.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the issuer.

#### data.issuer.email
__Type:__ String  
__Required:__ No  
__Description:__ The e-mail address of the issuer.

#### data.issuer.id
__Type:__ String  
__Required:__ No  
__Description:__ Any identity, alias or handle of the issuer, such as a corporate id or username.

#### data.issuer.group
__Type:__ String  
__Required:__ No  
__Description:__ Any group, such as a development team, committee or test group, to which the issuer belongs.

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

### SUBJECT
__Required:__ Yes  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md), [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md), [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md), [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a subject of the confidence level; in other words, what the confidence level applies to.

### SUB_CONFIDENCE_LEVEL
__Required:__ No  
__Legal targets:__ [EiffelConfidenceLevelModifiedEvent](../eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Used in events summarizing multiple confidence levels. Example use case: the confidence level "allTestsOk" summarizes the confidence levels "unitTestsOk, "scenarioTestsOk" and "deploymentTestsOk", and consequently links to them via __SUB_CONFIDENCE_LEVEL__. This is intended for purely descriptive, rather than prescriptive, use.

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
| 3.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelConfidenceLevelModifiedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |


## Examples

* [Simple example](../examples/events/EiffelConfidenceLevelModifiedEvent/simple.json)
