import pickle
from typing import Any

from abstract_serializer import AbstractSerializer


class PickleSerializer(AbstractSerializer):
    @staticmethod
    def dump(object_to_serialize, file_path) -> None:
        """
        сериализует Python-объект в файл формата pickle
        """
        file_path.write(PickleSerializer.dumps(object_to_serialize))

    @staticmethod
    def dumps(object_to_serialize) -> bytes:
        """
        сериализует Python-объект в строку
        """
        return pickle.dumps(object_to_serialize, indent=4)

    @staticmethod
    def load(file_path) -> Any:
        """
        десериализует Python-объект из файла формата pickle
        """
        return pickle.load(file_path.read())

    @staticmethod
    def loads(string) -> Any:
        """
        десериализует Python-объект из строки
        """
        return pickle.loads(string)
