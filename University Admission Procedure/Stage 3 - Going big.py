# About the project:
# https://hyperskill.org/projects/163?track=2

# Stage description
# https://hyperskill.org/projects/163/stages/846/implement

import re

n = int(input())
m = int(input())
student_list = []

for i in range(1, n+1):
    student_list.append(input().split())

applicants = []
for name, surname, s in student_list:
    applicants.append([name + " " + surname, float(s)
                       if re.match("\d", str(s)) else ""])

successful_applicants = sorted(applicants, key=lambda x: (-x[1], x[0]))
print("Successful applicants:")
for name, _ in successful_applicants[:m]:
    print(name)

# ANOTHER GREAT SOLUTION MADE BY OTHER USER THAT I JUST HAD TO COPPY
n = int(input())
m = int(input())
applicants = [input().split() for _ in range(n)]
successful_applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0]))

print('Successful applicants:')
for i in range(m):
    print(*successful_applicants[i][0:2])
