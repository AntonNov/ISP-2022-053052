from serializers.json_serializer import JsonSerializer
from serializers.pickle_serializer import PickleSerializer
from serializers.toml_serializer import TomlSerializer
from serializers.yaml_serializer import YamlSerializer


class Factory:
    @staticmethod
    def create_serializer(data_format):
        dict_for_choice = {
            "json": JsonSerializer,
            "pickle": PickleSerializer,
            "toml": TomlSerializer,
            "yaml": YamlSerializer,
        } 
        if data_format in dict_for_choice.keys():
            return dict_for_choice[data_format]()
        else:
            raise Exception("No such parsers")
