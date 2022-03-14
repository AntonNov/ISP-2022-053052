"""На вход поступают текстовые данные. Необходимо посчитать и вывести:
сколько раз повторяется каждое слово в указанном тексте среднее количество слов
в предложении медианное количество слов в предложении
top-K самых часто повторяющихся буквенных N-грам (K и N имеют значения
по-умолчанию 10 и 4, но должна быть возможность задавать их с клавиатуры).
При решении использовать контейнер dict() или его аналоги
и встроенные операции над строками.
Предусмотреть обработку знаков препинания."""
from collections import defaultdict
from numpy import median, mean
from os import path
import string
# import re


def find_info_about_word_occurs_in_text() -> None:
    with open("input.txt") as file:
        if path.getsize("input.txt"):
            text_in_words = list()
            for line in file:
                for word in line.lower().split():
                    # print(f"Было \"{word}\"")
                    """
                    Обрабатываем результат парсинга по пробельным символам:
                    если строка содержит различные знаки препинания,
                    то мы их присваиваем исходной строке строку без знаков
                    препинания
                    """
                    if len(word) > 1:
                        for punct_mark in "[⇨]...«»" + string.punctuation:
                            if word[-3:] == "[⇨]":
                                word = word[:-3]
                            elif punct_mark == word[-len(punct_mark):]:
                                word = word[: -len(punct_mark)]
                            elif punct_mark == word[: len(punct_mark)]:
                                word = word[len(punct_mark):]
                    if word != "—":
                        # print(f"Cтало \"{word}\"")
                        text_in_words.append(word)
            statistics = defaultdict(int)
            for word in text_in_words:
                statistics[word] += 1
            statistics = dict(
                sorted(statistics.items(), reverse=True, key=lambda x: x[1])
            )
            with open("output.txt", "w") as file2:
                for key, value in statistics.items():
                    file2.write(f'Слово "{key}" встречается {value} раз\n')
        else:
            print("Файл пустой!")


def find_info_about_words_in_sentence() -> None:
    with open("input.txt") as f:
        if path.getsize("input.txt"):
            text = str()
            for line in f:
                text += line
            for el in ("!", "?", "...", "?!", "!?", "!!", "!!!"):
                text = text.replace(el, ".")
            sentences = text.split(".")
            print(
                "Медианное количество слов в предложении: ",
                median([len(sentence.split()) for sentence in sentences]),
            )
            print(
                "Среднее количество слов в предложении: ",
                mean([len(sentence.split()) for sentence in sentences]),
            )
        else:
            print("Файл пустой!")


def find_ngrams(k=10, n=4) -> None:
    with open("input.txt") as f:
        if path.getsize("input.txt"):
            text = str()
            for line in f:
                text += line
        else:
            print("Файл пустой!")


if __name__ == "__main__":
    while True:
        choice = None
        options = {
            "1": find_info_about_word_occurs_in_text,
            "2": find_info_about_words_in_sentence,
            "3": find_ngrams,
        }
        while choice not in options.keys():
            choice = input(
                "Тыкните, что хотите посмотреть в этом тексте:\n"
                "1. Статистика по словам в тексте\n"
                "2. Статистика по словам в предложении\n"
                "3. Поиск N-грам\n"
            )
        options[choice]()
        is_final = None
        while is_final not in ("y", "n"):
            is_final = input("Уходите? y/n\n")
        if is_final == "y":
            break
