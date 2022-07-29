import re
N=int(input())
emails = []
for _ in range(N):
    string=input()
    result = re.findall(r"[\w\.]+@[\w+\.]+\w+",string)
    for item in result:
        if item not in emails:
            emails.append(item)
emails.sort()
print(";".join(map(str,emails)))   
