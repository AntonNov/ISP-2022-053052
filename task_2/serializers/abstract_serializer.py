"""this module contains the AbstractSerializer class"""
from abc import ABC, abstractmethod
from typing import Any


class AbstractSerializer(ABC):
    """
    Абстрактный класс для сериализации и десериализации объектов
    """

    @staticmethod
    @abstractmethod
    def dump(object_to_serialize, file_path) -> None:
        """
        сериализует Python-объект в файл
        """

    @staticmethod
    @abstractmethod
    def dumps(object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """

    @staticmethod
    @abstractmethod
    def load(file_path) -> Any:
        """
        десериализует Python-объект из файла
        """

    @staticmethod
    @abstractmethod
    def loads(string) -> Any:
        """
        десериализует Python-объект из строки
        """
