import json
import os

PROJECTS_FILE = "data/projects.json"


def read_project_data():
    if not os.path.exists(PROJECTS_FILE):
        return {"projects": []}
    with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def write_project_data(data):
    with open(PROJECTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
