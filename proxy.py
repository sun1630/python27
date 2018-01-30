# -*- coding=utf-8 -*-

# 目标： 生成抓取代理exe程序
# 主要功能： 地区，代理类型均可选  显示代理存活时间，连接时间，速度，最大可抓取条数，表格展示

from tkinter import *
root = Tk()
root.title('代理IP!')    # 添加 初识框的标题

httpValue=StringVar()
httpValues=StringVar()

Label(root,text="代理类型：").grid(row=0,column=0,sticky="w")


def callCheckbutton():
    httpValue.set("aaaaa");

httpChk = Checkbutton(root, text='HTTP', variable=httpValue,command = callCheckbutton).pack()
httpChk.grid(row=0,column=1, sticky=W)
httpsChk = Checkbutton(root, text='HTTPS',value="https", variable=httpValues)
httpsChk.grid(row=0,column=2, sticky=W)



mainloop()










# 代理类

#设置代理




