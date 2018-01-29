# -*- coding=utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
from collections import OrderedDict

# beautifulSoup4 处理小米商城秒杀HTML

# 抓取小米商城页面HTML
def xmUrl():
    res=False
    try:
        res = requests.get("https://list.mi.com")
        res.encoding='utf-8'
        #print(res.text)
    except BaseException:
        print('api Error：接口地址异常')
        raise Exception("api Error：接口地址异常") #抛出异常欣喜
    return res



# 查找商品分类节点 获取商品信息
def shopInfoByCategory(res):
    soup = BeautifulSoup(res.text, 'html.parser', from_encoding='utf-8')
    categorys=soup.find_all('div',class_='xm-plain-box category-list')
    shop=[]
    for cg in categorys:
        title = cg.div.h2.get_text()
        ts = OrderedDict()
        ts["title"]=title

        shops =[]
        sps=cg.find_all('li')
        for sp in sps:
            spName=sp.find('a',class_='category-list-title').get_text()
            ss=OrderedDict()
            ss["shopName"]=spName
            shops.append(ss)

        ts["shopList"]=shops
        shop.append(ts)
        # 打印数组出现中文编码问题 使用json.dumps([],ensure_ascii=False)
        # print(json.dumps(shop,ensure_ascii=False,indent=4))
    #print(json.dumps(shop, ensure_ascii=False, indent=4))
    return json.dumps(shop, ensure_ascii=False)

# 入口接入
def xmApi():
    res=xmUrl()
    json=shopInfoByCategory(res)
    return json

if __name__=='__main__':
    xmApi()














