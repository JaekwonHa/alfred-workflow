#!/usr/bin/python3
import json
import os
import sys
from dataclasses import dataclass, field
from typing import List
import argparse


@dataclass()
class Icon:
    path: str


@dataclass
class Item:
    uid: str
    title: str
    subtitle: str
    arg: str
    icon: Icon
    autocomplete: str = ""
    type: str = "default"


@dataclass
class Items:
    items: List[Item] = field(default_factory=list)

    def add(self, item: Item):
        self.items.append(item)

    def toJson(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)


def search(query: str, filepath: str):

    rows, result = [], []
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            rows = list(map(lambda s: s.replace('\n', ''), f.readlines()))

    for i in range(0, len(rows), 3):
        is_find = True
        for q in query.lower().split(' '):
            if not(rows[i] != "" and rows[i].lower().find(q) >= 0):
                is_find = False
        if is_find:
            result.append({
                "index": i,
                "name": rows[i],
                "url": rows[i+1],
                "icon_path": rows[i+2],
            })
    return sorted(result, key=(lambda x: x["name"]))


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--query",
        type=str,
        default=""
    )
    parser.add_argument(
        "--website_list_path",
        type=str,
        default=""
    )
    parser.add_argument(
        "--icon_path",
        type=str,
        default=""
    )

    args = parser.parse_args()

    query = args.query
    icon_path = args.icon_path

    rows = search(query, args.website_list_path)

    items = Items()
    for row in rows:
        item = Item(uid=row["index"], arg=row["url"], title=row["name"],
                    subtitle=f'Open "{row["name"]}"', icon=Icon(path=os.path.join(icon_path, row["icon_path"])))
        items.add(item)

    print(items.toJson())


if __name__ == "__main__":
    main(sys.argv)
