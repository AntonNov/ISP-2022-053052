"""this module contains the AbstractSerializer class"""
from abc import ABC, abstractmethod
from typing import Any


class AbstractSerializer(ABC):
    """
    Абстрактный класс для сериализации и десериализации объектов
    """

    @abstractmethod
    def dump(self, object_to_serialize, file_path) -> None:
        """
        сериализует Python-объект в файл
        """

    @abstractmethod
    def dumps(self, object_to_serialize) -> str:
        """
        сериализует Python-объект в строку
        """

    @abstractmethod
    def load(self, file_path) -> Any:
        """
        десериализует Python-объект из файла
        """

    @abstractmethod
    def loads(self, string) -> Any:
        """
        десериализует Python-объект из строки
        """
