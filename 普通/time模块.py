import time

# time.time
print(time.time())     #     1590719373.0562937

# localtime
print(time.localtime())    # time.struct_time(tm_year=2020, tm_mon=5, tm_mday=29, tm_hour=10, tm_min=30, tm_sec=6, tm_wday=4, tm_yday=150, tm_isdst=0)

print(time.localtime(100))     #time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=1, tm_sec=40, tm_wday=3, tm_yday=1, tm_isdst=0)
