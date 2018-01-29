# -*- coding:utf-8 -*-

# api 接口处理类
from flask import Flask,request
from flask_cors import CORS
from xiaomi_beautifulsoup import xmApi



app=Flask(__name__)

# 允许 hw请求 跨域  http://flask-cors.readthedocs.io/en/latest/
#CORS(app,resources=({r"*": {"origins": "*"}}))
CORS(app,resources=({r"/api/*": {"origins": "*"}}))

# GET 测试
# 方式一 get http://localhost:1222/hw?num1=1&num2=2
@app.route('/hw',methods=['GET','POST'])
def index():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return (num1+num2)

#  方式二 http://localhost:1222/hw/num1/num2
@app.route('/hw/<num1>/<num2>',methods=['GET','POST'])
def index1(num1,num2):
    return (num1+num2)

# 获取小米商城商品列表
@app.route('/api/xm',methods=['GET','POST'])
def xm():
   return xmApi()

if __name__ == "__main__":
    app.run(debug=True)




