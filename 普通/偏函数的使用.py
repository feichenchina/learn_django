# partial
from functools import partial


def a(*args,**kwargs):
    print(sum(args))

# a(1,2,3,4)

b = partial(a,100,v=10)
b(1,2,3)
