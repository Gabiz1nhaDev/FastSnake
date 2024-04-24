# Solution for problem A of contest 1956

# [START STEP COUNTER]

# from fastsnake.algorithms.something import *
# from fastsnake.structures.something import *
# from fastsnake.external.your_external_module import *

# Just remove the fastsnake code below if you will not use it.
from fastsnake.entries import *
puti = input_int
puta = input_int_array
putm = input_int_matrix

def f(players, a):
    while True:
        r = False

        for x in a:
            if len(players) >= x:
                players.pop(x-1)
                r = True
        if not r:
            break
    return players


for test_case in range(int(input())):
    k, q = puta()
    a = puta()
    ns = sorted(puta())

    mem = []
    c = []

    for i in range(len(ns)):
        n = list(range(1, ns[i] + 1))
        n = f(n, a)
        c.append(len(n))
    print(*c)




# [WARNING]: THIS IS AN **UNCOMPILED** SOLUTION!! Remember to REMOVE fastsnake code if you will NOT COMPILE this code.


