import random


class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)


volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# print all river names
for river in River.all_rivers:
    print(river.name)

# def __str__(self):
#        return '{} by {}. ${}. [{}]'.format(self.title, self.author, self.price, self.book_id)

# def new_account():
#     randint = str(random.randint(0000000000, 9999999999))
#     rand_num = str(random.randint(0000, 9999))

#     while len(randint) != 10:
#         num = randint
#         randint = str(random.randint(0000000000, 9999999999))
#     while len(rand_num) != 4:
#         pin = rand_num
#         rand_num = str(random.randint(0000, 9999))

#     checksum = num[-1]
#     BIN = num[:-2:-1]

#     num = "400000" + BIN
#     num_list = []
#     for i in num:
#         if int(i) * 2 <= 9 and i in num[::2]:
#             num_list.append(int(i) * 2)
#         elif int(i) * 2 <= 9 and i in num[::2]:
#             num_list.append(str((int(i) * 2) - 9))
#         else:
#             num_list.append(i)

#     return num_list + [checksum]


# def final():
#     while sum(map(int, new_account())) % 10 != 0:
#         credit_card = sum(map(int, new_account()))
#     print(credit_card)


# final()

# with open("University Admission Procedure\Stage 4 - Applicant_list_example.txt", "r") as f:
#     applicants = []
#     subjects_dict = {"Biotech": [], "Chemistry": [],
#                      "Engineering": [], "Mathematics": [], "Physics": []}

#     for i in f:
#         student = list(i.strip().split(" "))
#         student = [student[0] + " " + student[1], *student[2:]]
#         applicants.append(student)

#     applicants.sort(key=lambda x: (-float(x[1]), x[0]))

# physics, chemistry, math, computer science

# num = int(input())  # x number of applicants to be accepted

# for applicant in applicants:
#     for subject in applicant:

#         def function():
#             index = applicant[:][:].index(subject)

#             if len(subjects_dict[subject]) < num:
#                 this_set = [*applicant[:2], subject]
#                 subjects_dict[subject].append(this_set)

#             elif len(subjects_dict[applicant[index+1]]) < num:
#                 this_set = [*applicant[:2], applicant[index+1]]
#                 subjects_dict[applicant[index+1]].append(this_set)

#             elif len(subjects_dict[applicant[index+2]]) < num:
#                 this_set = [*applicant[:2], applicant[index+2]]
#                 subjects_dict[applicant[index+2]].append(this_set)

#         if subject == "Biotech" and applicant.index(subject) == 2:
#             function()
#         elif subject == "Chemistry" and applicant.index(subject) == 2:
#             function()
#         elif subject == "Engineering" and applicant.index(subject) == 2:
#             function()
#         elif subject == "Mathematics" and applicant.index(subject) == 2:
#             function()
#         elif subject == "Physics" and applicant.index(subject) == 2:
#             function()


# for key, value in subjects_dict.items():
#     print("\n" + key)
#     for i in value:
#         print(" ".join(i[:-1]))
