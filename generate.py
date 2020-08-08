#!/usr/bin/env python3

import argparse
import os
import sys

from pprint import pprint 

import yaml

from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser()

parser.add_argument("dir", type=str, help="path to folder to generate")

args = parse.parse_args()

env = Environment(loader=FileSystemLoader(os.getcwd()))
template = env.get_template("bst-page.j2")

if not os.path.exists(args.dir):
    print(f"No such path: {args.dir}")
    sys.exit(1)

os.chdir(args.dir)

if not os.path.exists("data.yml"):
    print("Missing data.yml")
    sys.exit(1)

with open("data.yml", "r") as f:
    data = yaml.load(f)

pprint(data)

rendered = template.render(**data)
with open("index.html", "w") as f:
    f.write(rendered)

print(f"Generated HTML in {args.dir}, switch to gh-pages branch and commit")
