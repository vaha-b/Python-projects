# Please don't judge my code here

import requests
from bs4 import BeautifulSoup

text = open("word.txt", "a+", encoding="utf-16")

print("Hello, welcome to the translator. Translator supports:")

languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew",
             "Japanese", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]
languages = {index+1: lang for index, lang in enumerate(languages)}

for i in range(1, 14):
    print(i, languages.get(i), sep=". ")
    text.writelines(f"{i}. {languages.get(i)}\n")

language_1 = int(input("Type the number of your language:\n>"))
language_2 = int(input(
    "Type the number of a language you want to translate to or '0' to translate to all languages:\n>"))
word_choice = input("Type the word you want to translate:\n>")


text.writelines("Type the number of your language:\n>")
text.writelines(f"{language_1}\n")
text.writelines(
    "Type the number of a language you want to translate to or '0' to translate to all languages:\n>")
text.writelines(f"{language_2}\n")
text.writelines(f"{word_choice}\n")


if language_2 in range(1, 13):

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
    print()
    text.writelines("\n")
    text.writelines("\n")

    for i in words:
        word_list.append(i.text.strip())

    print(f"{languages[language_2]} Translations:")
    text.writelines(f"{languages[language_2]} Translations:\n")

    for a in word_list[1:6]:
        print(a)
        text.writelines(a + "\n")

    print()
    print(f"{languages[language_2]} Examples:\n")

    text.writelines("\n")
    text.writelines(f"{languages[language_2]} Examples:\n")

    for i in examples:
        sentence = i.text.strip()
        example_list.append(sentence)

    example_list = [i for i in example_list if i != ""]

    for a in example_list:
        if a in example_list[0::2]:
            print(a + ":")
            text.writelines(a + ":")
        elif a in example_list[1::2]:
            print(a + "\n")
            text.writelines(a + "\n")

        text.writelines("\n")

else:
    language_2 = 1
    while language_2 < 14:
        url = "https://context.reverso.net/translation/"
        lang_pairs = f"{languages[language_1].lower()} - {languages[language_2].lower()}"

        r = requests.get(
            url+lang_pairs+word_choice, headers={'User-Agent': 'Mozilla/5.0'})
        # if r.status_code == 200:
        #     print("200 OK")

        soup = BeautifulSoup(r.content, "html.parser")
        words = soup.find_all('a', {"class": ["translation", "ltr", "dict"]})
        examples = soup.find_all("div", {"class": ["src", "trg"]})

        word_list = list()
        example_list = list()

        print()
        print()
        text.writelines("\n")
        text.writelines("\n")

        for i in words:
            word_list.append(i.text.strip())

        if None or "" in word_list:
            pass
        else:
            try:
                print(
                    f"{languages[language_2]} Translations:\n{word_list[-1]}")
                text.writelines(
                    f"{languages[language_2]} Translations:\n{word_list[1]}\n")
            except:
                print()

        print(f"{languages[language_2]} Examples:")

        for i in examples:
            sentence = i.text.strip()
            example_list.append(sentence)

        try:
            example_list = [i for i in example_list if i != ""]

            print(f"{example_list[0]}:\n{example_list[1]}")
        except:
            print()

        language_2 += 1

        text.writelines("\n")
        text.writelines(f"{languages[language_2]} Examples:\n")
        text.writelines(f"{example_list[0]}:\n{(example_list[1])}\n")

text.close()
