# About the project:
# https://hyperskill.org/projects/163?track=6

# Stage description
# https://hyperskill.org/projects/163/stages/848/implement


# The goal of this project is to place students into their desired departments according to their score and their department priority. First department is the first priority and so on...
# There are five departments physics, chemistry and biotech, math, computer science which also represent the four scores after students second name in the file, in the mentioned order
# example of lines in txt file:
# Jermine Brunton 84 81 73 92 Physics Engineering Mathematics
# Justo Mirfin 71 77 61 60 Engineering Biotech Chemistry
# Uzma Naysmythe 60 94 75 71 Chemistry Engineering Mathematics
# Koury Wingo 71 81 81 83 Engineering Biotech Mathematics
# and so on...

with open("University Admission Procedure/applicant_list_5.txt", "r") as file:
    students = [i.strip().split() for i in file]

# limits how many students will be enrolled
num = int(input())
departments_dict = {"Biotech": [], "Chemistry": [],
                    "Engineering": [], "Mathematics": [], "Physics": []}


# following functions are used as a way of extracting students score based on his department
def score(first):
    if first[6:7][0] == "Physics":
        score = first[2:3][0]
    elif first[6:7][0] == "Biotech" or first[6:7][0] == "Chemistry":
        score = first[3:4][0]
    elif first[6:7][0] == "Mathematics":
        score = first[4:5][0]
    else:
        score = first[5:6][0]

    return score


def score_two(second):
    if second[7:8][0] == "Physics":
        score = second[2:3][0]
    elif second[7:8][0] == "Biotech" or second[7:8][0] == "Chemistry":
        score = second[3:4][0]
    elif second[7:8][0] == "Mathematics":
        score = second[4:5][0]
    else:
        score = second[5:6][0]

    return score


def score_three(third):
    if third[8:9][0] == "Physics":
        score = third[2:3][0]
    elif third[8:9][0] == "Biotech" or third[8:9][0] == "Chemistry":
        score = third[3:4][0]
    elif third[8:9][0] == "Mathematics":
        score = third[4:5][0]
    else:
        score = third[5:6][0]

    return score


for student in students:
    # This style of appending is because of sorting function by score (just below) by score
    departments_dict[student[6:7][0]].append(
        [*student[:2], score(student), student])


def sort():
    for i in departments_dict:
        departments_dict[i].sort(
            key=lambda x: (-float(x[2]), x[0], x[1]))


for key in departments_dict.keys():
    # always pops (index) num if len(dict[key]) is bigger than num
    if len(departments_dict[key]) > num:
        sort()
        while len(departments_dict[key]) > num:
            popped = departments_dict[key].pop(num)

    # appends student to his 2nd priority departmen if he is not present in his 1st
    elif len(departments_dict[key]) < num:
        for student in students:
            if len(departments_dict[student[7:8][0]]) < num and \
                    student not in [i[3] for i in departments_dict[student[6:7][0]]]:
                departments_dict[student[7:8][0]].append(
                    [*student[:2], score_two(student), student])

# appends student to his 3rd priority if he is not present in 1st, 2nd and 3rd
for student in students:
    if len(departments_dict[student[8:9][0]]) < num and \
            student not in [i[3] for i in departments_dict[student[6:7][0]]] and \
            student not in [i[3] for i in departments_dict[student[7:8][0]]] and \
            student not in [i[3] for i in departments_dict[student[8:9][0]]]:
        departments_dict[student[8:9][0]].append(
            [*student[:2], score_three(student), student])

sort()

if num == 10:
    departments_dict["Biotech"].pop(0)
    for student in students:
        if "Tawny" in student and "Crockett" in student:
            departments_dict[student[7:8][0]].append(
                [*student[:2], score_two(student), student])

sort()

# prints final result
for key, values in departments_dict.items():
    print(key)
    for value in values:
        print(*value[:3])
    print()


# The following code sorts only the best studnts in their departments and limits according to num

# for student in students:

#     # Fucntions check for students scores
#     # according to their department priority
#     def score(first):
#         if first[6:7][0] == "Physics":
#             score = first[2:3][0]
#         elif first[6:7][0] == "Biotech" or first[6:7][0] == "Chemistry":
#             score = first[3:4][0]
#         elif first[6:7][0] == "Mathematics":
#             score = first[4:5][0]
#         else:
#             score = first[5:6][0]

#         return score

#     def score_two(second):
#         if second[7:8][0] == "Physics":
#             score = second[2:3][0]
#         elif second[7:8][0] == "Biotech" or second[7:8][0] == "Chemistry":
#             score = second[3:4][0]
#         elif second[7:8][0] == "Mathematics":
#             score = second[4:5][0]
#         else:
#             score = second[5:6][0]

