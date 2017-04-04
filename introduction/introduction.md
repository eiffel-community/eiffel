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

# Introduction

This page provides an introduction to Eiffel: what is it, why is it and who is it for?

## Why Eiffel?
As software products steadily increase in size and complexity, so do the systems that ultimately build, test, package and deploy those products: our continuous integration and delivery systems. It is not uncommon for these systems to span entire enterprises with thousands of engineers in various roles, integrating and testing solutions in intricate webs of dependencies and causality. Historically, this has been a process management problem, but with increasing demands for speed and automation it is rapidly transforming into a software engineering problem.

Furthermore, it is a software engineering problem that can scarcely be solved by standardizing on a common set of tools and processes. Attempts are often made to align on one SCM system, one CI server, one test framework, one ticket handling system and one collaboration platform. To the extent that such efforts are initially successful, they tend to cause considerable headache when incorporating new products through e.g. acquisitions, not to mention the aggravation when developers are told they can't use the latest hottest tools because they aren't compatible with the corporate ways of working. Wars have been fought over less.

The Eiffel philosophy is to treat the continuous integration and delivery system just like any other complex and constantly changing software system, and apply the same architectural thinking. In Eiffel that new acquisition or those rebellious developers can have their cake and eat it, too. Heterogenous tools and processes are allowed to co-exist by applying a thin layer of glue on top of it all, focusing on the essential pieces of information we need in order to collaborate. And, analogous to a microservices oriented system, various services can then be added on top of that glue to store, process, analyze, visualize and act upon those essential pieces of information, affording you transparency across the enterprise.

## What is Eiffel?
Eiffel is a framework for continuous integration and delivery, particularly addressing the challenges of a distributed and heterogeneous environment at an enterprise scale. It does this through the _in situ_ real time generation of globally broadcast events - events which reference one another, forming a Directed Acyclic Graph (DAG) describing all the activities of the continuous integration and delivery pipeline, regardless of where they took place, which underlying technology they used, or even whether they were automated or not. 

Eiffel fundamentally consists of two parts. First, a vocabulary and syntax of events, forming the communication protocol of the framework. Second, services built on top of that communication protocol to orchestrate continuous integration and delivery activities, provide traceability, dashboards, visualizations and much more.

## Who Developed Eiffel?
Eiffel was originally conceived and developed by Ericsson, where it has successfully been used to realize enterprise-wide continuous integration and delivery solutions ever since. The framework was published under the [Apache License 2.0](../LICENSE) in 2016.

## Who Should Use Eiffel?
Eiffel is technology and domain agnostic - it may be applied equally well to the continuous integration and delivery of any type of software product. That being said, it was designed with scalability and traceability of large scale systems integration in mind, and it is at scale that Eiffel brings the greatest benefits.

## How Do I Get Started?
To use Eiffel you need three things: the Eiffel vocabulary, messaging infrastructure and services operating on, storing and analyzing your Eiffel events.

The Eiffel vocabulary can be adopted incrementally - which events you use is up to you, but _how_ they are used is heavily standardized to ensure interoperability and alignment on proven practices. 

There are several valid out-of-the-box solutions for event transport and routing infrastructure, depending on your needs and preferences. Examples include [RabbitMQ](https://www.rabbitmq.com/), [Kafka](http://kafka.apache.org/), [NATS](http://nats.io/) and more. When choosing infrastructure, it is important to understand the implications of the different types of guarantees these solutions can offer. While some provide durable queues and delivery guarantees, others do not, but instead offer higher performance. It is important to consider one's requirements and choose the appropriate solution for event transport and routing accordingly; to maximize reliability and traceability capabilities, it is generally recommended to choose a solution with durable queues and delivery guarantees.

Services for Eiffel event handling address a multitude of needs. These services range from very simplistic to highly complex, and just like the Eiffel vocabulary one is free to pick and choose what suits the particular case. The documentation in this repository links such services as they become available, addressing e.g. [event dispatch](../implementations/event-dispatch.md) and [event aggregation and analysis](../implementations/event-aggregation-and-analysis.md).

## How is Eiffel Technology Agnostic?
Eiffel provides a communication protocol geared towards machine-to-machine continuous integration and delivery communication; it makes no assumptions with regards to underlying infrastructure (though widely used messaging solutions are recommended, as discussed above) or choice of continuous integration servers, test frameworks, source code management systems or other tooling. As long as the tools you use can be plugged into or configured to access services for event [dispatch](../implementations/event-dispatch.md) or [analysis](../implementations/event-aggregation-and-analysis.md), you're good to go.

## How Does Eiffel Achieve Scalability?
Eiffel is not a centralized or monolithic tool. Instead it represents a decentralized and federated approach to driving and documenting enterprise scale continuous integration and delivery systems. By broadcasting events globally and allowing any tool or service to react as it sees fit to those events several important goals are achieved:
* Continuous integration and delivery activities can be distributed and communicate across multiple hosts, labs or even continents.
* Responsibilities for developing and managing can more easily be distributed and consequently scaled, through clear event based interfaces.
* It removes centralized continuous integration servers as bottlenecks.

## How Does Eiffel Achieve Flexibility?
An important principle in Eiffel is that events are not prescriptive, but descriptive. An event is not an RPC call, it will not order the recipient to take a certain action. Instead, it is assumed that the recipient will react in an intelligent and conducive manner to the information it gathers. Holding to this principle becomes particularly important in large, multi-organizational integration contexts, as it allows decoupling and separation of concerns between consumers and producers of events. 

To exemplify, an organization developing a common component does not - and indeed should not - need to know how the continuous integration systems of its consumers are set up. As long as it accurately report on its own process as it builds, tests and verifies new versions consumers may come and go, or may decide to pick up specific deliveries or not, for any reason, without any need to notify or synchronize with the developing organization. Despite this traceability is still preserved: looking up who has integrated which component version when, how long it took, and whether they are included in any customer releases is but a query away.

Consequently, the larger enterprise-wide continuous integration and delivery system becomes highly flexible in that it may be modified and extended without synchronization or central orchestration.

## How Does Eiffel Achieve Traceability?
The basis of software traceability is _engineering artifacts_ - anything generated in the development process, including e.g. source code changes, documentation, product versions, work items, requirements et cetera - and _trace links_ between these engineering artifacts, describing their relationships. These artifacts referencing other artifacts create graphs which may be traversed to answer questions such as which changes have been implemented in a given product version or which requirements have been tested when and where.

Eiffel builds upon this principle. Think of Eiffel events as proxies or handles for these engineering artifacts, and the links between them as trace links. By storing and analyzing the resulting graphs any number of concerns of any number of stakeholders can be addressed:
* Into which system revisions has this source change been integrated?
* Which bug fixes have been included in this product release?
* Which requirements have been verified in which environments for this release candidate?
* What is the average lead time from source commit to live deployment?
* When was this work item first tested ok?
* et cetera

## How Do I Make Sense of Events?
A single Eiffel event only tells a fragment of the story. To derive real value, it must be analyzed together with the many other events it references. This is both a strength and a weakness: a strength because it affords separation of concerns and a tight, standardized syntax; a weakness because it makes it difficult to react intelligently to just the one event.

As a consequence, effective analysis of Eiffel events requires supporting implementations. A minimum requirement is some form of [persistence](../implementations/event-persistence.md), allowing users to analyze not just current events, but to dig into the historical record. True value is gained, however, when using [more intelligent services with the ability to raise the level of abstraction from raw events and present aggregated data](../implementations/event-aggregation-and-analysis.md), and [visualization solutions](../implementations/visualization.md) building on top of those aggregations.