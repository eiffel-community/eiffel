<!---
   Copyright 2017-2023 Ericsson AB.
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

# Compositions and validity checking
A central concept in Eiffel is that of _compositions_. A composition represents a set of source, artifact and documentation items defined by [EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md) for some purpose, e.g. forming an execution environment, defining the contents of a delivery or instructing the integration of a system. Compositions may be very simple, consisting of a single item, or very large, containing any number of items in nested composition structures.

## Composition Validity
Using the __data.dependsOn__, __data.implements__ and __data.requiresImplementation__ members of [EiffelArtifactCreatedEvent](../eiffel-vocabulary/EiffelArtifactCreatedEvent.md) the validity of any given composition can be checked.

### Checking Dependencies
In this straight forward example, the integration of a system requires the presence of an interface and a third party library. Consider the following composition:

![alt text](./composition-dependency-check-example.svg "Dependency Checking Example")

Here composition C2 is legal, but C1 is not. The reason is that B1 requires version "[1.1.0,)" of com.example:a (that is, version 1.1.0 or later). In composition C1 there is no such artifact, but in composition C2 there is.

Note that the [Maven version range syntax](http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html) is used to express version ranges, but that these ranges are percent encoded as the version component of the [purl identity](https://github.com/package-url/purl-spec) (although for readability, the version ranges are not percent encoded in this documentation).

### Checking Backend Implementation Validity
In this example we imagine a microservice setup. The service interface I has no implementation itself - instead it requires one or more implementations to which it can forward requests. There are multiple versions of the interface included, affording clients backwards compatibility.

![alt text](./composition-backend-implementation-example.svg "Backend Implementation Validity Example")

Composition C1 is not valid: it contains two instances of A, one of I1 and one of I2. A implements I from version 1.0.0 up to, but not including, 2.0.0. Hence, I2 is lacking implementation is this composition.

Composition C2, on the other hand, is valid. It also contains two instances of A, but also one instance of B, which implements I from version 1.0.0 up to 3.0.0. Consequently, in this composition I1 has three artifacts implementing it, while I2 has one.

### Purl vs event links
Wherever feasible, the Eiffel framework promotes the usage of event references to link to other artifacts. It may seem like a reasonable option to use event links to declare dependencies, as well.

The pragmatic reason for using (adapted) [purl identities](https://github.com/package-url/purl-spec) in this particular case is version ranges: with event links there is no practical way of declaring ranges.

There is also a conceptual reason why event links are not suitable, however. Event links are consistently used to reference historical engineering artifacts - things that have been created and exist. Dependency declarations - particularly dependencies on version ranges - are much more intangible in nature. They simply provide a description of something that ought to be present. For this reason they cannot be used as trace links, and are unsuitable for event reference representation.

### Additional Notes
_Isn't this a reinvention of the wheel?_ you may ask. After all, there are plenty of tools that excel in handling dependency graphs. This is true, and the Eiffel dependency definition syntax is heavily influenced not least by [Maven](http://maven.apache.org). Eiffel operates at a highly technology and context agnostic level of abstraction, however, covering e.g. projects with highly diversified technology stacks and/or projects near or crossing over into hardware. This has both limitations and benefits. An Eiffel composition check can never guarantee that a given composition will work; what it can tell you is whether it is obviously broken.

It should also be noted that Eiffel's dependency syntax is opinionated. An interface requiring supporting implementation does not dictate that it requires any particular implementation (actually it can - simply use __data.dependsOn__). Rather, it is up to that implementation to declare that it supports the interface. This is in order to encourage separation of concerns and decoupling.

Furthermore, Eiffel's dependency syntax makes no distinction between e.g. build time and runtime dependencies. This is
for two reasons. First, it is not intended for low level dependency management: most programming languages have
dedicated and specialized tools that will handle this type of dependency management. Instead, where Eiffel's comes into
play is in tracking and validating large, sprawling systems of heterogeneous artifacts. Second, even if one attempts to
develop specific syntax each type of dependency there will always be corner use cases which are not covered: better then
to err on the side of abstraction, rather than implicitly ruling out use cases by being overly specific. That being
said, it is also generally the case that an artifact has a fair idea of its intended use - it is rare that one and the
same artifact is both a deployable service and a source code library, with the need to declare a unique set of
dependencies for each case. Hence, the EiffelArtifactCreatedEvent dependency declarations shall be read in context.
