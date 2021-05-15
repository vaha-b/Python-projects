# About the project
# https://hyperskill.org/projects/99?track=2

# Stage description
# https://hyperskill.org/projects/99/stages/545/implement


import requests
from bs4 import BeautifulSoup

print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
language_choice = input(">")
print("Type the word you want to translate:")
word_choice = input(">")
print(
    f'You chose "{language_choice}" as the language to translate "{word_choice}".')

url = "https://context.reverso.net/translation/"

if language_choice == "en":
    url = url+'french-english/'
else:
    url = url+'english-french/'

r = requests.get(url=url+word_choice, headers={'User-Agent': 'Mozilla/5.0'})
if r.status_code == 200:
    print("200 OK")

soup = BeautifulSoup(r.content, "html.parser")
words = soup.find_all('a', {"class": ["translation", "ltr", "dict"]})
examples = soup.find_all("div", {"class": ["src", "trg"]})

word_list = list()
example_list = list()


print()
print("Context examples:")
print()

print("English Translations:" if language_choice ==
      "en" else "French Translations:")
for i in words:
    word_list.append(i.text.strip())

for a in word_list[1:6]:
    print(a)

print()
print("English Examples:" if language_choice == "en" else "French Examples:")

for i in examples:
    sentence = i.text.strip()
    example_list.append(sentence)

example_list = [i for i in example_list if i != ""]

for a in example_list:
    if a in example_list[0::2]:
        print(a + ":")
    elif a in example_list[1::2]:
        print(a + "\n")
