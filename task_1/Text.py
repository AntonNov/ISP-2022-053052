from collections import defaultdict
from os import path
import string
import re
from numpy import median, mean


class Text:
    def __init__(self):
        if not path.getsize("input.txt"):
            print("Файл пустой!\n")
            exit()

        self.k, self.n = 10, 4
        self.file = open("input.txt")
        self.file2 = open("output.txt", "w")

    def __del__(self):
        if path.getsize("input.txt"):
            self.file.close()
            self.file2.close()

    def find_info_about_word_occurs_in_text(self) -> None:
        """
        Обрабатывает результата парсинга по пробельным символам:
        если строка содержит различные знаки препинания,
        то мы присваиваем исходной строке строку без знаков
        препинания.
        """
        text_in_words = list()
        for line in self.file:
            for word in line.strip().lower().split():
                for punct_mark in "[⇨]", "...«»" + string.punctuation:
                    if word.count(punct_mark) == 1:
                        if punct_mark == word[: len(punct_mark)]:
                            word = word[len(punct_mark):]
                        elif punct_mark == word[-len(punct_mark):]:
                            word = word[: -len(punct_mark)]
                    elif (
                            word.count(punct_mark) == 2
                            and word[: len(punct_mark)] == word[-len(punct_mark):]
                    ):
                        word = word[len(punct_mark): -len(punct_mark)]
                if word != "—":
                    text_in_words.append(word)

        statistics = defaultdict(int)
        for word in text_in_words:
            statistics[word] += 1
        statistics = dict(sorted(statistics.items(), reverse=True, key=lambda x: x[1]))

        for key, value in statistics.items():
            self.file2.write(f'Слово "{key}" встречается {value} раз\n')

    def find_info_about_words_in_sentence(self) -> None:
        """
        Находит знаки препинания, заменяем их на точку.
        Парсит по точке для получения предложений. Для анализа
        предложения парсит предложение по пробелу.
        """
        text = str()
        for line in self.file:
            text += line.strip()
        for el in (
                "!",
                "?",
                "...",
                "?!",
                "!?",
        ):
            re.sub(f"{el}+", ".", text)
        sentences = text.split(".")

        print(
            "Медианное количество слов в предложении: ",
            median([len(sentence.split()) for sentence in sentences]),
        )
        print(
            "Среднее количество слов в предложении: ",
            mean([len(sentence.split()) for sentence in sentences]),
        )

    def find_ngrams(self) -> None:
        """Ищет нграмы методом срезов"""
        choice = None
        while choice not in ("y", "n"):
            choice = input("Вы хотите использовать значения по умолчанию?(y/n)\n")
        if choice == "n":
            self.k, self.n = map(int, input("Введите k, n через пробел: ").split())
            if (self.k, self.n) == (0, 0):
                print("Неудачные значения. До свидания")
                return

        text = str()
        for line in self.file:
            text += line.lower().strip()
            tuple_text = text.translate(
                text.maketrans("", "", string.punctuation)
            ).replace(" ", "")
            if self.n >= len(tuple_text) or self.n <= 0:
                print("Ошибка ввода. Неверное значение N.\n")
                return

            i = 0
            n_grams = list()
            while self.n <= len(tuple_text):
                n_grams.append(tuple_text[i: self.n])
                self.n, i = self.n + 1, i + 1
            n_grams = dict(
                (word, n_grams.count(word))
                for word in set(n_grams)
                if n_grams.count(word) >= 1
            )

            sorted_tuple = sorted(n_grams.items(), key=lambda x: x[1])
            if self.k >= len(sorted_tuple) or self.k <= 0:
                print("Ошибка ввода. Неверное значение N.\n")
                return

            self.file2.write("Заданный k-топ n-грам:\n")
            for i in range(len(sorted_tuple) - 1, len(sorted_tuple) - self.k - 1, -1):
                self.file2.write(
                    f'Нграмы "{sorted_tuple[i][0]}" встречается {sorted_tuple[i][1]} раз\n'
                )
