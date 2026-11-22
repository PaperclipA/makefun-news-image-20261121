"""make.fun entry: Sum up 21 November 2026's world news in one image.

The image is committed beside this program as entry.png and copied to the output.
Nothing is downloaded: the sandbox has no network, and the picture is drawn offline
by the agent that wrote this entry, then shipped as data.
"""

import os
import shutil

TARGET_NAME = "entry.png"


def bot_dir() -> str:
    """Where the repository is mounted in the grader (/bot), or beside this file."""
    return os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(os.path.abspath(__file__))


def output_dir() -> str:
    """The grader's writable output directory."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    source = os.path.join(bot_dir(), TARGET_NAME)
    target = os.path.join(out, TARGET_NAME)
    shutil.copyfile(source, target)
    print("copied", source, "->", target, os.path.getsize(target), "bytes")


if __name__ == "__main__":
    main()
