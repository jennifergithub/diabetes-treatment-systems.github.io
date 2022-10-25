import multiprocessing
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

def lag_the_computer(num):
    l = [x**3 for x in range(1, 20000000)]
    for i in range(1000000):
        l.append(num*i)
        new = num**4 + i**3 + 15
        
def spam_files(num):
    for i in range(1, 101):
        with open(f'file{num}_{i}.txt', 'w') as f:
            f.write(f'Number: {num}')
            
async def waste_network():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(session.get('https://en.wikipedia.org/Georgia_Institute_of_Technology'))] * 100
            
def main():
    with ThreadPoolExecutor() as executor:
        executor.map(spam_files, list(range(1, 10001)))
    with multiprocessing.Pool() as pool:
        pool.map(lag_the_computer, list(range(1000)))
        
if __name__ == '__main__':
    main()
        
