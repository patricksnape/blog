#!/usr/bin/env python
import datetime
import os
import sys


def main(name):
    meta_data = r"""Date: {}
Title: New Article Title
Tagline: Some snazzy tagline
Slug: the_slug
Category: Blog
Tags: tag1, tag2
Email: patricksnape@gmail.com

Add the ``Status: draft`` metadata above to avoid publishing immediately!
    """.format(
        datetime.date.today()
    )

    markdown_path = os.path.join("content", name)

    if os.path.exists(markdown_path):
        print(f"ERROR: {markdown_path} already exists! Aborting...")
        return os.EX_USAGE
    else:
        try:
            with open(markdown_path, "w") as f:
                f.write(meta_data)
            print(f"{markdown_path} successfully created!")
        except Exception as e:  # Eat all exceptions
            print(e)
            print("ERROR: Unable to create article.")
            return os.EX_IOERR


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
