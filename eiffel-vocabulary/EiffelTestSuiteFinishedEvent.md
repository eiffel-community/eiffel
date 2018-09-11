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

# EiffelTestSuiteFinishedEvent (TSF)
The EiffelTestSuiteFinishedEvent declares that a previously started test suite (declared by [EiffelTestSuiteStartedEvent](./EiffelTestSuiteStartedEvent.md)) has finished and reports the outcome.

Note that while similar, the __data.outcome__ object is different from that of [EiffelActivityFinishedEvent](./EiffelActivityFinishedEvent.md). The outcome of the test suite reports not only the conclusion of the test suite execution - whether the tests were successfully executed - but also passes a verdict on the item or items under test. To highlight this conceptual difference, both __data.outcome.verdict__ and __data.outcome.conclusion__ are included.

## Data Members
### data.outcome
__Type:__ Object  
__Required:__ No  
__Description:__ The outcome of the test suite.

#### data.outcome.verdict
__Type:__ String  
__Required:__ No  
__Legal values:__ PASSED, FAILED, INCONCLUSIVE  
__Description:__ A terse standardized verdict on the item or items under test. Unlike in [EiffelTestCaseFinishedEvent](./EiffelTestCaseFinishedEvent.md), this property is optional. It offers a method of summarizing the verdict of the test suite as a whole, but may be skipped.  
PASSED signifies that the item or items under test successfully passed the test suite.  
FAILED signifies that the item or items under test failed to pass the test suite.  
INCONCLUSIVE signifies that the verdict of the test suite was inconclusive. This SHOULD be the case if __data.outcome.conclusion__ is not __SUCCESSFUL__, but may in combination with a __SUCCESSFUL__ conclusion be used to represent unreliability or flakiness.

#### data.outcome.conclusion
__Type:__ String  
__Required:__ No  
__Legal values:__ SUCCESSFUL, FAILED, ABORTED, TIMED_OUT, INCONCLUSIVE  
__Description:__ A terse standardized conclusion of the test suite, designed to be machine readable. Unlike in [EiffelTestCaseFinishedEvent](./EiffelTestCaseFinishedEvent.md), this property is optional. It offers a method of summarizing the conclusion of the test suite as a whole, but may be skipped.  
SUCCESSFUL signifies that the test suite was successfully concluded. Note that this does not imply that the item under test passed the tests.  
FAILED signifies that the test suite could not be successfully executed. To exemplify, one or more tests failed to run due to required environments being unavailable.  
ABORTED signifies that the test suite was aborted before it could be concluded.  
TIMED_OUT signifies that the test suite did not conclude within the allowed time frame.  
INCONCLUSIVE signifies that the outcome of the test suite could not be determined.

#### data.outcome.description
__Type:__ String  
__Required:__ No  
__Description:__ A verbose description of the test suite outcome, designed to provide human readers with further information.

### data.persistentLogs
__Type:__ Object[]  
__Required:__ No  
__Description:__ An array of persistent log files generated during execution.

#### data.persistentLogs.name
__Type:__ String  
__Required:__ Yes  
__Description:__ The name of the log file.

#### data.persistentLogs.uri
__Type:__ String  
__Required:__ Yes  
__Description:__ The URI at which the log can be retrieved.

## Links
### TEST_SUITE_EXECUTION
__Required:__ Yes  
__Legal targets:__ [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md)  
__Multiple allowed:__ No  
__Description:__ Identifies the relevant test suite execution. In other words, [EiffelTestSuiteStartedEvent](../eiffel-vocabulary/EiffelTestSuiteStartedEvent.md) acts as a handle for a particular test suite execution.

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
| 2.0.0     | Current version                                        | Introduced purl identifiers instead of GAVs (see [Issue 182](https://github.com/eiffel-community/eiffel/issues/182)) |
| 1.1.0     | [edition-toulouse](../../../tree/edition-toulouse)     | Multiple links of type FLOW_CONTEXT allowed. |
| 1.0.0     | [edition-bordeaux](../../../tree/edition-bordeaux)     | Initial version.                        |

## Examples
* [Simple example](../examples/events/EiffelTestSuiteFinishedEvent/simple.json)
