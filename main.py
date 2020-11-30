#coding=utf-8  

#-*- coding: UTF-8 -*-
#使文件支持中文

from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import request
from flask import redirect
from getdat import getdat_none
from getdat import getdat_smooth
from getdat import jgetcluster
from getdat import getinfo
from getdat import getpfo
import sys


app = Flask(__name__)#新建网站对象


@app.route('/')#表示括号中路径对应网页的逻辑如下
def indx():
    return render_template('index.html')

@app.route('/pricing')
def efg():
    return render_template("dispatch.html")

@app.route('/predict/<w>')#<w>表示+/的内容s
def eu(w):
        #if 'use' in session:
        if w=="none":
            return render_template("predict_none.html")
        if w=="smooth":
            return render_template("predict_smooth.html")

@app.route('/cluster')
def euq():
    return render_template("cluster.html")

@app.route('/getpoi',methods=['GET','POST'])
def equc():
    return getinfo()

@app.route('/getpo',methods=['GET','POST'])
def equcccc():
    return getpfo()

@app.route('/point')
def equ():
    return render_template("point.html")

@app.route('/predict/getpredictnone' , methods=['GET','POST'])
def controller_getdat_none():
    return getdat_none()

@app.route('/predict/getpredictsmooth' , methods=['GET','POST'])
def controller_getdat_smooth():
    return getdat_smooth()

@app.route('/getcluster' , methods=['GET','POST'])
def controller_getcluster():
    return jgetcluster()

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__=='__main__':
    app.run()
