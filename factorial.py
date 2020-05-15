# -*- coding: utf-8 -*-

def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    return n!
    """
    print(n, end='')

    if n == 1:
        return 1
    return n * factorial(n-1)
    
   

print(factorial(10))
