num = int(input())
applicants = []

subjects_dict = {"Biotech": [], "Chemistry": [],
                 "Engineering": [], "Mathematics": [], "Physics": []}

with open("University Admission Procedure\Stage 4 - Applicant_list_example.txt", "r") as f:
    for i in f:
        student = list(i.strip().split(" "))
        student = [student[0] + " " + student[1], *student[2:]]
        applicants.append(student)

    # Sorts applicants by GDP in descending ord.
    applicants = sorted(applicants, key=lambda x: -float(x[1]))
    # print(applicants)

for applicant in applicants:
    for subject in applicant[:]:
        if subject == "Biotech" and applicant.index(subject) == 2:
            index = applicant[:][:].index(subject)

            if len(subjects_dict[subject]) < num:
                this_set = [*applicant[:2], subject]
                subjects_dict[subject].append(this_set)

            elif len(subjects_dict[applicant[index+1]]) < num:
                this_set = [*applicant[:2], applicant[index+1]]
                subjects_dict[applicant[index+1]].append(this_set)

            elif len(subjects_dict[applicant[index+2]]) < num:
                this_set = [*applicant[:2], applicant[index+2]]
                subjects_dict[applicant[index+2]].append(this_set)

        elif subject == "Chemistry" and applicant.index(subject) == 2:
            index = applicant[:][:].index(subject)

            if len(subjects_dict[subject]) < num:
                this_set = [*applicant[:2], subject]
                subjects_dict[subject].append(this_set)

            elif len(subjects_dict[applicant[index+1]]) < num:
                this_set = [*applicant[:2], applicant[index+1]]
                subjects_dict[applicant[index+1]].append(this_set)

            elif len(subjects_dict[applicant[index+2]]) < num:
                this_set = [*applicant[:2], applicant[index+2]]
                subjects_dict[applicant[index+2]].append(this_set)

        elif subject == "Engineering" and applicant.index(subject) == 2:
            index = applicant[:][:].index(subject)

            if len(subjects_dict[subject]) < num:
                this_set = [*applicant[:2], subject]
                subjects_dict[subject].append(this_set)

            elif len(subjects_dict[applicant[index+1]]) < num:
                this_set = [*applicant[:2], applicant[index+1]]
                subjects_dict[applicant[index+1]].append(this_set)

            elif len(subjects_dict[applicant[index+2]]) < num:
                this_set = [*applicant[:2], applicant[index+2]]
                subjects_dict[applicant[index+2]].append(this_set)

        elif subject == "Mathematics" and applicant.index(subject) == 2:
            index = applicant[:][:].index(subject)

            if len(subjects_dict[subject]) < num:
                this_set = [*applicant[:2], subject]
                subjects_dict[subject].append(this_set)

            elif len(subjects_dict[applicant[index+1]]) < num:
                this_set = [*applicant[:2], applicant[index+1]]
                subjects_dict[applicant[index+1]].append(this_set)

            elif len(subjects_dict[applicant[index+2]]) < num:
                this_set = [*applicant[:2], applicant[index+2]]
                subjects_dict[applicant[index+2]].append(this_set)

        elif subject == "Physics" and applicant.index(subject) == 2:
            index = applicant[:][:].index(subject)

            if len(subjects_dict[subject]) < num:
                this_set = [*applicant[:2], subject]
                subjects_dict[subject].append(this_set)

            elif len(subjects_dict[applicant[index+1]]) < num:
                this_set = [*applicant[:2], applicant[index+1]]
                subjects_dict[applicant[index+1]].append(this_set)

            elif len(subjects_dict[applicant[index+2]]) < num:
                this_set = [*applicant[:2], applicant[index+2]]
                subjects_dict[applicant[index+2]].append(this_set)


print(subjects_dict)

for key, value in subjects_dict.items():
    print("\n" + key)
    # print(key, value)
    for i in value:
        print(" ".join(i[:-1]))
