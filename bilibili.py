#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import json
import time
import cookielib
import urllib2
import urllib
#==============================================
message='看我刷出了什么...'
DmMessage='hahaha'
av='4043969'
cid='6523668'
DedeUserID=''
DedeUserID__ckMd5=''
SESSDATA=''
sid=''
#==============================================
null = ''
false = 'false'
true = 'true'
#==============================================
Login_URL = 'https://passport.bilibili.com/ajax/miniLogin/login'
Conment_URL = 'http://api.bilibili.com/x/reply/add'
Dynamic_URL = 'http://api.bilibili.com/x/feed/pull?callback=jQuery17207111566021762926_1456248357868&jsonp=jsonp&ps=5&type=0&pn=1&_=1456248364238'
upDynamic_URL = 'http://space.bilibili.com/ajax/member/getSubmitVideos?tid=0&mid='
Dm_URL = 'http://interface.bilibili.com/dmpost?cid='+cid+'&aid='+av+'&pid=1' #post
oneDynamicURL = 'http://space.bilibili.com/ajax/member/getSubmitVideos?pagesize=1&tid=0&keyword=&page=1&mid=' #get
#==============================================
Header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Origin' : 'http://www.bilibili.com',
        'Cookie' :'',
        'Connection' : 'keep-alive' 
}
Login_Data = {
        'keep': 0,
        'userid': '',
        'pwd': '',
        'captcha': ''
}
#==============================================
Conment_Data ={
    'jsonp':'jsonp',
    'message':message,
    'type':'1',
    'plat':'1',
#    'oid': av
    'oid': ''    
}

#================================================
Dynamic_Header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'pgv_pvi=9559737344; fts=1452313082; PLHistory=8eJ0%7ComCBZ; DedeID=3933618; uTZ=-480; loveplus=1; user_face=http%3A%2F%2Fstatic.hdslb.com%2Fimages%2Fmember%2Fnoface.gif; LIVE_BUVID=d237db3f309cfc0c1b759bfcc9612883; LIVE_BUVID__ckMd5=6979057eee2ea432; DedeUserID=9353541; DedeUserID__ckMd5=74df5d910dab6c83; SESSDATA=63e05447%2C1457792069%2C18f8de74; LIVE_LOGIN_DATA=139d2d42dc1c5ef14b431d5a4c22c1d3cc4cf006; LIVE_LOGIN_DATA__ckMd5=d667676404113142; _cnt_dyn=null; _cnt_pm=0; _cnt_notify=21; _dfcaptcha=73b9ffb3ab6549e052c6371f729b4fcf; rlc_time=1456237928841; sid=7r2u06a0; pgv_si=s3359137792',
    'Connection': 'keep-alive'

}
#==============================================
Dm_Header={
}

Dm_Data1={
        'color':'16777215',
        'playTime':'10',#+'%2E'+'215',#秒+微秒
        'fontsize':'25',
        'pool':'0',
        'rnd':'1250550860',
        'cid':cid,
        'mode':'1',
        'date':'2016%2D03%2D07%2021%3A30%3A57',
        'message':DmMessage
}

Dm_Data='color=16777215&playTime=19%2E256&fontsize=25&rnd=192738422&pool=0&cid='+cid+'&mode=1&date=2016%2D03%2D07%2023%3A16%3A35&message='+DmMessage
#==============================================
def Init():
        global Header
        Login()
        Header['Cookie']='sid='+sid+'; DedeUserID='+DedeUserID+'; DedeUserID__ckMd5='+DedeUserID__ckMd5+'; SESSDATA='+SESSDATA+';'
#==============================================
def Login():
        global DedeUserID
        global DedeUserID__ckMd5
        global SESSDATA
        global sid
        
        Login_Data['userid'] = raw_input('[+]User Name: ')
        Login_Data['pwd'] = raw_input('[+]Password: ')
        
        cookieBox = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieBox))
        data = urllib.urlencode(Login_Data)
        req = urllib2.Request(Login_URL,data=data,headers=Header)
        resp = opener.open(req)
        html = resp.read()
        html = json.loads(html.decode('utf-8'))
        if html['status']:
            print('[+]登陆成功！')
            for i in cookieBox:
                if i.name == 'DedeUserID':DedeUserID = i.value
                if i.name == 'DedeUserID__ckMd5':DedeUserID__ckMd5 = i.value
                if i.name == 'SESSDATA':SESSDATA = i.value
                if i.name == 'sid':sid = i.value
        else:
            print(html)
            print('[+]账号或密码错误！')
#===============================================
def setMessage():
        global message
        global Conment_Data
        message = raw_input('[+]设置评论为:')
        message = message.decode('gbk').encode('utf-8')
        print '[+]评论为'+ message
        Conment_Data['message'] = message
#==============================================
def addConment(av):
        global Conment_Data
        global null
        global false
        global true
        
        av = str(av)
        
        Conment_Data['oid']=av

        Conment_Req =requests.post(Conment_URL,data=Conment_Data,headers=Header)#Conment_Header)
        text = eval(Conment_Req.text)
        code = text['code']
        
        if code == 0:
                print '[+]【评论成功】'+'在av'+av+'中评论：'+Conment_Data['message']
        else:
                print '[+]【评论失败】'

#==================================================
def getDynamic():
    global Dynamic_Header
    global null
    global false
    global true
    
    Dynamic_Req =requests.get(Dynamic_URL,headers=Dynamic_Header)
    s = json.loads(json.dumps(eval(Dynamic_Req.text[41:-1])))
#    print 'av' + str(s['data']['feeds'][0]['add_id']) +'||'+'up'+ str(s['data']['feeds'][0]['src_id'])
#    print '#=================='
#    print 'av' + str(s['data']['feeds'][1]['add_id']) +'||'+'up'+ str(s['data']['feeds'][1]['src_id'])
#    print '#=================='
#    print 'av' + str(s['data']['feeds'][2]['add_id']) +'||'+'up'+ str(s['data']['feeds'][2]['src_id'])

    videoDict ={} #key:av,value:up
    for num in range(3):
        videoDict[str(s['data']['feeds'][num]['add_id'])] = str(s['data']['feeds'][num]['src_id'])

    return videoDict

def getUpDynamic(up):#返回单元素字典，key：av，value：title
    global upDynamic_Header
    global upDynamic_URL
    global null
    global false
    global true

    up = str(up)
    up_URL = upDynamic_URL + up
    Dynamic_Req =requests.get(up_URL,headers=Header)
    s = json.loads(json.dumps(eval(Dynamic_Req.text)))
    av = str(s['data']['vlist'][0]['aid'])
    title = str(s['data']['vlist'][0]['title']).decode("unicode_escape")
    
#    print 'av' + str(s['data']['vlist'][0]['aid']) +'||'+'up'+up+str(s['data']['vlist'][0]['author']).decode("unicode_escape") +'||'+'title:'+ str(s['data']['vlist'][0]['title']).decode("unicode_escape")

    return {av:title}


def getOneDynamic(up):
        up_URL = oneDynamicURL + str(up)
        oneDynamic = requests.get(up_URL,headers=Header)

        s = oneDynamic.json()
        av = str(s['data']['vlist'][0]['aid'])
        title = s['data']['vlist'][0]['title']

        return {av:title}
#===============================================================================
def SendDm():
        Dm_Req =requests.post(Dm_URL,data=Dm_Data,headers=Dm_Header)#Header)#
        print Dm_Req.text

if __name__ == '__main__':
        pass
