import multiprocessing
from concurrent.futures import ThreadPoolExecutor

def lag_the_computer(num):
    l = [x**3 for x in range(1, 20000000)]
    for i in range(1, 1000000):
        l.append(num*i)
        new = num**4 + i**3 + 15
        
def spam_files(num):
    with 
