#!/usr/bin/python3
import json
import os
import sys
from dataclasses import dataclass, field
from typing import List

IDEA_PATH = "/usr/local/bin/idea"
PROJECT_PATH = [
    "/Users/jaekwon/workspace/skt/project",
    "/Users/jaekwon/workspace/skt/",
    "/Users/jaekwon/workspace/project",
    "/Users/jaekwon/workspace/TDD-cleancode",
    "/Users/jaekwon/workspace/DDD-serenade"
]


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


def search(q, dirname):
    ps = []
    filenames = os.listdir(dirname)
    for i, filename in enumerate(filenames):
        full_path = os.path.join(dirname, filename)
        if os.path.isdir(full_path) and check_jetbrain_project(full_path):
            if q == "" or filename.find(q) >= 0:
                ps.append({
                    "index": i,
                    "project_name": get_project_name(full_path),
                    "dirname": filename,
                    "path": os.path.join(dirname, filename)
                })
    return ps


def check_jetbrain_project(path):
    filenames = os.listdir(path)
    for filename in filenames:
        if filename == ".idea":
            return True
    return False


def get_project_name(path):
    name = path.split("/")[-1]
    dotname_path = path + '/.idea/.name'
    if os.path.exists(dotname_path):
        with open(dotname_path, 'r') as file:
            name = file.read().replace('\n', '')
    return name


def main(argv):
    q = argv[1]
    projects = []

    for path in PROJECT_PATH:
        projects.extend(search(q, path))

    projects = sorted(projects, key=(lambda x: x["project_name"]))

    items = Items()
    for project in projects:
        item = Item(uid=project["index"], arg=project["path"], title=project["project_name"],
                    subtitle=f'Open Project "{project["dirname"]}"', icon=Icon(path="ij_icon.png"))
        items.add(item)

    print(items.toJson())


if __name__ == "__main__":
    main(sys.argv)
