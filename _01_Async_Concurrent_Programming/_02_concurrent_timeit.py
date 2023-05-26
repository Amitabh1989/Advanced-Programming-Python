# from dataclasses import dataclass
import asyncio
import time

def timeit(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        ret = await func(*args, **kwargs)
        stop = time.time()
        print(f'{type(func).__name__} took {stop-start} seconds')
        return wrapper
    return wrapper

@timeit
async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await asyncio.sleep(1)
    ret_val = await task
    await asyncio.sleep(1)
    print(f"Retval : {ret_val}")
    await asyncio.sleep(1)


@timeit
async def other_function():
    print("1")
    await asyncio.sleep(5)
    print("2")
    return 10

asyncio.run(main())

OUTPUT = r"""
Type "help", "copyright", "credits" or "license" for more information.
>>> import _01_concurrent
A
1
B
2
function took 4.9999330043792725 seconds
Retval : <function timeit.<locals>.wrapper at 0x000001E8A47EB920>
function took 7.030808210372925 seconds
"""