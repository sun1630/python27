# -*- coding=utf-8 -*-
import Tkinter as tk
import requests
import json
from bs4 import BeautifulSoup
from collections import OrderedDict

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 15, 8)
        t.pack(side="top", fill="x")


        # 设置表头
        ths=["国家","代理IP地址","端口","服务器地址","是否高匿","类型","存活时间","验证时间"]
        thsLen=len(ths)
        for th in range(thsLen):
            print("%s %s" % (ths[th],th))
            t.set(0,th,ths[th])

        res = xici()
        xiciData(res,t)
        #t.set(0,0,ths[0])


def xici():
    res = False
    try:
        # 设置User-Agent浏览器信息
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        cookie="_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTIzNDdjODA1ZTk2YjRhNDljNThhZTZmNTkzMjIxY2MxBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWZadG5QWk1sMEd2cFE2Sk5nUllmSG9zazFHVzAyRUNseVZmT2h3aVBYd0E9BjsARg%3D%3D--b1141333649eddda23275761e01ca9412cdefb01; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1517280032,1517291255,1517392101,1517470107; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1517473121"
        proxies = {"https": "http://211.159.177.212:3128"}  # 设置代理
        res = requests.get("http://www.xicidaili.com/nn/1",headers=headers)
        #print(res.text)
    except BaseException:
        raise Exception("api Error：接口地址异常")  # 抛出异常信息
    return res;

def xiciData(res,t):
    soup = BeautifulSoup(res.text, 'html.parser')
    tables=soup.find_all('table',id="ip_list")
    trs=tables[0].find_all("tr")
    #print(trs)

    for i in range(15):
        print(i)
        if i!=0:
            country = trs[i].find("img")
            if country!=None:
                country=country.get("alt")
            else:
                country=""
            t.set(i,0,country)

            ip=trs[i].find_all("td")[1]
            if ip!=None:
                ip=ip.get_text()
            else:
                ip=""
            t.set(i, 1, ip)

            port=trs[i].find_all("td")[2]
            if port!=None:
                port=port.get_text()
            else:
                port=""
            t.set(i, 2, port)

            serverAddr = trs[i].find_all("td")[3].find("a")
            if serverAddr != None:
                serverAddr = serverAddr.get_text()
            else:
                serverAddr = ""
            t.set(i, 3, serverAddr)

            highHide = trs[i].find_all("td")[4]
            if highHide != None:
                highHide = highHide.get_text()
            else:
                highHide = ""
            t.set(i, 4, highHide)

            http = trs[i].find_all("td")[5]
            if http != None:
                http = http.get_text()
            else:
                http = ""
            t.set(i, 5, http)

            live = trs[i].find_all("td")[8]
            if live != None:
                live = live.get_text()
            else:
                live = ""
            t.set(i, 6, live)

            vdalitate = trs[i].find_all("td")[9]
            if vdalitate != None:
                vdalitate = vdalitate.get_text()
            else:
                vdalitate = ""
            t.set(i, 7, vdalitate)

            print("%s %s" % (country,ip))

    #tr=table.find_all("tr")





class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    print(size)
    root.geometry(size)

if __name__ == "__main__":
    app = ExampleApp()
    app.title('测试窗口')
    center_window(app, 800, 318)
    #app.maxsize(600, 400)
    #app.minsize(600, 318)
    app.resizable(0, 0)
    app.mainloop()