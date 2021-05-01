import toml
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def config_load():
    path_project_root = str(get_project_root())
    return toml.load(path_project_root + "\\config\\config.toml")
