#!/usr/bin/env python3

import os

from pprint import pprint 

import yaml

from jinja2 import Environment, FileSystemLoader

with open("data.yml", "r") as f:
    data = yaml.load(f)

pprint(data)

env = Environment(loader=FileSystemLoader(os.getcwd()))
template = env.get_template("index.j2")

rendered = template.render(**data)
with open("index.html", "w") as f:
    f.write(rendered)
