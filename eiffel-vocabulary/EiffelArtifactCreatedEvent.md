<!---
   This file was generated from ../definitions/EiffelArtifactCreatedEvent/3.3.0.yml.
   See that file for a copyright notice.
--->

# EiffelArtifactCreatedEvent (ArtC)

The EiffelArtifactCreatedEvent declares that a software artifact has been created, what its coordinates are, what it contains and how it was created.

## Data Members

### data.identity
__Type:__ String  
__Format:__ [purl specification](https://github.com/package-url/purl-spec)  
__Required:__ Yes  
__Description:__ The identity of the created artifact, in [purl format](https://github.com/package-url/purl-spec).

### data.fileInformation
__Type:__ Object[]  
__Required:__ No  
__Description:__ A list of the artifact file contents. This information is optional and, when included, MAY include a complete or incomplete list of contents. In other words, it may be used to highlight only particular files of interest, such as launcher binaries or other entry-points.

#### data.fileInformation.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name (including relative path from the root of the artifact) on syntax appropriate for the artifact packaging type.

#### data.fileInformation.tags
__Type:__ String[]  
__Required:__ No  
__Description:__ Any tags associated with the file, to support navigation and identification of items of interest.

#### data.fileInformation.integrityProtection
__Type:__ Object  
__Required:__ No  
__Description:__ An optional object containing a digest of the file's contents, i.e. a checksum, computed using the specified algorithm.

##### data.fileInformation.integrityProtection.alg
__Type:__ String  
__Format:__ One of the hash algorithms listed in section 1 of [NIST FIPS 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf), excluding "SHA-1".  
__Required:__ Yes  
__Legal values:__ SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256  
__Description:__ The cryptographic algorithm used to compute the digest of the file's contents.

##### data.fileInformation.integrityProtection.digest
__Type:__ String  
__Format:__ A lowercase string of hexadecimal digits.  
__Required:__ Yes  
__Description:__ The digest of the file contents.

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

### data.dependsOn
__Type:__ String[]  
__Format:__ [purl specification](https://github.com/package-url/purl-spec)  
__Required:__ No  
__Description:__ An array of [purl identified](https://github.com/package-url/purl-spec) entities this artifact depends on. While not included in the purl specification itself, the Eiffel protocol allows version range notation according to [Maven syntax](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN402) to be used for the version component of the package identity. Note that the purl specification always requires the version component to be percent-encoded.

### data.implements
__Type:__ String[]  
__Format:__ [purl specification](https://github.com/package-url/purl-spec)  
__Required:__ No  
__Description:__ An array of [purl identified](https://github.com/package-url/purl-spec) entities this artifact implements. The typical use case of this is to identify interfaces implemented by this artifact. While not included in the purl specification itself, the Eiffel protocol allows version range notation according to [Maven syntax](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN402) to be used for the version component of the package identity. Note that the purl specification always requires the version component to be percent-encoded.

### data.name
__Type:__ String  
__Required:__ No  
__Description:__ Any (colloquial) name of the artifact. Unlike __data.identity__, this is not intended as an unambiguous identifier of the artifact, but as a descriptive and human readable name.

## Links

This section describes which link types are valid for this event type. For details on how to express the link objects themselves see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md).

### CAUSE
__Required:__ No  
__Legal targets:__ Any  
__Multiple allowed:__ Yes  
__Description:__ Identifies a cause of the event occurring. SHOULD not be used in conjunction with __CONTEXT__: individual events providing __CAUSE__ within a larger context gives rise to ambiguity. It is instead recommended to let the root event of the context declare __CAUSE__.

### COMPOSITION
__Required:__ No  
__Legal targets:__ [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the composition from which this artifact was built.

### CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelActivityTriggeredEvent](../eiffel-vocabulary/EiffelActivityTriggeredEvent.md), [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the activity or test suite of which this event constitutes a part.

### ENVIRONMENT
__Required:__ No  
__Legal targets:__ [EiffelEnvironmentDefinedEvent](../eiffel-vocabulary/EiffelEnvironmentDefinedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the environment in which this artifact was built.

### FLOW_CONTEXT
__Required:__ No  
__Legal targets:__ [EiffelFlowContextDefinedEvent](../eiffel-vocabulary/EiffelFlowContextDefinedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies the flow context of the event: which is the continuous integration and delivery flow in which this occurred – e.g. which product, project, track or version this is applicable to.

### PREVIOUS_VERSION
__Required:__ No  
__Legal targets:__ [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md)  
__Multiple allowed:__ Yes  
__Description:__ Identifies a latest previous version (there may be more than one in case of merges) of the artifact the event represents.

## Version History

| Version | Introduced in | Changes |
| ------- | ------------- | ------- |
| 3.3.0 | [edition-arica](../../../tree/edition-arica) | Added data.fileInformation.integrityProtection member (see [Issue 290](https://github.com/eiffel-community/eiffel/issues/290)). |
| 3.2.0 | [edition-arica](../../../tree/edition-arica) | Add schema URL to the meta object (see [Issue 280](https://github.com/eiffel-community/eiffel/issues/280)). |
| 3.1.0 | [edition-lyon](../../../tree/edition-lyon) | Add links.domainId member (see [Issue 233](https://github.com/eiffel-community/eiffel/issues/233)). |
| 3.0.0 | [edition-agen](../../../tree/edition-agen) | Improved information integrity protection (see [Issue 185](https://github.com/eiffel-community/eiffel/issues/185)). |
| 2.0.0 | [edition-agen](../../../tree/edition-agen) | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0 | [edition-toulouse](../../../tree/edition-toulouse) | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0 | [edition-bordeaux](../../../tree/edition-bordeaux) | Initial version. |
## Examples

* [Simple example](../examples/events/EiffelArtifactCreatedEvent/simple.json)
* [Interface example](../examples/events/EiffelArtifactCreatedEvent/interface.json)
* [Backend example](../examples/events/EiffelArtifactCreatedEvent/backend.json)
* [Dependent example](../examples/events/EiffelArtifactCreatedEvent/dependent.json)
* [Checksum example](../examples/events/EiffelArtifactCreatedEvent/checksum.json)
