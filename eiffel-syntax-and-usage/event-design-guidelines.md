<!---
   Copyright 2017 Ericsson AB.
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

# Event Design Guidelines
The design of Eiffel events is governed by the following guidelines:

* __What to communicate is volitional; how to communicate it is not:__ Users shall never be required to use the entire Eiffel vocabulary to derive benefit. The ability to use only a small subset to solve a particular problem shall always be safeguarded. How to communicate what is to be communicated, however, shall leave minimal room for interpretation.
* __Events as engineering artifact proxies:__ Eiffel events represent engineering artifacts - items generated in software development – particularly in the realm of continuous integration and delivery. In this way, they are designed to act as proxies and handles of those artifacts.
* __Referencing over duplication:__ Whenever feasible, do not duplicate what could instead be referenced – both in the case of Eiffel entities and non-Eiffel entities.
* __Event content and delivery are separate concerns:__ Do not include envelope details in the event contents, and do not introduce technology dependencies into event contents.
* __Do not use variable key names:__ For purposes of automated validation, analysis and search, custom key names shall be avoided. Consequently, for custom key-value pairs `{ "key": "customKeyName", "value": "customValue" }` shall be used instead of `{ "customKeyName": "customValue" }`.
* __Use industry generic terminology:__ Wherever possible, rely on industry standards (or at least de-facto standards) rather than internal company specific terminology.
* __Always use explicit semantics:__ Avoid ambiguous fields left open to interpretation. A key benefit of Eiffel is that it provides a common language for continuous integration and delivery to exchange information – when events are left open to interpretation this benefit is spoiled.
* __Secure technology agnosticity:__ Eiffel event design shall make no assumptions with regards to underlying infrastructure or tooling.
* __Secure flexibility:__ Eiffel events shall be designed as descriptive, rather than prescriptive. It shall be assumed that the recipient will react in an intelligent and conducive manner to the information it gathers.
* __Secure scalability:__ Eiffel events shall be designed so as to serve as natural extension points of continuous integration and delivery systems, where listeners - geographically and organizationally distributed - can hook into the chain of events and build upon it with preserved traceability and semantically unambiguous links.
* __Secure traceability:__ Eiffel events shall provide semantically unambiguous trace links between multiple types of engineering artifacts - where proxied by Eiffel events by linking to those events, where not through conducive ad-hoc referencing mechanism with a bias for URIs.
* __Be opinionated but open-minded:__ Eiffel events shall be designed to allow for diverse ways of working, while at the same time encouraging good practice.
* __Information model integrity over reader convenience:__ Eiffel events are not convenient to read – or to publish – as they require graph traversal in order to derive any meaningful information. Do not work around this by including convenience information (typically duplication). Such measures will never be completely satisfactory. Instead the primary concern of event design is information model integrity; readability and usability is the concern of services built upon that data source.
* __Key names in camelCase:__ All key names shall use camelCase.
* __Enumerations in CAPS_WITH_UNDERSCORE:__ All enumerated values shall use CAPS_WITH_UNDERSCORE.
* __Link types are nouns:__ Link types shall have names that fit the pattern "\<target event> is the \<source event>'s \<link type>", implying that they are nouns that describe the relationship between the source and the target event.
