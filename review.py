#! /usr/bin/env python3
import os
import requests

dir="/data/feedback/"
url= "http://1.1.1.1/feedback/"
#Replace with corpweb" IP Address

for file in os.listdir(dir):
    head = ["title","name","date","feedback"]
    d = {}
    lineas = []
    print(file)
    with open(dir+"/"+file,"r") as f
        x = 0
        for line in f:
            d[head[x]] = line.rsplit('\n')
            x += 1
    print(d)
    response = requests.post(url,json=d)