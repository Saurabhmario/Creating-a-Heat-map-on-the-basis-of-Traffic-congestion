import requests
import json
import schedule
import time 
import datetime
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# def func():
#     request = requests.get("https://data.traffic.hereapi.com/v7/flow?in=circle:30.9010167,75.9094733;r=200&locationReferencing=shape&apiKey=jpCatShkVUwcTW9tvl30gEghCIdXxOrNA0TXplvm2oE")
#     request_text = request.text
#     JSON = json.loads(request_text)

#     resultCount = len(JSON['results'])
#     # print(len(JSON['results']))
#     # print(len(JSON['results'][0]['location']['shape']['links'][0]['points']))
#     # print(len(JSON['results'][0]['location']['shape']['links']))
#     lats=[]
#     longs=[]
#     sus=[]
#     ffs=[]

#     for i in range(0, resultCount):
#         su = float(JSON['results'][i]['currentFlow']['speed'])
#         ff = float(JSON['results'][i]['currentFlow']['freeFlow'])
#         for j in range(0, len(JSON['results'][i]['location']['shape']['links'])):
#             la = []
#             lo = []
#             su1 = []
#             ff1 = []
#             for k in range(0, len(JSON['results'][i]['location']['shape']['links'][j]['points'])):
#                 la.append(float(JSON['results'][i]['location']['shape']['links'][j]['points'][k]['lat']))
#                 lo.append(float(JSON['results'][i]['location']['shape']['links'][j]['points'][k]['lng']))
#                 su1.append(float(su))
#                 ff1.append(float(ff))

#             lats.append(la)
#             longs.append(lo)
#             sus.append(np.mean(su1))
#             ffs.append(np.mean(ff1))

#     fig=plt.figure()
#     plt.style.use('dark_background')
#     # plt.plot(np.linspace(0,10,10),np.linspace(0,10,10))
#     plt.grid(False)
#     for i in range(0,len(lats)):
#         if(sus[i]/ffs[i]<0.25):
#             plt.plot(longs[i],lats[i], c='brown',linewidth=0.5)
#         elif(sus[i]/ffs[i]<0.5):
#             plt.plot(longs[i],lats[i], c='red',linewidth=0.5)
#         elif(sus[i]/ffs[i]<0.75):
#             plt.plot(longs[i],lats[i], c='yellow',linewidth=0.5)
#         else:
#             plt.plot(longs[i],lats[i], c='green',linewidth=0.5)
#         #print(i)
#     #plt.xlim(-77.055,-77.015)
#     #plt.ylim(38.885,38.91)
#     plt.axis('off')
#     plt.show()

# if __name__ == "__main__":
#     schedule.every(2).seconds.do(func)
#     while True:
#         schedule.run_pending()


request = requests.get("https://data.traffic.hereapi.com/v7/flow?in=circle:30.9010167,75.9094733;r=200&locationReferencing=shape&apiKey=jpCatShkVUwcTW9tvl30gEghCIdXxOrNA0TXplvm2oE")
request_text = request.text
JSON = json.loads(request_text)

resultCount = len(JSON['results'])
# print(len(JSON['results']))
# print(len(JSON['results'][0]['location']['shape']['links'][0]['points']))
# print(len(JSON['results'][0]['location']['shape']['links']))
lats=[]
longs=[]
sus=[]
ffs=[]

for i in range(0, resultCount):
    su = float(JSON['results'][i]['currentFlow']['speed'])
    ff = float(JSON['results'][i]['currentFlow']['freeFlow'])
    for j in range(0, len(JSON['results'][i]['location']['shape']['links'])):
        la = []
        lo = []
        su1 = []
        ff1 = []
        for k in range(0, len(JSON['results'][i]['location']['shape']['links'][j]['points'])):
            la.append(float(JSON['results'][i]['location']['shape']['links'][j]['points'][k]['lat']))
            lo.append(float(JSON['results'][i]['location']['shape']['links'][j]['points'][k]['lng']))
            su1.append(float(su))
            ff1.append(float(ff))

        lats.append(la)
        longs.append(lo)
        sus.append(np.mean(su1))
        ffs.append(np.mean(ff1))

fig=plt.figure()
plt.style.use('dark_background')
# plt.plot(np.linspace(0,10,10),np.linspace(0,10,10))
plt.grid(False)
for i in range(0,len(lats)):
    if(sus[i]/ffs[i]<0.25):
        plt.plot(longs[i],lats[i], c='brown',linewidth=0.5)
    elif(sus[i]/ffs[i]<0.5):
        plt.plot(longs[i],lats[i], c='red',linewidth=0.5)
    elif(sus[i]/ffs[i]<0.75):
        plt.plot(longs[i],lats[i], c='yellow',linewidth=0.5)
    else:
        plt.plot(longs[i],lats[i], c='green',linewidth=0.5)
    #print(i)
#plt.xlim(-77.055,-77.015)
#plt.ylim(38.885,38.91)
plt.axis('on')
plt.show()       
