# sandwich.py
import math

def sandwich(size, out_list):

    for i in range(size):
        out_list.append(math.sqrt(i * i))
