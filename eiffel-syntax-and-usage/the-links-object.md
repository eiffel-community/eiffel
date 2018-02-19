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

# The Links Object
The __links__ object is an array of trace links to other Eiffel events. These trace links by definition always reference backwards in time – it is only possible to reference an event that has already occurred. Each trace link is a tuple consisting of a type and a UUID corresponding to the __meta.id__ of the target event, on String format.

Some link types allow multiple trace links, whereas others only allow one.

Example syntax of a simple __links__ object:

    "links": [
      {"type": "CAUSE", "target": "8f3e0f94-5d11-46e7-ae02-91efa15d2329"},
      {"type": "COMPOSITION", "target": "43ee71d2-6d91-496a-b9cf-d121ff1d1bcf"}
    ]

The full list of optional and required links is described in the documentation of each respective event type.
