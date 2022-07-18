import math

ab = int(input())
bc = int(input())

ac = math.hypot(ab,bc)
mc = mb = ac/2
theta = math.degrees(math.acos(bc/(ac)))
print(f'{round(theta):g}' u"\N{DEGREE SIGN}")
