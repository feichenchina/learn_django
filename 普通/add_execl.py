# 将多个Excel文件合并成一个
import xlrd
import xlsxwriter
import os
from tkinter import filedialog
import tkinter as tk
temp = 1
# 打开一个excel文件
def open_xls(file):
    fh = xlrd.open_workbook(file)
    return fh


# 获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()


# 获取sheet表的行数
def getnrows(fh, sheet):
    table = fh.sheets()[sheet]
    return table.nrows


# 读取文件内容并返回行内容
def getFilect(file, shnum,datavalue):
    global temp
    fh = open_xls(file)
    table = fh.sheets()[shnum]
    num = table.nrows
    # print(num)
    title = table.row_values(0)
    for row in range(1,num):
        rdata = table.row_values(row)
        if rdata[0] == '关闭':
            pass
        else:
            rdata[0] = temp
            temp += 1
            print(type(rdata))
            print(rdata)
            print('>>>>>>>>>>>>>>>>>>>>')
            datavalue.append(rdata)
    return datavalue,title


# 获取sheet表的个数
def getshnum(fh):
    x = 0
    sh = getsheet(fh)
    for sheet in sh:
        x += 1
    return x

def get_file_path(path):# 递归获取指定目录下所有文件的绝对路径（非目录）
    result = []
    dir_list = os.listdir(path)
    for i in dir_list:
        sub_dir = os.path.join(path, i)
        if os.path.isdir(sub_dir):
            get_file_path(sub_dir)
        else:  # 此时sub_dir是文件的绝对路径
            result.append(sub_dir)
    return result

def run():
    # 定义要合并的excel文件列表
    # os.popen("C:\Windows\System32\osk.exe")
    root = tk.Tk()
    root.withdraw()  # 关闭默认tk小窗口
    Folderpath = filedialog.askdirectory()  # 获取目录路径
    # path = r'C:\Users\98113\Desktop\add'
    path = Folderpath
    allxls = get_file_path(path)
    # print(result)
    # allxls = ['F:/test/excel1.xlsx', 'F:/test/excel2.xlsx']
    # 存储所有读取的结果
    datavalue = []
    for fl in allxls:
        fh = open_xls(fl)
        x = getshnum(fh)
        for shnum in range(x):
            print("正在读取文件：" + str(fl) + "的第" + str(shnum) + "个sheet表的内容...")
            datavalue,title = getFilect(fl, shnum,datavalue)
            # datavalue.append(rvalue)
    # 定义最终合并后生成的新文件
    endfile = f'{path}/excel3.xlsx'
    wb1 = xlsxwriter.Workbook(endfile)
    datavalue.insert(0,title)
    # print(rvalue)
    # 创建一个sheet工作对象
    ws = wb1.add_worksheet()
    for a in range(len(datavalue)):
        for b in range(len(datavalue[a])):
            c = datavalue[a][b]
            ws.write(a, b, c)
    wb1.close()
    print("文件合并完成")

run()
