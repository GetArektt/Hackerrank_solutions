import math
import os
import random
import re
import sys
import collections

if __name__ == '__main__':
    s = input()
    sorted(s)
    result = collections.Counter(sorted(s)).most_common(3)
    for x in result:
        print(*x)

