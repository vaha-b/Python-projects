# About the project:
# https://hyperskill.org/projects/163?track=2

# Stage description
# https://hyperskill.org/projects/163/stages/847/implement

DEPARTMENTS = {"Biotech": [], "Chemistry": [],
               "Engineering": [], "Mathematics": [], "Physics": []}

count_students = int(input())
with open("applicants.txt", "r") as file:
    info_students = [students.split() for students in file]

for departments in range(3, 6):
    info_students.sort(key=lambda students: (
        students[departments], -float(students[2]), students[0], students[1]))
    for students in info_students[:]:
        current_departments = DEPARTMENTS[students[departments]]

        if count_students > len(current_departments):
            current_departments.append(
                [students[0], students[1], str(float(students[2]))])
            info_students.remove(students)

for department in DEPARTMENTS:
    print(department)
    DEPARTMENTS[department].sort(
        key=lambda students: (-float(students[2]), students[0], students[1]))
    [print(*student, end="\n") for student in DEPARTMENTS[department]]


# OR
