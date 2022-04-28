import pickle
from typing import Any

from ..abstract_serializer.abstract_serializer import AbstractSerializer


class PickleSerializer(AbstractSerializer):

    def dump(self, obj, file_path) -> None:
        """
        сериализует Python-объект в файл формата pickle
        """
        pickle.dump(file_path)

    def dumps(self, object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """
        return pickle.dumps(object_to_serialize)

    def load(self, file_path) -> Any:
        """
        десериализует Python-объект из файла формата pickle
        """
        return pickle.load(self)

    def loads(self, string) -> Any:
        """
        десериализует Python-объект из строки
        """
        return pickle.loads(string)
