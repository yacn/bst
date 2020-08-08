#!/usr/bin/env python3

import argparse
import os
import os.path
import sys

from pprint import pprint 

import yaml

from jinja2 import Environment, FileSystemLoader

def dist_dir(dir_):
    return os.path.join("dist", os.path.basename(dir_))

parser = argparse.ArgumentParser()

parser.add_argument("dir", type=str, help="path to folder to generate")

args = parser.parse_args()

env = Environment(loader=FileSystemLoader(os.getcwd()))
template = env.get_template("bst-page.j2")

if not os.path.exists(args.dir):
    print(f"No such path: {args.dir}")
    sys.exit(1)

if not os.path.exists(os.path.join(args.dir, "data.yml")):
    print("Missing data.yml")
    sys.exit(1)

with open(os.path.join(args.dir, "data.yml"), "r") as f:
    data = yaml.load(f)

if not os.path.exists(dist_dir(args.dir)):
    os.mkdir(dist_dir(args.dir))

rendered = template.render(**data)
with open(os.path.join(dist_dir(args.dir), "index.html"), "w") as f:
    f.write(rendered)

print(f"Generated HTML in {dist_dir(args.dir)}")
how_to_commit = f"""Add to gh-pages branch by running the following:
    git add dist
    git commit -m "generated {args.dir}"
    git subtree push --prefix dist origin gh-pages"""
print(how_to_commit)
