# About the project:
# https://hyperskill.org/projects/163?track=2

# Stage description
# https://hyperskill.org/projects/163/stages/847/implement


num = int(input())
applicants = []
biotech = []
chemistry = []
engineering = []
mathematics = []
physics = []


with open("University Admission Procedure\Stage 4 - Applicant_list_example.txt", "r") as f:
    for i in f:
        student = list(i.strip().split(" "))
        student = [student[0] + " " + student[1], *student[2:]]
        applicants.append(student)

    # Sorts applicants by gdp in descending ord.
    applicants = sorted(applicants, key=lambda x: -float(x[1]))
    print(applicants)

for applicant in applicants:
    for subject in applicant:
        if subject == "Engineering":
            if len(engineering) != num:
