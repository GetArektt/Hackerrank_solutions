string = list(input())
upper = []
lower = []
even = []
odd = []
for i in string:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    else:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
upper.sort()
lower.sort()
even.sort()
odd.sort()

print("".join(lower + upper + odd + even))
