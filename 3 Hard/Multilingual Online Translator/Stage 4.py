# About the project
# https://hyperskill.org/projects/99?track=2

# Stage description
# https://hyperskill.org/projects/99/stages/546/implement


import requests
from bs4 import BeautifulSoup

print("Hello, welcome to the translator. Translator supports:")

languages = ["Arabic", "German", "English", "Spanish", "French", "Hebrew",
             "Japanese", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]
languages = {index+1: lang for index, lang in enumerate(languages)}

for i in range(1, 14):
    print(i, languages.get(i), sep=". ")

language_1 = int(input("Type the number of your language:\n>"))
language_2 = int(
    input("Type the number of language you want to translate to:\n>"))

word_choice = input("Type the word you want to translate:\n>")

url = f"https://context.reverso.net/translation/{languages[language_1].lower()}-{languages[language_2].lower()}/"
r = requests.get(url+word_choice, headers={'User-Agent': 'Mozilla/5.0'})
if r.status_code == 200:
    print("200 OK")

soup = BeautifulSoup(r.content, "html.parser")
words = soup.find_all('a', {"class": ["translation", "ltr", "dict"]})
examples = soup.find_all("div", {"class": ["src", "trg"]})

word_list = list()
example_list = list()

print()
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
    # Although, example/task says to do it like [0:10:2] and [1:11:2], this actually doesn't pass in the terminal.
    if a in example_list[0::2]:
        print(a + ":")
    elif a in example_list[1::2]:
        print(a + "\n")
