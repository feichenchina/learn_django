# list1 = [1,2,3,4,5,6,7,8,9,10]
# def sun(list1):
#     return list1
# result = [i async for i in sun(list1) if i % 2]
# print(result)
async def elements(n):
    yield n
    # yield n*2
    # yield n*3
    # yield n*4


async def test():
    return {n:[x async for x in elements(n)] for n in range(3)}
