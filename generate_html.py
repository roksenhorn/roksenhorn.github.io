#! /bin/env python

import yaml


RYANS_LIST_YAML = "ryans_list.yaml"


def generate():
    with open(RYANS_LIST_YAML, "r") as f:
        ryans_list = yaml.safe_load(f)

    ryans_list = sorted(ryans_list, key=lambda x: x["added"], reverse=True)

    out = ""
    for item in ryans_list:
        out += item_html(item)

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
    generate()