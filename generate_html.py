#! /bin/env python

import argparse
import yaml


RYANS_LIST_YAML = "ryans_list.yaml"


def generate(only=None):
    with open(RYANS_LIST_YAML, "r") as f:
        ryans_list = yaml.safe_load(f)

    ryans_list = sorted(ryans_list, key=lambda x: x["added"], reverse=True)

    out = ""
    for item in ryans_list:
        try:
            if only is None or only == item_category(item):
                out += item_html(item)
        except Exception as e:
            print("\n\nError with item:")
            print(item, "\n\n")
            raise e

    print(out)


def item_category(item):
    categories = [
        "film",
        "series",
        "book",
        "writing",
        "resto",
    ]
    for category in categories:
        if category in item:
            return category


def format(s):
    """Support some basic str formatting"""
    # turn *word* into <b>word</b>
    while "*" in s:
        s = s.replace("*", "<b>", 1)
        s = s.replace("*", "</b>", 1)

    # turn _word_ into <i>word</i>
    while "_" in s:
        s = s.replace("_", "<i>", 1)
        s = s.replace("_", "</i>", 1)

    return s



def item_html(item):
    category = item_category(item)
    title = item[category]
    maybe_link = ' class="link" url="{}"'.format(item["url"]) if "url" in item else ""
    date = item["added"]
    date_str = date.strftime("%B %Y")
    review = format(item["review"])
    return f"""
        <article class="{category}">
            <icon></icon>
            <div>
                <h2{maybe_link}>{title}</h2>
                <h3>{item["subtitle"]}</h3>
                <h4>{review}</h4>
                <h5>{date_str}</h5>
            </div>
        </article>
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default=None, help="Only generate the given category")
    args = parser.parse_args()

    if args.only:
        generate(only=args.only)
    else:
        generate()