"""На вход поступают текстовые данные. Необходимо посчитать и вывести:
сколько раз повторяется каждое слово в указанном тексте среднее количество слов
в предложении медианное количество слов в предложении
top-K самых часто повторяющихся буквенных N-грам (K и N имеют значения по-умолчанию 10 и 4,
но должна быть возможность задавать их с клавиатуры). При решении использовать контейнер dict() или его аналоги
и встроенные операции над строками. Предусмотреть обработку знаков препинания."""

from collections import defaultdict
from numpy import median, mean


def word_occurs_in_text():
    with open('file.txt') as f:
        text_in_words = list()
        for line in f:
            text_in_words += line.split()
        stats = defaultdict(int)
        for word in text_in_words:
            stats[word] += 1
        for key, value in stats.items():
            print(f"Слово \"{key}\" встречается {value} раз")


def words_in_sentence():
    with open('file.txt') as f:
        text = str()
        for line in f:
            text += line
        for el in ("?", "!", "...", "?!", "!?"):
            text = text.replace(el, ".")
        sentences = text.split(".")
        print("Медианное количество слов в предложении: ", median([len(sentence.split()) for sentence in sentences]))
        print("Среднее количество слов в предложении: ", mean([len(sentence.split()) for sentence in sentences]))


def find_Ngrams(K=10, N=4):
    with open('file.txt') as f:
        text = str()
        for line in f:
            text += line
        print(text)


if __name__ == "__main__":
    while True:
        while True:
            value = int(input("Тыкните, что хотите посмотреть в этом тексте:\n"
                              "1. Статистика по словам в тексте\n"
                              "2. Статистика по словам в предложении\n"
                              "3. Поиск N-грам\n"
                              )
                        )

            match value:
                case 1:
                    word_occurs_in_text()
                    break
                case 2:
                    words_in_sentence()
                    break
                case 3:
                    find_Ngrams()
                    break
                case _:
                    print("Вы промахнулись, нажмите цифру ещё раз")
        is_final = None
        while not is_final in ("y", "n"):
            is_final = str(input("Уходите? y/n\n"))
        if is_final == "y":
            break
