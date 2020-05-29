# import os,time
# from multiprocessing import Pool
# def worker(arg):
#   print("子进程开始执行>>> pid={},ppid={},编号{}".format(os.getpid(),os.getppid(),arg))
#   time.sleep(0.5)
#   print("子进程终止>>> pid={},ppid={},编号{}".format(os.getpid(),os.getppid(),arg))
# def main():
#   print("主进程开始执行>>> pid={}".format(os.getpid()))
#   ps=Pool(5)
#   for i in range(10):
#     # ps.apply(worker,args=(i,))     # 同步执行
#     ps.apply_async(worker,args=(i,)) # 异步执行
#   # 关闭进程池，停止接受其它进程
#   ps.close()
#   # 阻塞进程
#   # ps.join()
#   print("主进程终止")
# if __name__ == '__main__':
#   main()



import math
from math import *


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
  if sin(xx / 2) == 0:
    return '*'
  c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
  dr = flatten / 8 * (c1 - c2)
  distance = ra * (xx + dr)
  return distance

def calc_triangle_area(a, b, c):
  """
  已知三角形三边求面积
  :param a:
  :param b:
  :param c:
  :return:
  """
  # 令p = (a + b + c) / 2
  # 则S =√[p(p - a)(p - b)(p - c)]
  p = (a + b + c) / 2
  s = math.sqrt(p * (p - a) * (p - b) * (p - c))
  return s
def calc_area(control_set):
  """
  根据控制点坐标,计算控制点面积并返回面积
  将控制点切割为几个三角形，分别求每个三角形面积，最后相加
  :param control_set:
  :return:
  """
  # 比如说有五个控制点
  # [[lon,lat],[lon,lot],[lon,lat],[lon,lat],[lon,lat]]
  # 以第一个点为起点O计算这个点到其余所有点的距离
  O = control_set[0]
  # 用于记录O到所有点的距离
  start_distance_set = []
  for index, lon_lat in enumerate(control_set):
    if index < 1:
      continue
    start_distance_set.append(calcDistance(O[0], O[1], lon_lat[0], lon_lat[1]) * 1000)
  left_points_distance_set = []
  for i, lon_lat in enumerate(control_set):
    if i < 2:
      continue
    left_points_distance_set.append(
      calcDistance(control_set[i - 1][0], control_set[i - 1][1], lon_lat[0], lon_lat[1]) * 1000)
  triangle_areas = []
  for j, distance in enumerate(start_distance_set):
    if j < 1:
      continue
    triangle_areas.append(
      calc_triangle_area(start_distance_set[j - 1], start_distance_set[j], left_points_distance_set[j - 1]))
  total_area = 0
  for area in triangle_areas:
    total_area = total_area + area
  return total_area
control_set = [(103.0265887835, 32.5478446682), (103.026577283, 32.5478703935), (103.0259624862, 32.5476049886), (103.0259809304, 32.5475855701)]
total_area = calc_area(control_set)
print(type(total_area))
print(total_area)
x_total_length = 58.82658498650902
y_total_width = 31.58600578324691

rate = total_area/(x_total_length*y_total_width)
print(rate)
# import time
# start = time.time()
# data_list = []
# for i in range(1,118):
#   for j in range(1,84):
#     data_list.append([i,j])
# print(data_list)
# end = time.time()
# print("耗时：",end-start)