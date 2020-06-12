# list1 = [1,2,3,4,5,6,7,8,9,10]
# def sun(list1):
#     return list1
# result = [i async for i in sun(list1) if i % 2]
# print(result)
# async def elements(n):
#     yield n
#     # yield n*2
#     # yield n*3
#     # yield n*4
#
#
# async def test():
#     return {n:[x async for x in elements(n)] for n in range(3)}

# import asyncio
# async def cancel_me(x,y,time_sel):
#     print('cancel_me(): before sleep')
#
#     try:
#         # Wait for 1 hour
#         # await asyncio.sleep(3600)
#         import time
#         await asyncio.sleep(3,time_sel)
#         a = x+y
#         return a
#     except asyncio.CancelledError:
#         print('cancel_me(): cancel sleep')
#         raise
#     finally:
#         print('cancel_me(): after sleep')
#
# async def main():
#     # Create a "cancel_me" Task
#     import time
#     start = time.time()
#     x = 3
#     y = 4
#     time_sel = ''
#     task = asyncio.create_task(cancel_me(x,y,time_sel))
#     task1 = asyncio.create_task(cancel_me(x, y,time_sel))
#     task2 = asyncio.create_task(cancel_me(x, y,time_sel))
#     task3 = asyncio.create_task(cancel_me(x, y,time_sel))
#     task4 = asyncio.create_task(cancel_me(x, y,time_sel))
#
#     try:
#
#         res = await task,task1,task2,task3,task4
#         if res:
#             print(time_sel)
#             print("result:",res)
#         else:
#             print('暂无数据')
#         end = time.time()
#         print("耗时：",end-start)
#     except asyncio.CancelledError:
#         print("main(): cancel_me is cancelled now")
#
# asyncio.run(main())


# asyncio.gather用来存储并发运行的函数
# import asyncio
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#
# async def main():
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#
# asyncio.run(main())


# asyncio.wait_for   设置超时
import asyncio
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())