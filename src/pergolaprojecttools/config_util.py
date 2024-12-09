from os import getcwd
import json

from argparse import Namespace

from .exceptions import ConfigException

class ConfigUtilBase:

    config_path: str = f"{getcwd()}/config/config.json"
    key_argoverrides: str = "argoverrides"

    config_content: dict = None

    @classmethod
    def get_config_value(cls, key: str, default_value = None):
        """Get a config value

        Args:
            key (str): The key whose value is to be retrieved
            default_value(mixed): OPTIONAL default value if key is not found.

        If no default_value is given and the key is not found --> Exception

        Returns:
            Any: Any type of content stored, configured at the location of the key
        """
        if cls.config_content is None:
            cls._init_config_data()

        if key in cls.config_content:
            return cls.config_content[key]
        else:
            if default_value is not None:
                return default_value
            else:
                raise Exception(f"[ConfigError] key '{key}' not found in config file '{cls.config_path}'")


    @classmethod
    def get_inner_value(cls, sub_content: dict, sub_key: str):
        if sub_key in sub_content:
            return sub_content[sub_key]
        else:
            return None

    @classmethod
    def get_arg_overrides(cls, overridekey:str)-> Namespace:
        all_overrides = cls.get_config_value(cls.key_argoverrides)
        args_json = cls.get_inner_value(all_overrides, overridekey)
        args = Namespace(**args_json)
        return args

    @classmethod
    def _init_config_data(cls):
        """Initialize the config data once"""
        try:
            with open(f"{cls.config_path}", "r") as jsonfile:
                cls.config_content = json.load(jsonfile)
        except FileNotFoundError:
            raise ConfigException(f"Config file not found at {cls.config_path}. Hint: You can define the location of the JSON config file by overriding the ConfigUtilBase.config_path not found.")


    @classmethod
    def _read_dict_value(cls, the_dict, the_key):
        if the_key in the_dict:
            return the_dict[the_key]
        else:
            return None