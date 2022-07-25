import re

def card_number_is_valid(s):
    if len(s) == 16:
        result = re.match(r"(?!.*(\d)(-?\1){3})(^[4-6]\d{15})", s)
    elif len(s) == 19:
        result = re.match(r"(?!.*(\d)(-?\1){3})((^[4-6]\d{3}-)((\d){4}-){2}(\d){4})", s)
    else: return False
    return result

N = int(input())
for _ in range(N):
    string = input()
    if card_number_is_valid(string): print("Valid")
    else: print("Invalid")
