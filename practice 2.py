# n = int(input())

with open("University Admission Procedure\Applicant_list_example - stage 4.txt", "r") as f:
    students = {}

    for i in f:
        a = list(i.strip().split(" "))
        print(a)
