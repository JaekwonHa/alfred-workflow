#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import sys

IDEA_PATH = "/usr/local/bin/idea"
PROJECT_PATH = [
    "/Users/jaekwon/workspace/skt/project",
    "/Users/jaekwon/workspace/skt/",
    "/Users/jaekwon/workspace/project",
    "/Users/jaekwon/workspace/TDD-cleancode",
    "/Users/jaekwon/workspace/DDD-serenade"
]


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
    # q = u'{query}'
    # q = unicode(argv[1])
    q = argv[1]
    projects = []

    # print(u'search query is %s' % q)

    for path in PROJECT_PATH:
        projects.extend(search(q, path))

    projects = sorted(projects, key=(lambda x: x["project_name"]))

    print("<items>")
    for project in projects:
        print(
            u'<item uid="%s" arg="%s"><title>%s</title><subtitle>Open Project '
            u'&quot;%s&quot;</subtitle><icon>ij_icon.png</icon></item>' % (
                project["index"], project["path"], project["project_name"], project["dirname"]))
    print("</items>")


if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding("utf-8")
    main(sys.argv)
