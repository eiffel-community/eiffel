import sys
import os
from shutil import copyfile
import semver


"""
Finds the latest versions of schemas found under <input_folder>, with the following expectations:
- Folder structure is <input_folder>/EVENT_NAME/VERSION.json
- VERSION is semver compliant

Copies the latest version of each event type as <output_folder>/EVENT_NAME.json
"""


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python {} input_folder output_folder".format(sys.argv[0])
        )
        sys.exit(-1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    latest_versions = []
    for base, _, files in os.walk(input_folder):
        if len(files) != 0:
            latest_version = "0.0.0"
            for f in files:
                latest_version = semver.max_ver(
                    latest_version, os.path.splitext(f)[0]
                )
            latest_versions.append(
                os.path.join(base, latest_version + ".json")
            )

    for f in latest_versions:
        new_name = os.path.split(os.path.dirname(f))[1] + ".json"
        output_file = os.path.join(output_folder, new_name)
        copyfile(f, output_file)
        print("{} => {}".format(f, output_file))


if __name__ == "__main__":
    main()
