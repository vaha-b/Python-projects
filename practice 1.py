applicants = [['vaha', 11.3], ['ajd aa', 11.2],
              ['ajd ba', 11.2], ['mir', 10.1]]

successful_applicants = sorted(
    applicants, key=lambda x: (x[1], x[0]), reverse=True)
print(successful_applicants)
successful_applicants = sorted(
    successful_applicants, key=lambda x: (-x[1], x[0]))

print(successful_applicants)
