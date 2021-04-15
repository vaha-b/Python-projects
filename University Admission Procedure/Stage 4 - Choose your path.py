# About the project:
# https://hyperskill.org/projects/163?track=2

# Stage description
# https://hyperskill.org/projects/163/stages/847/implement

n = int(input())
m = int(input())
applicants = [input().split() for _ in range(n)]
successful_applicants = sorted(applicants, key=lambda x: (-float(x[2]), x[0]))

print('Successful applicants:')
for i in range(m):
    print(*successful_applicants[i][0:2])
