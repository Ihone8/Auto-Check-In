# !usr/bin/env python
# _*_coding:utf-8 _*_

import  requests
import datetime
import time
import re

from threading import Timer
from datetime import datetime




def Sign():
    #Cookie
    cookie = {
            'Cookie': 'chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; UM_distinctid=165e76722881-0a41a1cd64e627-50422618-100200-165e767228a9; pgv_pvi=2426425344; pgv_si=s4797890560; __jsluid=d251aabf2c5b9f4e4b68a2ff1fb5399a; CNZZDATA1262179880=667623201-1537187022-%7C1537187022; Hm_lvt_9104989ce242a8e03049eaceca950328=1537188015; Hm_lvt_1a32f7c660491887db0960e9c314b022=1537188016; aUZ1_2132_saltkey=IPsAT7so; aUZ1_2132_lastvisit=1537185621; Hm_lvt_2d0601bd28de7d49818249cf35d95943=1537185622,1537190825; ci_session=92a44f0be5acce92464175d5d6d84a4163850e49; Hm_lpvt_2d0601bd28de7d49818249cf35d95943=1537191228; aUZ1_2132_sendmail=1; Hm_lpvt_9104989ce242a8e03049eaceca950328=1537191317; Hm_lpvt_1a32f7c660491887db0960e9c314b022=1537191317; aUZ1_2132_auth=f1e8ECA5dTLKTwkpZsKZTXXPneE0hXdKWpX2lVJRmyksAeQC; aUZ1_2132_sid=uZZnOK; aUZ1_2132_connect_is_bind=0; aUZ1_2132_security_cookiereport=3f3bG5IZQxcSMsWLpxn43UKFJWRcZr3Tr6gaC5zyhEzoOmTJ0qnD; aUZ1_2132_ulastactivity=6bae71Thjge7wiIGCFFJ3WZwi2wRjSofNyub0%2Bnw38%2FE%2BSgosdsh; Hm_lvt_a05b2675ca344b30c2cc9dc221706782=1537188006,1537188074,1537188145,1537191331; aUZ1_2132_lastcheckfeed=366647%7C1537191332; Hm_lpvt_a05b2675ca344b30c2cc9dc221706782=1537191340; aUZ1_2132_lastact=1537191377%09plugin.php%09; aUZ1_2132_creditbase=0D1D1D1D0D0D0D0D0; aUZ1_2132_creditnotice=0D1D19D2D0D0D0D0D0D366647; aUZ1_2132_creditrule=%E5%8F%91%E8%A1%A8%E4%B8%BB%E9%A2%98'
    }
    # 请求头
    header = {
    'Host': 'bbs.ichunqiu.com',
    'Referer': 'https://bbs.ichunqiu.com/plugin.php?id=dsu_paulsign:sign',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
        }
    Url = 'https://bbs.ichunqiu.com/plugin.php?id=dsu_paulsign:sign'


    s  = requests.get(url= Url,cookies = cookie, headers = header)

    req = re.compile(r'<input type="hidden" name="formhash" value="(.*?)" />')
    value = re.findall(req,s.text)  # 身份验证
    #print(value[0])
    sign_url = 'https://bbs.ichunqiu.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
    sign_payload = {
            'formhash': value[0],
            'qdxq': 'fd',
            'qdmode': '2',
            'todaysay': 'qiandao',
            'fastreply': 0,
    }
    sign_req = requests.post(url= sign_url,cookies = cookie, headers = header,data=sign_payload)
    #print(sign_req.text)
    nowTime= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt','a') as f:
            if '签到成功' in sign_req.text:
                  f.write('*********-------------***************\n')
                  f.write(nowTime+'\n')
                  f.write('签到成功。。\n')
                  f.write('*********-------------***************\n')
            elif '您今日已经签到，请明天再来！' in sign_req.text:
                f.write('*********-------------***************\n')
                f.write(nowTime + '\n')
                f.write('您今日已经签到，请明天再来。。\n')
                f.write('*********-------------***************\n')
            else:
                f.write('*********-------------***************\n')
                f.write(nowTime + '\n')
                f.write('出现错误。。。。\n')
                f.write('*********-------------***************\n')



if __name__== '__main__':
    # 死循环  60 秒一次
        while True:
            Sign()
            time.sleep(60)
      

