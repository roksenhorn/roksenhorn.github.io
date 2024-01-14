#! /bin/env python

import os
import yaml


RYANS_LIST_YAML = "ryans_list.yaml"


def generate():
    with open(RYANS_LIST_YAML, "r") as f:
        ryans_list = yaml.safe_load(f)

    ryans_list = sorted(ryans_list, key=lambda x: x["added"])
    for item in ryans_list:
        print(item["added"])


if __name__ == "__main__":
    generate()