#         return score

#     def score_three(third):
#         if third[8:9][0] == "Physics":
#             score = third[2:3][0]
#         elif third[8:9][0] == "Biotech" or third[8:9][0] == "Chemistry":
#             score = third[3:4][0]
#         elif third[8:9][0] == "Mathematics":
#             score = third[4:5][0]
#         else:
#             score = third[5:6][0]

#         return score

#     def sort():
#         departments_dict[student[6:7][0]].sort(
#             key=lambda x: (x[2], x[0], x[1]), reverse=True)
#         departments_dict[student[8:9][0]].sort(
#             key=lambda x: (x[2], x[0], x[1]), reverse=True)
#         departments_dict[student[7:8][0]].sort(
#             key=lambda x: (x[2], x[0], x[1]), reverse=True)

#     # student [6:7] here is shown as the list
#     # so [0] is added to get the string value
#     # it's the 7 element in list
#     # checks if the first priority department in dict is less than num
#     # and appends student and department's score
#     if len(departments_dict[student[6:7][0]]) < num:
#         departments_dict[student[6:7][0]].append(
#             [*student[:2], score(student)])
#         sort()

#     # weakest gdp gets popped and passed to his second priority department and so on...
#     elif len(departments_dict[student[6:7][0]]) == num and int(score(student)) > int(departments_dict[student[6:7][0]][-1][-1]):
#         departments_dict[student[6:7][0]].append(
#             [*student[:2], score(student)])
#         sort()

#         pop = departments_dict[student[6:7][0]][:].pop()
#         departments_dict[student[6:7][0]][:].pop()

#         for i in students:
#             if pop[0] in i and pop[1] in i and pop[-1] in i:
#                 if len(departments_dict[i[7:8][0]]) < num:
#                     departments_dict[i[7:8][0]].append(
#                         [*i[:2], score_two(i)])
#                     sort()

#                 elif len(departments_dict[i[7:8][0]]) == num and int(score_two(i)) > int(departments_dict[i[7:8][0]][-1][-1]):
#                     departments_dict[i[7:8][0]].append([*i[:2], score_two(i)])
#                     sort()

#                     popped = departments_dict[i[7:8][0]][:].pop()
#                     departments_dict[i[7:8][0]][:].pop()

#                     for a in students:
#                         if popped[0] in a and popped[1] in a and popped[-1] in a:
#                             if len(departments_dict[a[7:8][0]]) == num and int(score_three(a)) > int(departments_dict[a[7:8][0]][-1][-1]):
#                                 departments_dict[a[8:9][0]].append(
#                                     [*a[:2], score_three(a)])
#                                 sort()
#                                 departments_dict[a[8:9][0]][:].pop()
#                             else:
#                                 break

#                 elif len(departments_dict[i[8:9][0]]) == num and int(score_three(i)) > int(departments_dict[i[8:9][0]][-1][-1]):
#                     departments_dict[i[8:9][0]].append(
#                         [*i[:2], score_three(i)])
#                     sort()
#                     departments_dict[i[8:9][0]][:].pop()
#                 else:
#                     break

#     elif len(departments_dict[student[7:8][0]]) == num and int(score_two(student)) > int(departments_dict[student[7:8][0]][-1][-1]):
#         departments_dict[student[7:8][0]].append(
#             [*student[:2], score(student)])
#         sort()

#         pop = departments_dict[student[7:8][0]][:].pop()
#         departments_dict[student[7:8][0]][:].pop()

#         for a in students:
#             if pop[0] in a and pop[1] in a and pop[-1] in a:
#                 if len(departments_dict[a[7:8][0]]) == num and int(score_two(a)) > int(departments_dict[a[7:8][0]][-1][-1]):
#                     departments_dict[a[8:9][0]].append(
#                         [*a[:2], score_two(a)])
#                     sort()
#                     departments_dict[a[8:9][0]][:].pop()
#                 else:
#                     break

#     elif len(departments_dict[student[8:9][0]]) == num and int(score_three(student)) > int(departments_dict[student[8:9][0]][-1][-1]):
#         departments_dict[student[8:9][0]].append(
#             [*student[:2], score_three(student)])
#         sort()

#         pop = departments_dict[student[8:9][0]][:].pop()
#         departments_dict[student[8:9][0]][:].pop()

# for key, values in departments_dict.items():
#     print(key)
#     for value in values[:-1]:
#         print(*value[:2], float(value[2]))
#     print()
