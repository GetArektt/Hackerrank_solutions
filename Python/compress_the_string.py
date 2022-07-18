import itertools


string = input()

S = [int(a) for a in str(string)]

for key, group in itertools.groupby(S, None):
    print((len(list(group)), key), end=" ")
