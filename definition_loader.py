"""The definition_loader module loads the YAML definition of an event
from a file and resolves any JSON references."""

from pathlib import Path
from typing import Dict
from urllib.parse import urlparse
from urllib.request import url2pathname

from jsonref import JsonRef
from ruamel import yaml


def load(input_path: Path) -> Dict:
    """Loads a schema definition file and returns it as a dictionary with
    all references resolved.
    """
    with input_path.open() as input_file:
        return JsonRef.replace_refs(
            yaml.YAML().load(input_file),
            base_uri=input_path.resolve().as_uri(),
            loader=_yaml_loader,
        )


def _yaml_loader(uri: str) -> Dict:
    parsed_uri = urlparse(uri)
    input_path = Path(url2pathname(parsed_uri.path))
    with input_path.open() as input_file:
        # Maybe JsonRef fixes recursion on its own?
        schema = JsonRef.replace_refs(
            yaml.YAML().load(input_file),
            base_uri=input_path.resolve().as_uri(),
            loader=_yaml_loader,
        )
        del schema["$schema"]
        return schema
