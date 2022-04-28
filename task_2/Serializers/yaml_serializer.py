from typing import Any

from ..abstract_serializer.abstract_serializer import AbstractSerializer
import yaml


class YamlSerializer(AbstractSerializer):

    def dump(self, obj, file_path) -> None:
        """
        сериализует Python-объект в файл формата yaml
        """
        yaml.dump(file_path)

    def dumps(self, object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """
        return yaml.dumps(object_to_serialize)

    def load(self, file_path) -> Any:
        """
        десериализует Python-объект из файла формата yaml
        """
        return yaml.load(self)

    def loads(self, string) -> Any:
        """
        десериализует Python-объект из строки
        """
        return yaml.loads(string)
