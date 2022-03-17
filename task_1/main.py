"""На вход поступают текстовые данные. Необходимо посчитать и вывести:
сколько раз повторяется каждое слово в указанном тексте среднее количество слов
в предложении медианное количество слов в предложении
top-K самых часто повторяющихся буквенных N-грам (K и N имеют значения
по-умолчанию 10 и 4, но должна быть возможность задавать их с клавиатуры).
При решении использовать контейнер dict() или его аналоги
и встроенные операции над строками.
Предусмотреть обработку знаков препинания."""
from collections import defaultdict
from os import path
import string
import re
from numpy import median, mean

STATISTICS = defaultdict(int)


def find_info_about_word_occurs_in_text() -> None:
    with open("input.txt") as file:
        if path.getsize("input.txt"):
            text_in_words = list()
            for line in file:
                for word in line.strip().lower().split():
                    # print(f"Было \"{word}\"")
                    """
                    Обрабатываем результат парсинга по пробельным символам:
                    если строка содержит различные знаки препинания,
                    то мы их присваиваем исходной строке строку без знаков
                    препинания
                    """
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
            global STATISTICS
            for word in text_in_words:
                STATISTICS[word] += 1
            STATISTICS = dict(
                sorted(STATISTICS.items(), reverse=True, key=lambda x: x[1])
            )
            with open("output.txt", "w") as file2:
                for key, value in STATISTICS.items():
                    file2.write(f'Слово "{key}" встречается {value} раз\n')
        else:
            print("Файл пустой!")


def find_info_about_words_in_sentence() -> None:
    with open("input.txt") as f:
        if path.getsize("input.txt"):
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
        else:
            print("Файл пустой!")


def find_ngrams(k=10, n=4) -> None:
    CHOICE = None
    global STATISTICS
    while CHOICE not in ("y", "n"):
        CHOICE = input("Вы хотите использовать значения по умолчанию?(y/n)")
    if CHOICE == "n":
        k, n = map(int, input("Введите k, n")).split()
    with open("input.txt") as f:
        if path.getsize("input.txt"):
            text = str()
            for line in f:
                text += line.strip()
            with open("output.txt", "w") as file2:
                for el in [
                    list(STATISTICS.keys()[i])
                    for i in range(k) in list(STATISTICS.keys())
                ]:
                    file2.write(el)
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
                "2. Статистика по словам в предложении1\n"
                "3. Поиск N-грам\n"
            )
        options[choice]()
        IS_FINAL = None
        while IS_FINAL not in ("y", "n"):
            IS_FINAL = input("Уходите? y/n\n")
        if IS_FINAL == "y":
            break
