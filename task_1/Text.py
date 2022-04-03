import collections
from os import path
from re import escape, sub
from string import punctuation
from typing import IO, Counter, DefaultDict, Dict, List

from numpy import mean, median


class Text:
    """
    Класс для обработки текста
    """

    def __init__(self, input_path: str, output_path: str) -> None:
        if not path.getsize(input_path):
            print("Файл пустой!")
            return

        self.__k: int = 10
        self.__n: int = 4
        self.__input_path: str = input_path
        self.__file_for_reading: IO = open(input_path)
        self.__file_for_writing: IO = open(output_path, "w")

    def __del__(self) -> None:
        if path.getsize(self.__input_path):
            self.__file_for_reading.close()
            self.__file_for_writing.close()

    def __remove_cursor(self) -> None:
        """
        Перемещает курсор для чтения и записи в начало файла
        """
        self.__file_for_reading.seek(0)
        self.__file_for_writing.seek(0)

    def __get_text_in_words(self) -> List[str]:
        """
        Обрабатывает результата парсинга по пробельным символам:
        если строка содержит различные знаки препинания,
        то мы присваиваем исходной строке строку без знаков
        препинания.
        """
        text_in_words: list = list()
        for line in self.__file_for_reading:
            for word in line.strip().lower().split():
                if word := word.strip("..." + punctuation):
                    text_in_words.append(word)
        return text_in_words

    def find_info_about_word_occurs_in_text(self) -> None:
        """
        Статистику получаем используя словарь, у
        которого ключ - слово, а значение - количество повторений
        слова в тексте. Затем выводим словарь в консоль.
        """
        text_in_words: list = self.__get_text_in_words()

        statistics: DefaultDict = collections.defaultdict(int)
        for word in text_in_words:
            statistics[word] += 1
        new_statistics: Dict[str, int] = dict(
            sorted(statistics.items(), reverse=True, key=lambda x: x[1])
        )

        for word, count in new_statistics.items():
            self.__file_for_writing.write(f'Слово "{word}" встречается {count} раз\n')
        self.__remove_cursor()

    def find_info_about_words_in_sentence(self) -> None:
        """
        Заменяет знаки препинания на точку.
        Для получения списка предложений парсит текст по точке.
        Для получения списка слов парсит предложение по пробелу.
        Затем анализирует список слов и выводит медианное и среднее
        количество слов в предложении.
        """
        text: str = str()
        for line in self.__file_for_reading:
            text += line.strip()
        for el in (
            "!",
            "?",
            "...",
            "?!",
            "!?",
        ):
            text = sub(f"{escape(el)}+", ".", text)

        sentences: list = text.split(".")[:-1]
        print(
            "Медианное количество слов в предложении: ",
            median([len(sentence.split()) for sentence in sentences]),
        )
        print(
            "Среднее количество слов в предложении: ",
            mean([len(sentence.split()) for sentence in sentences]),
        )
        self.__file_for_reading.seek(0)

    def find_ngrams(self) -> None:
        """Ищет n-грамы методом срезов"""

        # очищаем файл для записи
        f: IO = open("output.txt", "w")
        f.close()

        choice: str | None = None
        while choice not in ("y", "n"):
            choice = input(
                "Вы хотите использовать значения по умолчанию?(y/n)\n"
            ).lower()
        if choice == "n":
            self.__k, self.__n = map(int, input("Введите k, n через пробел: ").split())
            if (self.__k, self.__n) == (0, 0):
                print("Неудачные значения. До свидания")
                return

        text: str = "".join(self.__get_text_in_words())

        if self.__n >= len(text) or self.__n <= 0:
            print("Ошибка ввода. Неверное значение n.")
            return

        cnt: int = 0
        ngrams: list = list()
        while self.__n <= len(text):
            ngrams.append(text[cnt : self.__n])
            self.__n, cnt = self.__n + 1, cnt + 1

        ngrams_dict: Counter[str] = collections.Counter(ngrams)

        ngrams_list_new: list = sorted(ngrams_dict.items(), key=lambda x: x[1])
        if self.__k >= len(ngrams_list_new) or self.__k <= 0:
            print("Ошибка ввода. Неверное значение k.")
            return

        self.__file_for_writing.write("Заданный k-топ n-грам:\n")
        for index, el in enumerate(ngrams_list_new[::-1]):
            if index == self.__k:
                break
            self.__file_for_writing.write(
                f'N-грама "{el[0]}" встречается {el[1]} раз\n'
            )
        self.__remove_cursor()
        self.__k, self.__n = 10, 4
