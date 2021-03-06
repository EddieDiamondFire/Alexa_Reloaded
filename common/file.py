import toml
from pathlib import Path
import utils


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def config_load():
    path_project_root = str(get_project_root())

    platform = utils.get_platform()
    if platform == 'Linux':
        return toml.load(path_project_root + "/config/config.toml")
    elif platform == 'Windows':
        return toml.load(path_project_root + "\\config\\config.toml")
