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

# The Meta Object
The __meta__ object contains meta-information describing the event: when it was created, where it came from, its type et cetera. The __meta__ object contains the same members regardless of __meta.type__<sup>[1](#footnote1)</sup>, with the caveat that certain members are optional and the tendency to use them may vary with event type.

Even though the meta object is kept universal for all event types, it may change over time as the Eiffel protocol evolves. Due to the [per-event versioning](./versioning.md) of the protocol, this means that different unique combinations of event type, version and meta object version may feature different meta object syntax.

&nbsp;
&nbsp;

------------------
&nbsp;

<a name="footnote1">1</a>: Event types are versioned independently from one another. There are three important consequences of this. First, any change to __meta__ requires all events to be updated. Second, any schema of a specific version of an event must also include the __meta__ object – specifically as it is defined for that version of the event. Third, consumers should be prepared to receive events of varying __meta__ contents. The exception to this are the __meta.type__ and __meta.version__ fields, which are always assumed to be present change.
