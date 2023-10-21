def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permut_C(n, m):
    return factorial(n) / (factorial(n - m) * factorial(m))

def permut_A(n, m):
    return permut_C(n, m) * factorial(m)