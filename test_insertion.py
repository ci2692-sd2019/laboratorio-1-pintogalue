from insertion import *

R = []
filename = './test.txt'

with open(filename,'r') as file:
    raw = file.readlines()
    R = [int(k) for k in raw]
    print('secuencia antes de ejecutar insertion sort:')
    print(R)
    print('\nsecuencia resultante de aplicar insertion sort')
    insertion_sort(R)
    print(R)
