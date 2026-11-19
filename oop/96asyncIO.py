import asyncio
import time


async def function1():
    await asyncio.sleep(4)
    print("Function 1 completed")

async def function2():
    await asyncio.sleep(3)
    print("Function 2 completed")

async def function3():
    await asyncio.sleep(1)
    print("Function 3 completed")


# async def main():
#     task=asyncio.create_task(function1())
#     await function2()
#     await function3()
 

async def secomdmain():
    l=await asyncio.gather(
        function1(),
        function2(),
        function3()
    )


# asyncio.run(main())
asyncio.run(secomdmain())
print("All functions completed")
  