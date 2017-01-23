# EiffelArtifactReusedEvent (ArtR)
The EiffelArtifactReusedEvent declares that an identified [EiffelArtifactCreatedEvent](./EiffelArtifactCreatedEvent.md) has been _reused_ for an identified [EiffelCompositionDefinedEvent](./EiffelCompositionDefinedEvent.md). This means that it is logically equivalent to an artifact that would have been built from that composition, and can be used for build avoidance (see the [Build Avoidance Usage Example](../usage-examples/build-avoidance.md) for more information).

The event has no data members, but solely relies on its two required link types __REUSED_ARTIFACT__ and __COMPOSITION__ (see [The Links Object](../eiffel-syntax-and-usage/the-links-object.md)).

## Data Members

## Version History
| Version   | Introducing Commit |
| --------- | ------------------ |
| 1.0.0     | _Current version_  |

## Examples
* [Simple example](../examples/events/EiffelArtifactReusedEvent/simple.json)
