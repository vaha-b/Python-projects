# About the project:
# https://hyperskill.org/projects/163?track=2

# Stage description
# https://hyperskill.org/projects/163/stages/845/implement

a = int(input())
b = int(input())
c = int(input())

mean = (a + b + c) / 3
print(mean)

if mean >= 60:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")
