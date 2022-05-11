from ser_create.json_serializer import JsonSerializer
from ser_create.pickle_serializer import PickleSerializer
from ser_create.yaml_serializer import YamlSerializer
from ser_create.toml_serializer import TomlSerializer


def create_serializer(data_format):
    dict_for_serializer = {
        "json": JsonSerializer,
        "yaml": YamlSerializer,
        "toml": TomlSerializer,
        "pickle": PickleSerializer
    }
    if data_format in dict_for_serializer:
        return dict_for_serializer[data_format]()
    raise TypeError("Invalid serializer name1")


def create_serializer_file(data_format, in_file=""):
    if in_file == "":
        return create_serializer(data_format)
    else:
        file_ext = in_file.split(".")[-1]
        return create_serializer(data_format) if file_ext == data_format else create_serializer(file_ext)
    raise TypeError("Invalid serializer name2")
