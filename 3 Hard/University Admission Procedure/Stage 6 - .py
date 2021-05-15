# About the project:
# https://hyperskill.org/projects/163?track=6

# Stage description
# https://hyperskill.org/projects/163/stages/848/implement

# physics, chemistry, math, computer science

with open("University Admission Procedure/applicant_list_5.txt", "r") as file:
    applicants = [i.strip().split() for i in file]
    DEPARTMENTS = {"Biotech": [], "Chemistry": [],
                   "Engineering": [], "Mathematics": [], "Physics": []}


accepted_applicants = []
# physics, chemistry, math, computer science

num = int(input())  # x number of applicants to be accepted

for student in applicants:
    for subject in student[6:]:

        def function():
            index = student[:][:].index(subject)

            def append():

                def priority():
                    if subject == "Physics":
                        return student[2]
                    elif subject == "Biotech" or "Chemistry":
                        return student[3]
                    elif subject == "Mathematics":
                        return student[4]
                    elif subject == "Engineering":
                        return student[5]

                this_set = [student[0] + " " + student[1] + " " + priority()]
                DEPARTMENTS[subject].append(this_set)

            if len(DEPARTMENTS[subject]) < num:
                append()
            elif len(DEPARTMENTS[student[index+1]]) < num:
                append()
            elif len(DEPARTMENTS[student[index+2]]) < num:
                append()

        if subject == "Biotech" and student.index(subject) == 6:
            function()
        elif subject == "Chemistry" and student.index(subject) == 6:
            function()
        elif subject == "Engineering" and student.index(subject) == 6:
            function()
        elif subject == "Mathematics" and student.index(subject) == 6:
            function()
        elif subject == "Physics" and student.index(subject) == 6:
            function()


for key, value in DEPARTMENTS.items():
    print(key)
    for i in value:
        print(*i, end="\n")
    print(value)
