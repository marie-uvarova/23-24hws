from mymath import *

print(dir())
x = input('Enter C for combinatorics, G for geometry.')
if x == 'C':
    print('Choose the function you need: factorial, C-permutation, A-permutation. Enter STOP if you want to exit.')
    ans = input()
    while ans != 'STOP':
        if ans == 'factorial':
            n = int(input())
            print(factorial(n))
        elif ans == 'C-permutation':
            n, m = int(input())
            #print(combinatorics.permut_C(n, m))
        elif ans == 'A-permutation':
            n, m = int(input())
            #print(combinatorics.permut_A(n, m))

