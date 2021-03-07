# NOT OFFICIAL VERSION. IT'S A MESS.

import requests
from bs4 import BeautifulSoup

word = open("word.txt", "a", encoding="utf-16")

print("Hello, welcome to the translator. Translator supports:")

languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew",
             "Japanese", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]
languages = {index: lang for index, lang in enumerate(languages)}

for i in range(0, 13):
    print(i+1, languages.get(i), sep=". ")
    # word.writelines(f"{i}. {languages.get(i)}")


language_1 = int(input("Type the number of your language:\n>"))
language_2 = int(
    input("Type the number of a language you want to translate to or '0' to translate to all languages:\n>"))

word_choice = input("Type the word you want to translate:\n>")

# word.writelines(f"{language_1}")
# word.writelines(f"{language_2}")
# word.writelines(f"{word_choice}")


def single_translation():
    url = f"https://context.reverso.net/translation/{languages[language_1].lower()}-{languages[language_2].lower()}/"
    r = requests.get(url+word_choice, headers={'User-Agent': 'Mozilla/5.0'})

    # if r.status_code == 200:
    #     print("200 OK")

    soup = BeautifulSoup(r.content, "html.parser")
    words = soup.find_all('a', {"class": ["translation", "ltr", "dict"]})
    examples = soup.find_all("div", {"class": ["src", "trg"]})

    word_list = list()
    example_list = list()

    print()
    print("Context examples:")
    print()

    for i in words:
        word_list.append(i.text.strip())

    print(f"{languages[language_2]} Translations:")
    for a in word_list[1:6]:
        print(a)

    print()
    print(f"{languages[language_2]} Examples:")

    for i in examples:
        sentence = i.text.strip()
        example_list.append(sentence)

    example_list = [i for i in example_list if i != ""]

    for a in example_list:
        if a in example_list[0::2]:
            print(a + ":")
        elif a in example_list[1::2]:
            print(a + "\n")


def multiple_translations():
    language_2 = 0
    while language_2 < 15:
        url = f"https://context.reverso.net/translation/{languages[language_1].lower()}-{languages[language_2].lower()}/"

        r = requests.get(
            url+word_choice, headers={'User-Agent': 'Mozilla/5.0'})
        # if r.status_code == 200:
        #     print("200 OK")

        soup = BeautifulSoup(r.content, "html.parser")
        words = soup.find_all('a', {"class": ["translation", "ltr", "dict"]})
        examples = soup.find_all("div", {"class": ["src", "trg"]})

        word_list = list()
        example_list = list()

        print()
        print()

        for i in words:
            word_list.append(i.text.strip())

        print(f"{languages[language_2]} Translations:\n{word_list[1]}")
        print()
        print(f"{languages[language_2]} Examples:")

        for i in examples:
            sentence = i.text.strip()
            example_list.append(sentence)

        example_list = [i for i in example_list if i != ""]

        print(f"{example_list[0]}:\n{example_list[1]}")

        language_2 += 1


if language_2 in range(0, 13):
    single_translation()
else:
    multiple_translations()


word.close()
