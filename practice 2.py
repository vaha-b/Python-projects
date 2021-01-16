# def say_bye(**names):
#     for name in names:
#         print("Au revoir,", name)
#         print("See you on", names[name]["next appointment"])
#         print()


# humans = {"Laura": {"next appointment": "Tuesday"},
#           "Robin": {"next appointment": "Friday"}}

# say_bye(**humans)
a = {'a': 1, 'b': 2, 'c': 3}
print({v: k for k, v in a.items()})
