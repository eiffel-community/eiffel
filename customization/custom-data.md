# Custom Data
Eiffel events are designed to be generalizable to a wide array of cases and applications. To that end they often contain a number of optional data members and links which may or may not be used, depending on the level of detail required and/or feasible in any given situation. The underlying principle is that _what_ one communicates is volitional, but not _how_ one communicates it. This is to minimize the need for local dialects and thereby provide the best possible conditions for a non-initiated event consumer to make sense of any given set of events.

That being said, there are times when a highly specific and/or localized use case calls for data members not included in the Eiffel vocabulary. This is where __data.customData__ comes into play.

__data.customData__ is an optional member of _all_ Eiffel events. It is an array of key-value pairs, where the value can be of any type. This grants users a high degree of freedom in including their own, custom content in messages without any disruption to the rest of the syntax: the unitiated reader is free to simply ignore any __data.customData__ contents without fear of adverse effects.

While __data.customData__ affords users extensive freedom in including custom content, they are strongly encouraged to consider the following before making use of it:

* Are there existing Eiffel events and/or event members able to express the information? Using the standard vocabulary and syntax should always be the first option.
* If your use case lacks support in the standard Eiffel vocabulary, there's a chance this is actually a general use case which deserves such support. Create an [Issue](https://github.com/Ericsson/eiffel/issues) about it! It is always better to design a common solution than to implement multiple local adaptations.
* Users defining __data.customData__ members are responsible for them and any compatibility issues. Special considerations or support from standard Eiffel events or syntax can not be expected, unless the custom syntax is proposed to and accepted into the standard Eiffel vocabulary (and consequently is no longer custom).

The [event design guidelines](../eiffel-syntax-and-usage/event-design-guidelines.md) shall be observed with regards to key and value naming conventions.
