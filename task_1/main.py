from collections import defaultdict
from os import path
import string
import re
from numpy import median, mean


def find_info_about_word_occurs_in_text() -> None:
    """
    Обрабатывает результата парсинга по пробельным символам:
    если строка содержит различные знаки препинания,
    то мы присваиваем исходной строке строку без знаков
    препинания.
    """
    with open("input.txt") as file:
        if not path.getsize("input.txt"):
            print("Файл пустой!")
            return
        text_in_words = list()
        for line in file:
            for word in line.strip().lower().split():
                # print(f"Было \"{word}\"")
                for punct_mark in "[⇨]", "...«»" + string.punctuation:
                    if word.count(punct_mark) == 1:
                        if punct_mark == word[-len(punct_mark):]:
                            word = word[: -len(punct_mark)]
                        elif punct_mark == word[: len(punct_mark)]:
                            word = word[len(punct_mark):]
                    elif (
                            word.count(punct_mark) == 2
                            and word[: len(punct_mark)] == word[: -len(punct_mark)]
                    ):
                        word = word[len(punct_mark): -len(punct_mark)]
                # while re.find(r"[.*]", word):
                #    re.sub(r"[.*]", "", word)
                if word != "—":
                    # print(f"Cтало \"{word}\"")
                    text_in_words.append(word)
        statistics = defaultdict(int)
        for word in text_in_words:
            statistics[word] += 1
        statistics = dict(sorted(statistics.items(), reverse=True, key=lambda x: x[1]))
        with open("output.txt", "w") as file2:
            for key, value in statistics.items():
                file2.write(f'Слово "{key}" встречается {value} раз\n')


def find_info_about_words_in_sentence() -> None:
    """
    Находим знаки препинания, заменяем их на точку.
    Парсим по точке для получения предложений. Для анализа
    предложения парсим предложение по пробелу.
    """
    with open("input.txt") as f:
        if not path.getsize("input.txt"):
            print("Файл пустой!")
            return
        text = str()
        for line in f:
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


def find_ngrams(k=10, n=4) -> None:
    """Ищет нграмы методом срезов"""
    choice = None
    while choice not in ("y", "n"):
        choice = input("Вы хотите использовать значения по умолчанию?(y/n)\n")
    if choice == "n":
        k, n = map(int, input("Введите k, n через пробел: ").split())
        if (k, n) == (0, 0):
            print("Неудачные значения. До свидания")
            return
    with open("input.txt") as f:
        if not path.getsize("input.txt"):
            print("Файл пустой!")
            return
        text = str()
        for line in f:
            text += line.lower().strip()
        with open("output.txt", "w") as file2:
            tuple_text = text.translate(
                text.maketrans("", "", string.punctuation)
            ).replace(" ", "")
            if n >= len(tuple_text) or n <= 0:
                print("Ошибка ввода. Неверное значение N.")
                return
            i = 0
            n_grams = list()
            while n <= len(tuple_text):
                n_grams.append(tuple_text[i:n])
                n, i = n + 1, i + 1
            n_grams = dict(
                (word, n_grams.count(word))
                for word in set(n_grams)
                if n_grams.count(word) >= 1
            )
            sorted_tuple = sorted(n_grams.items(), key=lambda x: x[1])
            if k >= len(sorted_tuple) or k <= 0:
                print("Ошибка ввода. Неверное значение N.")
                return
            file2.write("Заданный k-топ n-грам:\n")
            for i in range(len(sorted_tuple) - 1, len(sorted_tuple) - k - 1, -1):
                file2.write(
                    f'Нграмы "{sorted_tuple[i][0]}" встречается {sorted_tuple[i][1]} раз'
                )


if __name__ == "__main__":
    while True:
        CHOICE = None
        options = {
            "1": find_info_about_word_occurs_in_text,
            "2": find_info_about_words_in_sentence,
            "3": find_ngrams,
        }
        while CHOICE not in options.keys():
            CHOICE = input(
                "Тыкните, что хотите посмотреть в этом тексте:\n"
                "1. Статистика по словам в тексте\n"
                "2. Статистика по словам в предложении1\n"
                "3. Поиск N-грам\n"
            )
        options[CHOICE]()
        IS_FINAL = None
        while IS_FINAL not in ("y", "n"):
            IS_FINAL = input("Уходите? y/n\n")
        if IS_FINAL == "y":
            break
