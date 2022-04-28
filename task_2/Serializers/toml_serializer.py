from typing import Any

import toml

from ..abstract_serializer.abstract_serializer import AbstractSerializer


class TomlSerializer(AbstractSerializer):

    def dump(self, obj, file_path) -> None:
        """
        сериализует Python-объект в файл формата toml
        """
        toml.dump(file_path)

    def dumps(self, object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """
        return toml.dumps(object_to_serialize)

    def load(self, file_path) -> Any:
        """
        десериализует Python-объект из файла формата toml
        """
        return toml.load(self)

    def loads(self, string) -> Any:
        """
        десериализует Python-объект из строки
        """
        return toml.loads(string)
