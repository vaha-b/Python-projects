
from sqlalchemy import create_engine

engine = create_engine('sqlite:///')
engine = create_engine('sqlite:///practice.sqlite', echo=True)

connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

# def __str__(self):
#        return '{} by {}. ${}. [{}]'.format(self.title, self.author, self.price, self.book_id)

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
