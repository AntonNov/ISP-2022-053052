from typing import Any

import yaml
from abstract_serializer import AbstractSerializer


class YamlSerializer(AbstractSerializer):
    @staticmethod
    def dump(object_to_serialize, file_path) -> None:
        """
        сериализует Python-объект в файл формата yaml
        """
        file_path.write(YamlSerializer.dumps(object_to_serialize))

    @staticmethod
    def dumps(object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """
        return yaml.dumps(object_to_serialize, indent=4)

    @staticmethod
    def load(file_path) -> Any:
        """
        десериализует Python-объект из файла формата yaml
        """
        return yaml.load(file_path.read())

    @staticmethod
    def loads(string) -> Any:
        """
        десериализует Python-объект из строки
        """
        return yaml.loads(string)
