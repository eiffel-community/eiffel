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

# Custom Events
Eiffel offers a rich vocabulary designed to cover the vast majority of continuous integration and delivery use cases. Situations may arise where the defined events are not sufficient, however. In such circumstances, users are encouraged to spawn a discussion by [creating an Issue in the Eiffel repository](https://github.com/eiffel-community/eiffel/issues) - perhaps the existing vocabulary can be used, or perhaps the new use case warrants changes to the Eiffel event definitions.

That being said, users are free to send custom complementary events in parallel with Eiffel events. These events can be defined similarly to the standard vocabulary and may use __links__ to reference the standard Eiffel events. When defining such custom events, however, there are a few rules of conduct that users are strongly encouraged to observe:

* Custom events are not allowed masquerade as standard Eiffel events, and shall therefore not be prefixed "Eiffel". To exemplify, a recommended custom event name would be "MyCustomEvent", but not "EiffelMyCustomEvent".
* Use [Issues](https://github.com/eiffel-community/eiffel/issues) and [Pull requests](https://github.com/eiffel-community/eiffel/pulls) to stay in touch with the community to discuss why and how you define custom events. Others may find them useful, too!
* Follow the [event design guidelines](../eiffel-syntax-and-usage/event-design-guidelines.md).
* Consider whether your need can be addressed by __data.customData__.
* Users defining custom events are responsible for them and any compatibility issues. Special considerations or support from standard Eiffel events can not be expected, unless the custom events are proposed to and accepted into the standard Eiffel vocabulary (and consequently are no longer custom).