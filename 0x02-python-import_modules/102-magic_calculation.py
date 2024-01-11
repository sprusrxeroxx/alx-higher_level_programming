#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return sub(a, b)
...........................................................
vi 103-fast_alphabet.py

#!/usr/bin/python3
import string
print(string.ascii_uppercase)

