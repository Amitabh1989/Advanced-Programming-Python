"""
Code to demonstrate the most basic ASYNCHRONOUS programming using Python.
Its also termed as CONCURRENT programming. 

Remember one thing, in any case there will be only one function running but
asunc programming is a step up.

In general, all the code execution is sequential.

But to better use the CPU cycles, we introdue the ASYNC programming
(Python 3.5 onwards)

Here, when a function is sleeping, the control can be transferred to other
function to execute
so that no other CPU cycle can be saved.

Here, I demonstrate how 2 functions works asynchronously.

USAGE:
>>> import _01_concurrent
A  <- from main()
1  <- from foo() since we have a async sleep of 1 second. Control is transferred.
B  <- from main() since we have a async sleep of 1 second. Control is transferred.
2  <- from foo() since the main execution is over after

# Changed the prints to reflect better
>>> import _01_concurrent
Starting Execution : MAIN
Since MAIN is sleeping, executing FUNC_1
Since FUNC_1 is sleeping, executing MAIN
Since MAIN is done, executing FUNC_1
>>> 

"""
import asyncio

async def main():
    """
    main function that is entry point into execution
    """
    asyncio.create_task(func_1())
    print("Starting Execution : MAIN")
    await asyncio.sleep(1)
    print("Since FUNC_1 is sleeping, executing MAIN")
    await asyncio.sleep(1)


async def func_1():
    """
    main function that is entry point into execution
    """
    print("Since MAIN is sleeping, executing FUNC_1")
    await asyncio.sleep(1)
    print("Since MAIN is done, executing FUNC_1")

asyncio.run(main())
