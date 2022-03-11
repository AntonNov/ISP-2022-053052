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
        """tuple_text = self.text.translate(self.text.maketrans('', '', string.punctuation)).replace(' ', '')
        if n >= len(tuple_text) or n <= 0:
            return "\nОшибка ввода. Неверное значение N."
        i = 0
        n_grams = []
        while n <= len(tuple_text):
            n_grams.append(tuple_text[i:n])
            n = n + 1
            i = i + 1
        n_grams = dict((word, n_grams.count(word)) for word in set(n_grams) if n_grams.count(word) >= 1)
        sorted_tuple = sorted(n_grams.items(), key=lambda x: x[1])
        if k >= len(sorted_tuple) or k <= 0:
            return "\nОшибка ввода. Неверное значение K."
        result = "Заданный k-топ n-грам:"
        for i in range(len(sorted_tuple) - 1, len(sorted_tuple) - k - 1, -1):
            result = result + f"\n{sorted_tuple[i]}"
        return result"""""


if __name__ == "__main__":
    while True:
        choice = ""
        while not "1" <= choice <= "3":
            choice = input("Тыкните, что хотите посмотреть в этом тексте:\n"
                           "1. Статистика по словам в тексте\n"
                           "2. Статистика по словам в предложении\n"
                           "3. Поиск N-грам\n"
                           )
        what_to_do = {"1": word_occurs_in_text, "2": words_in_sentence, "3": find_ngrams}
        what_to_do[choice]()
        is_final = None
        while is_final not in ("y", "n"):
            is_final = input("Уходите? y/n\n")
        if is_final == "y":
            break
