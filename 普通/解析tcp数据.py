# -*- coding: cp936 -*-
# import socket
# from struct import *
# from time import ctime,sleep
# from os import system
# system('title tcp sniffer')
# system('color 05')
# # the public network interface
# HOST = socket.gethostbyname(socket.gethostname())
# # create a raw socket and bind it to the public interface
# s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
# s.bind((HOST, 0))
# # Include IP headers
# s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
# # receive all packages
# #s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
# # receive a package
# while 1==1:
#     packet = s.recvfrom(65565)
#     packet = packet[0]
#     ip_header = packet[0:20]
#     iph = unpack('!BBHHHBBH4s4s',ip_header)
#     version = iph[0] >> 4 #Version
#     ihl = iph[0] * 0xF    #IHL
#     iph_length = ihl * 4  #Total Length
#     ttl = iph[5]
#     protocol = iph[6]
#     s_addr = socket.inet_ntoa(iph[8])
#     d_addr = socket.inet_ntoa(iph[9])
#     print(ctime())
#     print('Version : ' + str(version) + ' IHL : ' + str(ihl) + ' Total Length: ' + str(iph_length) + ' TTL : ' + str(
#         ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(
#         d_addr))
#     if protocol == 6:
#         tcp_header = packet[20:40]
#         tcph = unpack('!HHLLBBHHH' , tcp_header)
#         source_port = tcph[0]
#         dest_port = tcph[1]
#         sequence = tcph[2]
#         acknowledgement = tcph[3]
#         doff_reserved = tcph[4]
#         tcph_length = doff_reserved >> 4
#         print('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(
#             sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))
#         data = packet[40:len(packet)]
#         print('Data : ' + data)
#
# # disabled promiscuous mode
# s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
# import math
# def hex_to_dec(a):
#     hex= [ord(n) - 55 if n in list("ABCDEF") else ord(n) - 48 for n in a.upper()]
#     dec = [hex[-i - 1] * math.pow(16, i) for i in range(len(hex))]
#     return sum(dec)
# # a = '\0xFF\0xFF\0xFF\0xFE'
# a = '\0x00\0x00\0x00\0x64'
# res = hex_to_dec(a)
# print(res)
# print(bin(0xFFFFFFFE))
# print(bin(10))
# print(hex(4196))

# width=32  # 16进制数所占位数
# # data = '0xFE0xFF0xFF0xFF'      # 值为-2
# data = '0x640x000x000x00'        # 值为100
# data = ''.join(data.split('0x')[-1:0:-1])
# int_data=int(data, 16)
# if int_data > 2 ** (width-1)- 1:
#     int_data = 2 ** width-int_data
#     int_data=0-int_data
# print(int_data)


# def get_s16(val):
#     if val < 0x8000:
#         return val
#     else:
#         return (val - 0x10000)
# res = get_s16(0xFFFFFFFE)
# print(res)
str_list = []
with open('liaoyuan.data',"rb") as f:
    while f.readline():
       str_list.append(str(f.readline()).split(r'\r')[0].split(r'\n')[0])
str_data = ''.join(''.join(str_list).split("b'"))
print(str_data)
if '$GNRMC' in str_data:
    print('存在')
    split_data = str_data.split('$GNRMC')[1]
    print(split_data)
    print(len(split_data))
else:
    print('不存在')

        # a = str(f.readline()).split(r'\r')[0].split(r'\n')[0]
        # res = hex_to_dec(a)
        # print(res)
        # print(str(f.readline()).split(r'\r')[0].split(r'\n')[0])