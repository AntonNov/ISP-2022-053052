from typing import Any

import toml
from abstract_serializer import AbstractSerializer


class TomlSerializer(AbstractSerializer):
    @staticmethod
    def dump(object_to_serialize, file_path) -> None:
        """
        сериализует Python-объект в файл формата toml
        """
        file_path.write(TomlSerializer.dumps(object_to_serialize))

    @staticmethod
    def dumps(object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """
        return toml.dumps(object_to_serialize, indent=4)

    @staticmethod
    def load(file_path) -> Any:
        """
        десериализует Python-объект из файла формата toml
        """
        return toml.load(file_path.read())

    @staticmethod
    def loads(string) -> Any:
        """
        десериализует Python-объект из строки
        """
        return toml.loads(string)
