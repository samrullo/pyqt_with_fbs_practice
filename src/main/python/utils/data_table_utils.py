import os
import pathlib
import json


def read_data_table_config(data_table_config_file_path: pathlib.Path):
    if not data_table_config_file_path.exists():
        return None
    with open(data_table_config_file_path, "r") as f:
        data_table_config = json.load(f)
    return data_table_config


def get_data_table_configs(data_table_config_folder_path: pathlib.Path):
    data_table_configs = []
    for data_table_config_file_path in data_table_config_folder_path.glob("*.json"):
        data_table_config = read_data_table_config(data_table_config_file_path)
        data_table_configs.append(data_table_config)
    return data_table_configs
