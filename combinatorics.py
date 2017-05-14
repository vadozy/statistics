import operator as op
import functools as ft

def fact(n):
    """
    Factorial

    Returns n!
    """
    if n < 0: return 0
    if n == 0: return 1
    return ft.reduce(op.mul, range(n, 0, -1))

def npk(n, k):
    """
    Permutations (Ordered Sampling without Replacement)

    Returns the total number of ways to choose k objects from a set with n elements:
    npk = n×(n−1)×...×(n−k+1)
    npk = n!/(n-k)!
    """
    if min(k, n-k) < 0: return 0
    if k == 0: return 1
    return ft.reduce(op.mul, range(n, n-k, -1))

def nck(n, k):
    """
    n choose k (Unordered Sampling without Replacement)
    aka binomial coefficient

    Returns the total number of ways to choose k objects from a set with n elements:
    nck(n,k) = npk(n,k)/k!
    nck = n!/(k!*(n-k)!)
    """
    k = min(k, n-k)
    if k < 0: return 0
    if k == 0: return 1
    numer = ft.reduce(op.mul, range(n, n-k, -1))
    denom = ft.reduce(op.mul, range(1, k+1))
    return numer//denom

# Test
# print("nck(n=4, k=0) = {}".format(nck(n=4, k=0)))
# print("nck(n=4, k=1) = {}".format(nck(n=4, k=1)))
# print("nck(n=4, k=2) = {}".format(nck(n=4, k=2)))
# print("nck(n=4, k=3) = {}".format(nck(n=4, k=3)))
# print("nck(n=4, k=4) = {}".format(nck(n=4, k=4)))
# print("nck(n=4, k=5) = {}".format(nck(n=4, k=5)))