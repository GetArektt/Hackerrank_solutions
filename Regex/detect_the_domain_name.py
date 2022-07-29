import re

N=int(input())
domains = []
for _ in range(N):
    string=input()
    result = re.findall(r"(?:https?://)(?:www.|ww2.)?((?:[a-zA-Z0-9\._-]+)\.[a-zA-Z]+)",string)
    for item in result:
        if item not in domains:
            domains.append(item)
domains.sort()
print(";".join(map(str,domains)))   

