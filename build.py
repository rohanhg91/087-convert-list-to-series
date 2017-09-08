import pandas as pd


def solution(array):
    b = pd.Series(array)
    b.index.name = 'Index'
    b.name = 'value'
    return b


'''
a = [2, 1, 3, 5]
print solution(a)
'''
