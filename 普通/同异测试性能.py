# import time
#
# def hello():
#     time.sleep(1)
#
# def run():
#     for i in range(5):
#         hello()
#         print('Hello World:%s' % time.time())
# if __name__ == '__main__':
#     run()


# 异步
import time
import asyncio

# 定义异步函数
def t():
    time.sleep(3)
    print('世界，你好！')
    return 3
async def hello():
    print('Hello World:%s' % time.time())

def run():
    for i in range(5):
        loop.run_until_complete(hello())

loop = asyncio.get_event_loop()
if __name__ =='__main__':
    run()


# import time
#
# def hello():
#     time.sleep(1)
#
# def run():
#     for i in range(5):
#         hello()
#         print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！
# if __name__ == '__main__':
#     run()

# import asyncio
# import time
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())

