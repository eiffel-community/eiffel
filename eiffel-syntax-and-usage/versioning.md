<!---
   Copyright 2017-2021 Ericsson AB and others.
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

# Versioning
In Eiffel, each individual event type is versioned independently. This version is declared by the __meta.version__ property (see [The Meta Object](./the-meta-object.md)) and follows the [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) format. The documentation of each event type lists the complete version history of that type, including links to commits introducing older versions of the type.

The independent versioning of event types, as opposed to a protocol-wide versioning scheme, was chosen for the greater flexibility and extensibility it affords. There are consequences, however, which are important to understand:
* Consumers must always be ready to receive event types which they are unable to parse: the event producer may be ahead of the consumer on one event type, but not another. Similarly, new and/or custom event types must be expected and handled.
* Backwards incompatible changes may not be introduced to the __meta.type__ and __meta.version__ properties, as these together form the key which allows the consumer to unlock the remainder of the event.

That being said, to facilitate compatibility and consistency, the Eiffel protocol as described in this repository is released in named and internally coherent _editions_. Each of these editions is represented as a GitHub [release](https://github.com/eiffel-community/eiffel/releases). A history of Eiffel editions is available below.

| Edition   | Tag                                                 | Changes                                          |
| --------- | --------------------------------------------------- | ------------------------------------------------ |
| Tacna  | _Reserved for future use._  | |
| Budapest  | _Reserved for future use._  | |
| Ruhnu  | _Reserved for future use._  | |
| Santiago  | _Reserved for future use._  | |
| Orizaba  | [edition-orizaba](../../../tree/edition-orizaba)  | Add ORIGINAL_TRIGGER link to ActT/TCT/TSS ([Issue 246](https://github.com/eiffel-community/eiffel/issues/246)), add ArtD event ([Issue 239](https://github.com/eiffel-community/eiffel/issues/239)), TCT can now link directly to SCC or SCS without using an intermediary CD  ([Issue 317](https://github.com/eiffel-community/eiffel/issues/317)). |
| Arica  | [edition-arica](../../../tree/edition-arica)  | Added optional file digest member to ArtC ([Issue 290](https://github.com/eiffel-community/eiffel/issues/290)), added meta.schemaUri member ([Issue 280](https://github.com/eiffel-community/eiffel/issues/280)), added PRECURSOR link type to ActT, TCT, and TSS ([Issue 227](https://github.com/eiffel-community/eiffel/issues/227)), added testCase.version member to TERCC ([Issue 288](https://github.com/eiffel-community/eiffel/issues/288)). |
| Lyon  | [edition-lyon](../../../tree/edition-lyon)  | Added domainId member to links ([Issue 233](https://github.com/eiffel-community/eiffel/issues/233)), added {mediaType,tags} to data.{liveLogs,persistentLogs} of various event types ([Issue 166](https://github.com/eiffel-community/eiffel/issues/166)), added RUNTIME_ENVIRONMENT as link type for ED ([Issue 258](https://github.com/eiffel-community/eiffel/issues/258)), and added missing validation pattern for links.target of TERCC ([Issue 271](https://github.com/eiffel-community/eiffel/issues/271)). |
| Paris  | [edition-paris](../../../tree/edition-paris)  | Minor backwards-compatible changes to CD and ArtP (Issues [218](https://github.com/eiffel-community/eiffel/issues/218) and [248](https://github.com/eiffel-community/eiffel/issues/248)). |
| Agen-1  | [edition-agen-1](../../../tree/edition-agen-1)  | Maintenance release to solve [Issue 205](https://github.com/eiffel-community/eiffel/issues/205). |
| Agen  | [edition-agen](../../../tree/edition-agen)  | Introduced [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md). Updated meta.security of all event types. Changed from GAV to purl based artifact identification. Introduced automated packaging of schema files for edition tags. Added detailed rules and examples for event type version stepping. |
| Toulouse  | [edition-toulouse](../../../tree/edition-toulouse)  | Stepped major version of TERCC. Updated FLOW_CONTEXT link type, resulting in new minor version of all event types. |
| Bordeaux  | [edition-bordeaux](../../../tree/edition-bordeaux)  | Initial edition. |

The [schema definition files](event-schemas.md) document the mappings between event versions and editions.

## Rules for patch, minor and major versions
In the case of a communication protocol, applying Semantic Versioning is not as straight-forward as for a regular software implementation. The ground rule is to consider backwards compatibility from the perspective of the consumer of an event. Below are rules and examples of how this applies to the Eiffel protocol.

* Mere documentation updates with no impact on event schemas require no stepping of the version at all. Indeed, the version is best understood as a _schema_ versions. Or, conversely, documentation SHALL NOT be updated in such a way as to change the semantics of event types or their properties without also making a change to the schema. To exemplify, changing the meaning of a property without changing its name or format is not allowed, as this introduces hidden compatibility issues.
* An exception to the prior rule is changes in the allowed link types and their properties (e.g. if multiple links of a particular type are allowed). Even though the link types currently aren't covered by the schemas we version the schemas as if the opposite were true. Consequently, adding a new link type SHALL result in a minor version increment and a removed link type SHALL result in a major version increment.
* __patch:__ The patch version is incremented for changes that do not affect event structure, do not carry semantic significance and do not introduce additional legal values. To exemplify, narrowing a string pattern in a schema (e.g. from `[a-zA-Z_]` to `[a-zA-Z]`) would require the patch version to be stepped.
* __minor:__ The minor version is incremented for changes to event structure or other changes that carry semantic significance but are backwards compatible from a consumer's point of view. To exemplify, adding a property to an event type without changing the syntax of existing properties would require the minor version to be stepped. Note that existing _producers_ may not be able to produce the new event type version, but a _consumer_ SHALL be able to derive the same information as from the previous version. Note that this means that consumers SHOULD be prepared to handle (and disregard) unrecognized properties in higher minor versions than they are familiar with.
* __major:__ The major version is incremented for changes that are not backwards compatible from the consumer's point of view. To exemplify, removing or renaming an existing property would require the major version to be stepped. Similarly, broadening a string pattern to allow additional legal values (e.g. from `[a-zA-Z]` to `[a-zA-Z_]`) requires the major version to be stepped.

## Updating Historical Event Types and Editions
As with any software, historical versions may need to be updated occasionally. Users of a specific edition of the Eiffel protocol may require improvements or corrections, without having to migrate to the latest event type versions. Such changes are perfectly permissible: it is important to understand that the versions do not represent chronology, but compatibility. In other words, version 2.1.0 of a particular event type may well be introduced _after_ version 3.0.0. The one exception is that only the highest extant version at any given level may step that level. To exemplify:

* If 2.0.0 and 3.0.0 exist, only the 3.0.0 event may serve as the baseline for a new major version (thereby stepping to 4.0.0).
* If 2.0.0 and 2.1.0 exist, only the 2.1.0 event may serve as the baseline for a new minor version (thereby stepping to 2.2.0).
* If 2.0.0 and 2.0.1 exist, the 2.0.0 event may not serve as a baseline for new versions. Instead the 2.0.1 event shall be used as baseline for changes to the event type.

Users are not bound to use only event types included in an edition. To exemplify, a consumer may accept all [edition-toulouse](../../../tree/edition-toulouse) events, plus [EiffelIssueVerifiedEvent](../eiffel-vocabulary/EiffelIssueVerifiedEvent.md) 2.0.0, which is not included in that edition. Indeed, it may also accept additional events not included at all, such as [EiffelIssueDefinedEvent](../eiffel-vocabulary/EiffelIssueDefinedEvent.md). In this sense, editions are non-exclusive. That being said, if there is a need to identify a collection of events updated from a historical edition, a new edition may be created for that purpose. The naming scheme of such editions SHALL be `<baseline edition name>-<increment integer starting at 1>`. To exemplify, an updated [edition-toulouse](../../../tree/edition-toulouse) would be named `edition-toulouse-1`, while a subsequent one would be named `edition-toulouse-2`, et cetera.

## Experimental event versions
To allow for experimentation with new event types that require actual usage to be fully understood and evaluated, pre-1.0.0 version numbers may be used. The first experimental version of an event is 0.1.0, and stepping the minor and patch components of such versions is done in the usual manner except the important difference that backwards incompatible changes may take place in any 0.x.y version. The introduction of a 0.x.y version of an event type does not imply that there will ever be a 1.0.0 version; it may be abandoned and not included in subsequent protocol editions.

Other events types may link to events that only exist as experimental. Normal rules apply when adding or removing such link types from a source event, i.e. adding the link requires a minor version stepping and removing it again (e.g. if the experimental event type is abandoned) requires a major version stepping. The source event type documentation should note that the target event type is experimental and that the link type may be removed in a later version.
