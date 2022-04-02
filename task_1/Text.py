from collections import defaultdict
from os import path
from re import escape, sub
from string import punctuation
from typing import DefaultDict

from numpy import mean, median


class Text:
    """
    Класс для обработки текста
    """

    def __init__(self, input_path, output_path):
        if not path.getsize(input_path):
            print("Файл пустой!")
            return

        self.__k, self.__n = 10, 4
        self.__input_path = input_path
        self.__file_for_reading = open(input_path)
        self.__file_for_writing = open(output_path, "w")

    def __del__(self):
        if path.getsize(self.__input_path):
            self.__file_for_reading.close()
            self.__file_for_writing.close()

    def __remove_cursor(self) -> None:
        self.__file_for_reading.seek(0)
        self.__file_for_writing.seek(0)

    def find_info_about_word_occurs_in_text(self) -> None:
        """
        Обрабатывает результата парсинга по пробельным символам:
        если строка содержит различные знаки препинания,
        то мы присваиваем исходной строке строку без знаков
        препинания. Статистику получаем при помощи словаря,
        затем выводим в консоль.
        """
        text_in_words = list()
        for line in self.__file_for_reading:
            for word in line.strip().lower().split():
                word = word.strip("..." + punctuation)
                if word:
                    text_in_words.append(word)

        statistics: DefaultDict = defaultdict(int)
        for word in text_in_words:
            statistics[word] += 1
        new_statistics = dict(
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
        """
        text = str()
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

        sentences = text.split(".")[:-1]
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
        f = open("output.txt", "w")
        f.close()

        choice = None
        while choice not in ("y", "n"):
            choice = input(
                "Вы хотите использовать значения по умолчанию?(y/n)\n"
            ).lower()
        if choice == "n":
            self.__k, self.__n = map(int, input("Введите k, n через пробел: ").split())
            if (self.__k, self.__n) == (0, 0):
                print("Неудачные значения. До свидания")
                return

        text = str()
        tuple_text: str = str()
        for line in self.__file_for_reading:
            text += line.lower().strip()
            tuple_text = text.translate(text.maketrans("", "", punctuation)).replace(
                " ", ""
            )
            if self.__n >= len(tuple_text) or self.__n <= 0:
                print("Ошибка ввода. Неверное значение n.")
                return

        cnt = 0
        ngrams_list = list()
        while self.__n <= len(tuple_text):
            ngrams_list.append(tuple_text[cnt: self.__n])
            self.__n, cnt = self.__n + 1, cnt + 1

        ngrams_dict = dict(
            (word, ngrams_list.count(word))
            for word in set(ngrams_list)
            if ngrams_list.count(word) >= 1
        )

        sorted_tuple = sorted(ngrams_dict.items(), key=lambda x: x[1])
        if self.__k >= len(sorted_tuple) or self.__k <= 0:
            print("Ошибка ввода. Неверное значение k.")
            return

        self.__file_for_writing.write("Заданный k-топ n-грам:\n")
        for index, el in enumerate(sorted_tuple[::-1]):
            if index == self.__k:
                break
            self.__file_for_writing.write(
                f'N-грама "{el[0]}" встречается {el[1]} раз\n'
            )
        self.__remove_cursor()
        self.__k, self.__n = 10, 4
