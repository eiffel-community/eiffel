<!---
   Copyright 2020 Ericsson AB.
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

# Eiffel Glossary
This a non-exhaustive, alphabetical list of terms used in the Eiffel Vocabulary and its documentation.

 - [Terms Used in Event Definitions](#terms-used-in-event-definitions)
   - [Activity](#activity)
   - [Artifact](#artifact)
   - [Environment](#environment)
   - [Event](#event)
   - [Source Change](#source-change)
   - [Submit](#submit)

 - [Terms Used in Documentation](#terms-used-in-documentation)
   - [Pipeline](#pipeline)
   - [Step](#step)

## Terms Used in Event Definitions
These terms are either part of the event names in the Eiffel Vocabulary, or they are part of parameter names or values in the events. Users of Eiffel should be able to rely on these terms to be kept, unless a major change to event types are done.

### Activity
An _activity_ is any kind of action in a CI/CD system, normally triggered by an operation done in an SCM system or by a previous activity. It's purpose is to notify what is going on and what has finished, and when, and with what outcome.

Activities are hierarchical. Activities could be whole [pipelines](#pipeline), [pipeline steps](#pipeline-step) or any level of pipeline sub steps. And those steps could for example be build activities or test activities.

An activity could also be an SCM operation such as a manual code review or automated source change check. 

### Artifact
_Artifacts_ are items or software packages generated in a CI/CD [pipeline](#pipeline), for example a built binary or a Docker image. An artifact should be possible to identify using a purl (package URL). An artifact is often the subject of a test executed or a delivery performed within a CI/CD [pipeline](#pipeline).

### Environment
An Eiffel _environment_ defines the environment in which an [activity](#activity) is executed. Could be for example a host, node, service name/uri, a Docker image or some other kind of machine configuration definition.

### Event
An Eiffel _event_ is a broadcast notification telling any consumer about an event occurring in the CI/CD [pipeline](#pipeline).

### Source Change
A _source change_ is the unit of a review. It results in a single commit when merged to the Git repository.

### Submit
A _submit_ is the action of merging a [source change](#source-change) to its intended target branch.

## Terms Used in Documentation
These terms are not defined by Eiffel. They are added here to enable a homogenous and easy read protocol documentation. These terms are subject to change without notice if a better name is found or defined elsewhere.

### Pipeline
A _pipeline_ is an ordered set of [pipeline steps](#pipeline-step) often triggered by a source change being created or submitted.

### Pipeline Step
A _pipeline step_ is used in the Eiffel protocol documentation to exemplify operations executed in a [pipeline](#pipeline).
