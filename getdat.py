# -*- coding: utf-8 -*-
from flask import request
import random
import time
import math

def getdat_none():
    if request.method == 'POST':
        z = request.form['z']
        x = request.form['x']
        c = request.form['c']
        p = request.form['p']
        return none(z,x,c,p)

def none(z,x,c,p):
        e = open("prediction_none.csv","r")
        o = ""
        p = int(p)
        while 1:
            w = e.readline()
            if len(w)==0:
                break
            q = w.split(",")[4]
            m = w.split(",")[3]
            if q[0:q.find("M")]==z and q[q.find("M")+1:q.find("D")]==x and c==m:
                o = o + w.split(",")[p] + ","
        e.close()
        return o

def getdat_smooth():
    if request.method == 'POST':
        z = request.form['z']
        x = request.form['x']
        c = request.form['c']
        p = request.form['p']
        return smooth(z,x,c,p)

def smooth(z,x,c,p):
        e = open("prediction_smooth.csv","r")
        o = ""
        p = int(p)
        while 1:
            w = e.readline()
            if len(w)==0:
                break
            q = w.split(",")[4]
            m = w.split(",")[3]
            if q[0:q.find("M")]==z and q[q.find("M")+1:q.find("D")]==x and c==m:
                o = o + w.split(",")[p] + ","
        e.close()
        return o



def jgetcluster():
    if(request.method =='POST'):
        clusterfile = open("newcluster.txt","r");
        retext = "";
        while(1):
            w = clusterfile.readline()
            if(len(w)==0):
                break
            retext = retext+w
        clusterfile.close()
        #print(retext)
        #print(retext.replace('\n',' '))
        return retext.replace('\n',' ')

def getinfo():
    if(request.method =='POST'):
        poifile = open("info.txt","r");
        retext = "";
        while(1):
            w = poifile.readline()
            if(len(w)==0):
                break
            retext = retext+w
        poifile.close()
        #print(retext)
        #print(retext.replace('\n',' '))
        return retext
def getpfo():
    if(request.method =='POST'):
        poifile = open("price.txt","r");
        retext = "";
        while(1):
            w = poifile.readline()
            if(len(w)==0):
                break
            retext = retext+w
        poifile.close()
        #print(retext)
        #print(retext.replace('\n',' '))
        return retext







