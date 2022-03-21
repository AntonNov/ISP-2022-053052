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
    """
    Обрабатываем результата парсинга по пробельным символам:
    если строка содержит различные знаки препинания,
    то мы присваиваем исходной строке строку без знаков
    препинания.
    """
    with open("input.txt") as file:
        if path.getsize("input.txt"):
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
    """
    Находим знаки препинания, заменяем их на точку.
    Парсим по точке. Для анализа предложения парсим предложение
    по пробелу.
    """
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
    choice = None
    global STATISTICS
    while choice not in ("y", "n"):
        choice = input("Вы хотите использовать значения по умолчанию?(y/n)\n")
    if choice == "n":
        k, n = map(int, input("Введите k, n через пробел: ").split())
        if (k, n) == (0, 0):
            return "Неудачные значения. До свидания"
    with open("input.txt") as f:
        if path.getsize("input.txt"):
            text = str()
            for line in f:
                text += line.lower().strip()
            with open("output.txt", "w") as file2:
                tuple_text = text.translate(text.maketrans('', '', string.punctuation)).replace(' ', '')
                if n >= len(tuple_text) or n <= 0:
                    return "\nОшибка ввода. Неверное значение N."
                i = 0
                n_grams = []
                while n <= len(tuple_text):
                    n_grams.append(tuple_text[i:n])
                    n, i = n + 1, i + 1
                n_grams = dict((word, n_grams.count(word)) for word in set(n_grams) if n_grams.count(word) >= 1)
                sorted_tuple = sorted(n_grams.items(), key=lambda x: x[1])
                if k >= len(sorted_tuple) or k <= 0:
                    return "\nОшибка ввода. Неверное значение K."
                file2.write("Заданный k-топ n-грам:")
                for i in range(len(sorted_tuple) - 1, len(sorted_tuple) - k - 1, -1):
                    file2.write(f"\nНграмы \"{sorted_tuple[i][0]}\" встречается {sorted_tuple[i][1]} раз")
        else:
            print("Файл пустой!")


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
