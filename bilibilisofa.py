#!/usr/bin/env python
#-*- coding:utf-8 -*-

import bilibili
import time
#================================================
upDict={
    '221648':'柚子木',
    '433351':'老E',
    '883968':'暴走漫画',
    '2949989':'电喵',
    '1293653':'萱框框',
  '928334':'SaSa',
    '423895':'老菊'
}

avList=[]
#=================================================
delayTime = 20 #秒
flag = False
#=================================================
bilibili.Init()
for up in upDict.keys():
        avList.append(bilibili.getOneDynamic(up).keys()[0])

print '[+]初始化完毕'+str(avList)

while True:
    a = time.clock()
    for up in upDict.keys():
        av = bilibili.getOneDynamic(up).keys()[0]
        if av not in avList:
            bilibili.addConment(av)
            avList.append(av)

    now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time())))
    print '[+]'+now
    b = time.clock()
#   print b-a
    time.sleep(delayTime)    



#=================================================
avList = bilibili.getDynamic().keys()

while True:
    now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time())))
    print '[+]'+now
    
    videoDict = bilibili.getDynamic()#key:av,value:up
    for av in videoDict.keys():
        if av not in avList:
            if videoDict[av] in upDict.keys():
                bilibili.addConment(av)
                avList.append(av)

    time.sleep(delayTime)
    


