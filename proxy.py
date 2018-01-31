# -*- coding=utf-8 -*-

# 目标： 生成抓取代理exe程序
# 主要功能： 地区，代理类型均可选  显示代理存活时间，连接时间，速度，最大可抓取条数，表格展示

from tkinter import *
root = Tk()
root.title('代理IP!')    # 添加 初识框的标题

# 第一行
proxyTypeValue=IntVar()
Label(root,text="代理类型：").grid(row=0,column=0,sticky="w")
httpRdo = Radiobutton(root, text='HTTP', variable=proxyTypeValue,value="1")
httpRdo.grid(row=0,column=1, sticky=W)
httpsRdo = Radiobutton(root, text='HTTPS', variable=proxyTypeValue,value="2")
httpsRdo.grid(row=0,column=2, sticky=W)

# 第二行
highHideValue=IntVar()
Label(root,text="是否匿名：").grid(row=1,column=0,sticky="w")
highHideRdo = Radiobutton(root, text='高匿', variable=highHideValue,value="1")
highHideRdo.grid(row=1,column=1, sticky=W)
hyalineRdo = Radiobutton(root, text='透明', variable=highHideValue,value="2")
hyalineRdo.grid(row=1,column=2, sticky=W)




mainloop()










# 代理类

#设置代理




