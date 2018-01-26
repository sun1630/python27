# -*- coding:utf-8 -*-

# api 接口处理类
from flask import Flask,request
from flask_cors import CORS

app=Flask(__name__)

# 允许 hw请求 跨域  http://flask-cors.readthedocs.io/en/latest/
CORS(app,resources=({r"/hw/*": {"origins": "*"}}))

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





if __name__ == "__main__":
    app.run(debug=True)




