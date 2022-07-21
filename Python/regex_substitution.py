import re

N = int(input())
string = ""
for _ in range(N):
    string += input() + "\n"

result = re.sub(r"\ \|\|\ ", " or ", re.sub(r"\ \&\&\ ", " and ", string))

print(re.sub(r"\ \|\|\ ", " or ", re.sub(r"\ \&\&\ ", " and ", result)))
