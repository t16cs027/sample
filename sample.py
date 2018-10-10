'''
Created on 2018/10/10

@author: t16cs027
'''

def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)