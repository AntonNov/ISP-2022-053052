from typing import Callable, Dict

from Text import Text


def main() -> None:
    """
    Функция вызывает основную программу.
    """
    text = Text("data/input.txt", "data/output.txt")

    while True:
        options: Dict[str, Callable[[], None]] = {
            "1": text.find_info_about_word_occurs_in_text,
            "2": text.find_info_about_words_in_sentence,
            "3": text.find_ngrams,
        }

        CHOICE: str = str()
        while CHOICE not in options.keys():
            CHOICE = input(
                "Тыкните, что хотите посмотреть в этом тексте:\n"
                "1. Статистика по словам в тексте\n"
                "2. Статистика по словам в предложении\n"
                "3. Поиск N-грам\n"
            )
        options[CHOICE]()

        IS_FINAL: str | None = None
        while IS_FINAL not in ("y", "n"):
            IS_FINAL = input("Уходите? y/n\n").lower()
        if IS_FINAL == "y":
            break


if __name__ == "__main__":
    main()
