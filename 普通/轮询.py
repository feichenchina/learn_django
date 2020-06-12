from decimal import Decimal
from threading import Timer
import time
import pymysql
conn=pymysql.connect(host='172.20.20.3', port=3306, user='root', password='jianke@2020',database='xin_rc',charset="utf8")
cursor=conn.cursor()

def printHello():
    while True:
        select_sql = "select * from gpsdatum where temp=0 and gpsTime >=1591237635000"
        cursor.execute(select_sql)
        result = cursor.fetchall()
        print(len(result))
        for i in result:
            update_sql = 'update gpsdatum set temp=1 where sn = %s and gpsTime=%s'
            cursor.execute(update_sql,(i[0],i[1]))
            conn.commit()
        if len(result) == 0:
            pass
        sqls = [i[:-1] for i in result]
        insert_sql = "insert into xin_daba_gpsdatum(sn,gpsTime,longitude,latitude,height,velocity,qualityIndex,satelliteNumber,cmv,frequency,amplitude) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(insert_sql,sqls)
        conn.commit()
        print('success')
        # time.sleep(1)

# printHello()
# def loop_func(func, second,gpstime):
#     # 每隔second秒执行func函数
#     # while True:
#         timer = Timer(second, func,args=[gpstime,])
#         timer.start()
#         timer.join()
#
#
# loop_func(printHello, 1,1591231555000)
from math import sin, asin, cos, radians, fabs, sqrt, atan, tan, acos

EARTH_RADIUS = 6371  # 地球平均半径，6371km


def hav(theta):
    s = sin(theta / 2)
    return s * s
def get_distance_hav(lat0, lng0, lat1, lng1):
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance
lon1, lat1 = (103.02624311, 32.54832148)  # 深圳野生动物园(起点）
lon2, lat2 = (103.02624310, 32.54832148)  # 深圳坪山站 (百度地图测距：38.3km)
d2 = get_distance_hav(lon1, lat1, lon2, lat2)
print(format(d2,'.15f'))


def calcDistance(Lng_A, Lat_A, Lng_B, Lat_B):
    """
    根据两个点的经纬度求两点之间的距离,注意需要乘以1000,因为返回的单位为千米
    :param Lng_A:
    :param Lat_A:
    :param Lng_B:
    :param Lat_B:
    :return:
    """
    ra = 6378.140
    rb = 6356.755
    flatten = (ra - rb) / ra
    rad_lat_A = radians(Lat_A)
    rad_lng_A = radians(Lng_A)
    rad_lat_B = radians(Lat_B)
    rad_lng_B = radians(Lng_B)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    # 经测试当传入这两个点的经纬度一样时会返回 *
    if sin(xx/2)==0:
        return '*'
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance

print('经纬度：',calcDistance(103.02628873,32.54575973,103.02631256,32.54597357)*1000)
print('经纬度：',calcDistance(103.02624311, 32.54832148,103.02624310, 32.54832148)*1000)
