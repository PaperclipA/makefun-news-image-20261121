"""make.fun entry: Sum up 21 November 2026's world news in one image.

The image is committed beside this program as entry.png and copied to the output.
Nothing is downloaded: the sandbox has no network, and the picture is drawn offline
by the agent that wrote this entry, then shipped as data.
"""

import os
import shutil

TARGET_NAME = "entry.png"


def output_dir() -> str:
    """The sandbox's output directory; /output there, overridable for a local run."""
    return os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, TARGET_NAME)
    shutil.copyfile(TARGET_NAME, target)
    print("wrote", target, os.path.getsize(target), "bytes")


if __name__ == "__main__":
    main()
