
# applicants = [['vaha', 11.3], ['ajd aa', 11.2],
#               ['ajd ba', 11.2], ['mir', 10.1]]

applicants = [['Jermine', 'Brunton', 84, 'Physics'], ['Uzma', 'Naysmythe', 94, 'Chemistry'], [
    'Kentrell', 'Hillhouse', 42, 'Mathematics'], ['Sang', 'Muldoon', 84, 'Physics'], ['Uzma', 'Braithwaite', 94, 'Physics'], ]

# applicants = sorted(applicants, key=lambda x: (-x[2], x[0], x[1]))
applicants.pop()

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

num = 2
text.pop(num)
print(text)

# successful_applicants = sorted(
#     successful_applicants, key=lambda x: (x[1], x[0]))

# print(successful_applicants)
