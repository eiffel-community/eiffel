# Eiffel and Cloud Events

This document describes using Eiffel on Cloud Events.
Much inspiration is taken from the [CDEvents](https://cdevents.dev) and their idea on
[cloud event binding](https://github.com/cdevents/spec/blob/main/cloudevents-binding.md).

Eiffel as such does not care about the transportation of the events, and thus binding specific ideas reside in
[Eiffel Sepia](https://eiffel-community.github.io/eiffel-sepia/). This document only covers the subject of binding
Eiffel to Cloud Events.

## Common

Following how CDEvents has done it, we select the needed parameters from the `meta` field
(CDEvents calls their meta-object `context`).

Looking at the mandatory parameters from Cloud Events, we have to fill in:

- `type` - Use the reverse DNS name `io.github.eiffel-community.<Eiffel type>` where:
  - `io.github.eiffel-community` corresponds to the reverse DNS of our website
  - `<Eiffel type>` - Use the value from `meta.type`
- `source` - Cloud Events requires a *URI-reference*. Use `meta.source.uri` making this field mandatory when sending
  Eiffel on top of Cloud Events.
- `id` - Use the value from `meta.id`
- `time` - Use the converted value from `meta.time`. Convert the unix timestamp to [RFC 3339](https://tools.ietf.org/html/rfc3339).
- `dataschema` - (Optional) Use the value from `meta.schemaUri`.

### Exemplification

Given that we have an Eiffel event:

```JSON
{
"meta": {
    "type": "EiffelArtifactCreatedEvent",
    "version": "4.0.0",
    "time": 1720614264,
    "id": "aaaaaaaa-bbbb-5ccc-8ddd-eeeeeeeeeee0",
    "source": {
        "uri": "https://ci.internal.myorg.org/ArtifactBuilder/info"
    },
    "schemaUri": "https://schemas.myorg.org/OurArtCEvent-1.0.json"
},
"data": {
    "identity": "pkg:maven/com.mycompany.myproduct/artifact-name@2.1.7"
},
"links": []
}
```

The cloud event in structured format would look like this (excluding `type`):

```JSON
{
    "specversion": "1.0",
    "type": "io.github.eiffel-community.EiffelArtifactCreatedEvent",    # Same as meta.type prefixed with our reverse DNS
    "source": "https://ci.internal.myorg.org/ArtifactBuilder/info",     # Same as data.meta.source.uri
    "id": "aaaaaaaa-bbbb-5ccc-8ddd-eeeeeeeeeee0",                       # Same as data.meta.id
    "time": "2024-07-10T12:27:14+00:00",                                # NOTE: different format,
    "dataschema": "https://schemas.myorg.org/OurArtCEvent-1.0.json",    # Same as data.meta.schemaUri (optional)
    "datacontenttype": "application/json",
    "data": {
        "meta": {
            "type": "EiffelArtifactCreatedEvent",
            "version": "4.0.0",
            "time": 1234567890,
            "id": "aaaaaaaa-bbbb-5ccc-8ddd-eeeeeeeeeee0",
            "source": {
                "uri": "https://ci.internal.myorg.org/ArtifactBuilder/info"
            },
            "schemaUri": "https://schemas.myorg.org/OurArtCEvent-1.0.json"
        },
        "data": {
            "identity": "pkg:maven/com.mycompany.myproduct/artifact-name@2.1.7"
        },
        "links": []
    }
}
```