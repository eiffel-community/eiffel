<!---
   This file was generated from ../definitions/EiffelSourceChangeCreatedEvent/4.2.0.yml.
   See that file for a copyright notice.
--->

# EiffelSourceChangeCreatedEvent (SCC)

The EiffelSourceChangeCreatedEvent declares that a change to sources has been made, but not yet submitted (see [EiffelSourceChangeSubmittedEvent](./EiffelSourceChangeSubmittedEvent.md)). This can be used to represent a change done on a private branch, undergoing review or made in a forked repository. Unlike EiffelSourceChangeSubmittedEvent, EiffelSourceChangeCreatedEvent _describes the change_ in terms of who authored it and which issues it addressed.

Where changes are integrated (or "submitted") directly on a shared branch of interest (e.g. "master", "dev" or "mainline") both EiffelSourceChangeCreatedEvent and EiffelSourceChangeSubmittedEvent are sent together.

## Data Members

### data.author
__Type:__ Object  
__Required:__ No  
__Description:__ The author of the change.

#### data.author.name
__Type:__ String  
__Required:__ No  
__Description:__ The name of the author.

#### data.author.email
__Type:__ String  
__Required:__ No  
__Description:__ The email address of the author.

#### data.author.id
__Type:__ String  
__Required:__ No  
__Description:__ Any identity, username or alias of the author.

#### data.author.group
__Type:__ String  
__Required:__ No  
__Description:__ Any group or organization to which the contributor belongs.

### data.change
__Type:__ Object  
__Required:__ No  
__Description:__ A summary of the change.

#### data.change.insertions
__Type:__ Integer  
__Required:__ No  
__Description:__ The number of inserted lines in the change.

#### data.change.deletions
__Type:__ Integer  
__Required:__ No  
__Description:__ The number of deleted lines in the change.

#### data.change.files
__Type:__ String  
__Required:__ No  
__Description:__ A URI to a list of files changed, on JSON String array format.

#### data.change.details
__Type:__ String  
__Required:__ No  
__Description:__ A URI to further details about the change. These details are not assumed to be on any standardized format, and may be intended for human and/or machine consumption. Examples include e.g. Gerrit patch set descriptions or GitHub commit pages. It is recommended to also include __data.change.tracker__ to provide a hint as to the nature of the linked details.

#### data.change.tracker
__Type:__ String  
__Required:__ No  
__Description:__ The name of the tracker, if any, of the change. Examples include e.g. Gerrit or GitHub.

#### data.change.id
__Type:__ String  
__Required:__ No  
__Description:__ The unique identity, if any, of the change (apart from what is expressed in the identifier object). Examples include e.g. Gerrit Change-Ids or GitHub Pull Requests. It is recommended to also include __data.change.tracker__ to provide a hint as to the nature of the identity.

### data.gitIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a Git change.

#### data.gitIdentifier.commitId
__Type:__ String  
__Required:__ Yes  
__Description:__ The commit identity (hash) of the change.

#### data.gitIdentifier.branch
__Type:__ String  
__Required:__ No  
__Description:__ The name of the branch where the change was made.

#### data.gitIdentifier.repoName
__Type:__ String  
__Required:__ No  
__Description:__ The name of the repository containing the change.

#### data.gitIdentifier.repoUri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the repository containing the change.

### data.svnIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a Subversion change.

#### data.svnIdentifier.revision
__Type:__ Integer  
__Required:__ Yes  
__Description:__ The revision of the change.

#### data.svnIdentifier.directory
__Type:__ String  
__Required:__ Yes  
__Description:__ The directory (branch/tag) of the change.

#### data.svnIdentifier.repoName
__Type:__ String  
__Required:__ No  
__Description:__ The name of the repository containing the change.

#### data.svnIdentifier.repoUri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the repository containing the change.

### data.ccCompositeIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a composite ClearCase change – in other words, not single file commit, but analogous of repository-wide commits of e.g. SVN or Git.

#### data.ccCompositeIdentifier.vobs
__Type:__ String[]  
__Required:__ Yes  
__Description:__ The names of the changed ClearCase VOBs.

#### data.ccCompositeIdentifier.branch
__Type:__ String  
__Required:__ Yes  
__Description:__ The branch of the change.

#### data.ccCompositeIdentifier.configSpec
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the relevant ClearCase config spec.

### data.hgIdentifier
__Type:__ Object  
__Required:__ No  
__Description:__ Identifier of a Mercurial change.

#### data.hgIdentifier.commitId
__Type:__ String  
__Required:__ Yes  
__Description:__ The commit identity (hash) of the change.

#### data.hgIdentifier.branch
__Type:__ String  
__Required:__ No  
__Description:__ The branch of the change.

#### data.hgIdentifier.repoName
__Type:__ String  
__Required:__ No  
__Description:__ The name of the repo.

#### data.hgIdentifier.repoUri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI of the repo.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### BASE
__Required:__ No  
__Legal targets:__ [EiffelSourceChangeSubmittedEvent](../eiffel-vocabulary/EiffelSourceChangeSubmittedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the base revision of the created source change.

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

### DERESOLVED_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an issue which was previously resolved, but that this SCC claims it has made changes to warrant removing the resolved status. For example, if an issue "Feature X" was resolved, but this SCC removed the implementation that led to "Feature X" being resolved, that issue should no longer be considered resolved.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### PARTIALLY_RESOLVED_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an issue that this event partially resolves. That is, this SCC introduces some change that has advanced an issue towards a resolved state, but not completely resolved.

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelSourceChangeCreatedEvent](../eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the created source change.

### RESOLVED_ISSUE
__Required:__ No  
__Legal targets:__ [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies an issue that this SCC is claiming it has done enough to resolve. This is not an authoritative resolution, only a claim. The issue may or may not change status as a consequence this, e.g. through a [successful verification](../eiffel-vocabular/EiffelIssueVerifiedEvent.md) or a manual update on the issue tracker.

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
| 4.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 4.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 4.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 3.0.0 | [dc5ec6f](../../../blob/dc5ec6fb87e293eeffe88fdafe698eec0f5a2c89/eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 2.0.0 | [0706840](../../../blob/070684053ceb1da5fb42d9f0ef21df816961d6bc/eiffel-vocabulary/EiffelSourceChangeCreatedEvent.md) | Replaced data.issues with links |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |


## Examples

* [Simple example](../examples/events/EiffelSourceChangeCreatedEvent/simple.json)
