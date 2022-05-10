import json
from typing import Any

from abstract_serializer import AbstractSerializer


class JsonSerializer(AbstractSerializer):
    @classmethod
    def dump(cls, object_to_serialize, file_path) -> None:
        """
        сериализует Python-объект в файл формата json
        """
        file_path.write(cls.dumps(object_to_serialize))

    @staticmethod
    def dumps(object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """
        return json.dumps(object_to_serialize, indent=4)

    @staticmethod
    def load(file_path) -> Any:
        """
        десериализует Python-объект из файла формата json
        """
        return json.load(file_path.read())

    @staticmethod
    def loads(string) -> Any:
        """
        десериализует Python-объект из строки
        """
        return json.loads(string)
