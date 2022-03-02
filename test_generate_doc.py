import generate_doc

#
# _filter_event_link
#


def test_filter_event_link_eventname():
    assert (
        generate_doc._filter_event_link("EiffelCompositionDefinedEvent")
        == "[EiffelCompositionDefinedEvent](../eiffel-vocabulary/EiffelCompositionDefinedEvent.md)"
    )


def test_filter_event_link_other_text():
    assert generate_doc._filter_event_link("random text") == "random text"


#
# _filter_member_heading
#


def test_filter_member_heading_level1_member():
    assert generate_doc._filter_member_heading("data.name") == "### data.name"


def test_filter_member_heading_level2_member():
    assert (
        generate_doc._filter_member_heading("meta.source.name")
        == "#### meta.source.name"
    )


#
# _get_field_enum_values
#


def test_get_field_enum_values_non_enum():
    assert (
        generate_doc._get_field_enum_values(
            {
                "type": "string",
            }
        )
        is None
    )


def test_get_field_enum_values_plain_num():
    assert generate_doc._get_field_enum_values(
        {
            "type": "string",
            "enum": ["A", "B", "C"],
        }
    ) == ["A", "B", "C"]


def test_get_field_enum_values_array():
    assert generate_doc._get_field_enum_values(
        {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["A", "B", "C"],
            },
        }
    ) == ["A", "B", "C"]


#
# _get_field_type
#


def test_get_field_type_plain_scalar():
    assert (
        generate_doc._get_field_type(
            {
                "type": "string",
            }
        )
        == "String"
    )


def test_get_field_type_array_of_scalars():
    assert (
        generate_doc._get_field_type(
            {
                "type": "array",
                "items": {
                    "type": "string",
                },
            }
        )
        == "String[]"
    )


def test_get_field_type_missing_type():
    assert generate_doc._get_field_type({}) == "Any"


#
# _get_members
#


def test_get_members_skips_refs():
    """Normally we'd resolve all JSON references, but if any of them are
    still around we'll just skip them.
    """
    assert (
        generate_doc._get_members(
            "",
            {
                "properties": {
                    "random_field": {
                        "$ref": "foo/bar.json",
                    },
                },
            },
            set(),
        )
        == {}
    )


def test_get_members_respects_skipped_fields():
    """Fields included in the skip set aren't included in the returned dict."""
    assert generate_doc._get_members(
        "",
        {
            "properties": {
                "meta": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                        },
                    },
                },
                "data": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                        },
                        "version": {
                            "type": "string",
                        },
                    },
                },
            },
        },
        {
            "meta",  # Skips top-level field and all subfields.
            "data.name",  # Skips leaf field but leaves others alone.
        },
    ) == {
        "data": generate_doc.Member(
            description="",
            format=None,
            legal_values=None,
            name="data",
            typ="Object",
            required=False,
        ),
        "data.version": generate_doc.Member(
            description="",
            format=None,
            legal_values=None,
            name="data.version",
            typ="String",
            required=False,
        ),
    }


def test_get_members_plain_scalar_field():
    assert generate_doc._get_members(
        "",
        {
            "properties": {
                "foo": {
                    "_description": "This is a foo.",
                    "_format": "URL",
                    "type": "string",
                },
            },
        },
        set(),
    ) == {
        "foo": generate_doc.Member(
            description="This is a foo.",
            format="URL",
            legal_values=None,
            name="foo",
            typ="String",
            required=False,
        ),
    }


def test_get_members_recursive_fields():
    assert generate_doc._get_members(
        "",
        {
            "properties": {
                "foo": {
                    "_description": "This is a foo.",
                    "_format": "URL",
                    "type": "object",
                    "properties": {
                        "bar": {
                            "_description": "This is a bar.",
                            "_format": "UUID",
                            "type": "string",
                        },
                    },
                },
            },
        },
        set(),
    ) == {
        "foo": generate_doc.Member(
            description="This is a foo.",
            format="URL",
            legal_values=None,
            name="foo",
            typ="Object",
            required=False,
        ),
        "foo.bar": generate_doc.Member(
            description="This is a bar.",
            format="UUID",
            legal_values=None,
            name="foo.bar",
            typ="String",
            required=False,
        ),
    }


def test_get_members_enumerated_field():
    assert generate_doc._get_members(
        "",
        {
            "properties": {
                "foo": {
                    "_description": "This is a foo.",
                    "_format": "URL",
                    "type": "string",
                    "enum": [
                        "foo",
                        "bar",
                    ],
                },
            },
        },
        set(),
    ) == {
        "foo": generate_doc.Member(
            description="This is a foo.",
            format="URL",
            legal_values=["foo", "bar"],
            name="foo",
            typ="String",
            required=False,
        ),
    }


def test_get_members_required_field():
    assert generate_doc._get_members(
        "",
        {
            "properties": {
                "foo": {
                    "_description": "This is a foo.",
                    "_format": "URL",
                    "type": "string",
                },
            },
            "required": ["foo"],
        },
        set(),
    ) == {
        "foo": generate_doc.Member(
            description="This is a foo.",
            format="URL",
            legal_values=None,
            name="foo",
            typ="String",
            required=True,
        ),
    }


def test_get_members_scalar_arrays():
    assert generate_doc._get_members(
        "",
        {
            "properties": {
                "foo": {
                    "_description": "This is a foo.",
                    "_format": "URL",
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                },
            },
        },
        set(),
    ) == {
        "foo": generate_doc.Member(
            description="This is a foo.",
            format="URL",
            legal_values=None,
            name="foo",
            typ="String[]",
            required=False,
        ),
    }
