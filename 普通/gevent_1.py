# from gevent import monkey
# monkey.patch_socket()
# import gevent
#
# def f(n):
#     for i in range(n):
#         gevent.sleep(1)
#         print (gevent.getcurrent(), i)
#
# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 4)
# g3 = gevent.spawn(f, 3)
# g1.join()
# g2.join()
# g3.join()

from gevent import monkey; monkey.patch_all()
import gevent
import request

def f(url):
    print('GET: %s' % url)
    resp = request.GET(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])