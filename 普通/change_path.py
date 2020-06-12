from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()   #关闭默认tk小窗口

Folderpath = filedialog.askdirectory()  #获取目录路径
print(Folderpath)
