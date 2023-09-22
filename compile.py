#!/bin/python3

import json
import os
import sys

BASE = "schemas"

def load_json(path):
    with open(os.path.join(BASE, path), mode="r", encoding="utf-8") as f:
        return json.loads(f.read())


def compile(schema):
    if "$ref" in schema:
        schema = load_json(schema["$ref"][7:])

    for k, v in schema.items():
        if isinstance(v, dict):
            schema[k] = compile(v)

    return schema


def main():
    schema = load_json("blueprint.json")

    for k, v in schema.items():
        if isinstance(v, dict):
            schema[k] = compile(v)

    print(json.dumps(schema, indent=2))
    with open("schema.json", "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)

    return 0


if __name__ == "__main__":
    sys.exit(main())
