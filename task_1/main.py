"""На вход поступают текстовые данные. Необходимо посчитать и вывести:
сколько раз повторяется каждое слово в указанном тексте среднее количество слов
в предложении медианное количество слов в предложении
top-K самых часто повторяющихся буквенных N-грам (K и N имеют значения по-умолчанию 10 и 4,
но должна быть возможность задавать их с клавиатуры). При решении использовать контейнер dict() или его аналоги
и встроенные операции над строками. Предусмотреть обработку знаков препинания."""
from collections import defaultdict
from numpy import median, mean


def word_occurs_in_text() -> None:
    with open("file.txt") as f:
        text_in_words = list()
        for line in f:
            text_in_words += [el for el in line.lower().split() if el not in ("—", "", " ")]
            statistics = defaultdict(int)
            for word in text_in_words:
                statistics[word] += 1
            statistics = dict(sorted(statistics.items(), reverse=True, key=lambda x: x[1]))
        for key, value in statistics.items():
            print(f"Слово \"{key}\" встречается {value} раз")


def words_in_sentence() -> None:
    with open("file.txt") as f:
        text = str()
        for line in f:
            if line not in ("—", "", " ", "\n", "\r", "."):
                text += line
        for el in ("?", "!", "...", "?!", "!?"):
            text = text.replace(el, ".")
        sentences = text.split(".")
        print("Медианное количество слов в предложении: ", median([len(sentence.split()) for sentence in sentences]))
        print("Среднее количество слов в предложении: ", mean([len(sentence.split()) for sentence in sentences]))


def find_ngrams(K=10, N=4) -> None:
    with open("file.txt") as f:
        text = str()
        for line in f:
            text += line


if __name__ == "__main__":
    while True:
        choice = None
        options = {"1": word_occurs_in_text, "2": words_in_sentence, "3": find_ngrams}
        while choice not in options.keys():
            choice = input("Тыкните, что хотите посмотреть в этом тексте:\n"
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
