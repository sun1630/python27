# -*- coding:utf-8 -*-

from flask import Flask,request

app=Flask(__name__)
# GET
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




