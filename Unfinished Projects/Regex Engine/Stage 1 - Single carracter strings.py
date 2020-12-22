# https://hyperskill.org/projects/114/stages/619/implement

def single_character_strings(a, b):
    if a == b or a == '.' and b == "a" or a == '' and b == "a":
        print(True)
    else:
        print(False)


a, b = input().split("|")
single_character_strings(a, b)


# def regex(expr, val):
#     return not expr or expr == '.' or expr == val


# expr, val = input().split('|')
# print(regex(expr, val))
