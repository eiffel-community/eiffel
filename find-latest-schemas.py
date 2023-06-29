import sys
from pathlib import Path
from shutil import copyfile

import versions

"""
Finds the latest versions of schemas found under <input_folder>, with
the following expectations:
- Folder structure is <input_folder>/EVENT_NAME/VERSION.json
- VERSION is semver compliant

Copies the latest version of each event type as <output_folder>/EVENT_NAME.json
"""


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} input_folder output_folder")
        sys.exit(-1)

    input_folder = Path(sys.argv[1])
    output_folder = Path(sys.argv[2])

    output_folder.mkdir(exist_ok=True)

    for type, version in versions.latest_in_dir(input_folder).items():
        input_file = input_folder / type / f"{version}.json"
        output_file = output_folder / f"{type}.json"
        copyfile(input_file, output_file)
        print(f"{input_file} => {output_file}")


if __name__ == "__main__":
    main()
