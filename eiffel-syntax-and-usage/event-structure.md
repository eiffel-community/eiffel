<!---
   Copyright 2017 Ericsson AB.

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

# Event Structure
Eiffel events are represented as JSON objects. These JSON objects contain three required members: __meta__, __data__ and __links__.

## meta
__Type:__ Object  
__Required:__ Yes  
__Description:__ This object contains fields common to all event types: meta-data describing the event itself. It is described in detail [here](./the-meta-object.md).

## data
__Type:__ Object  
__Required:__ Yes  
__Description:__ This object contains all fields specific to the event type – the payload of the event – including trace links to non-Eiffel entities. It is described in detail per event type.

## links
__Type:__ Object  
__Required:__ Yes  
__Description:__ This object contains all trace links to other Eiffel events. It is described in detail [here](./the-links-object.md).
