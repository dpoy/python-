'''
CHANGELOG
0.8:
    完成登录后查询部分
1.0:
    实现登录功能
1.1:
    实现部分输入异常处理
1.2:
    实现登录过程异常处理
    优化Cookies兼容性
1.5:
    优化程序逻辑
    引入函数
1.6:
    去除不必要的OCR相关import
    将学年学期选择转为函数xnxq()
'''

import requests
from PIL import Image
import base64
from bs4 import BeautifulSoup

print('\n============================================')
print('\n　华东理工大学综合教务管理系统自动成绩查询\n')
print('============================================\n')


def auth():
    username_o = input('请输入用户名：')
    password_o = input('请输入密码：')
    # 用户名密码
    username = base64.b64encode(username_o.encode('utf-8'))
    password = base64.b64encode(password_o.encode('utf-8'))
    # 转码字符串到Byte，用Base64编码
    username = str(username, 'utf-8')
    password = str(password, 'utf-8')
    # 转回Unicode
    return [username, password]


def xnxq():
    try:
        while True:
            global yr
            global yr2
            global sm
            yr = int(input('请输入学年的起始年（如2017-2018学年，输入2017即可）：'))
            if yr < 2000 or yr > 9999:
                print('年份输对了吗？')
            else:
                break
        yr2 = yr + 1
        yr = str(yr)
        yr2 = str(yr2)
        while True:
            sm = str(input('请输入学期数（1或2）：'))
            if sm == '1' or sm == '2':
                break
            else:
                print('一学年只有两学期吧？')
        xnxq = yr + '-' + yr2 + '-' + sm
        return xnxq
    except:
        print('好好打字！')


def login():
    global headers
    global postData
    global cookie
    print('\n正在尝试连接教务处网站……')
    try:
        Url = 'http://inquiry.ecust.edu.cn/jsxsd/'
        r = requests.get(Url)
    except WindowsError:
        print('连不上，应该是教务处网站又挂了……过会试试？')
        input('按下回车继续尝试')
        Url = 'http://inquiry.ecust.edu.cn/jsxsd/'
        r = requests.get(Url)
    else:
        print('连接成功。')
        JSESSIONID = r.cookies['JSESSIONID']
        SERVERID = r.cookies['SERVERID']
        # 获取Cookies

    CaptchaUrl = "http://inquiry.ecust.edu.cn/jsxsd/verifycode.servlet"
    PostUrl = "http://inquiry.ecust.edu.cn/jsxsd/xk/LoginToXk"
    # 验证码和Post地址

    cookie = r.cookies。

    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'SERVERID=' + SERVERID + '; JSESSIONID=' + JSESSIONID,
        'Host': 'inquiry.ecust.edu.cn',
        'Origin': 'http://inquiry.ecust.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://inquiry.ecust.edu.cn/jsxsd/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
    }
    # 根据抓包信息 构造headers

    vimage = requests.get(CaptchaUrl, headers=headers, cookies=cookie)
    # 使用requests获取验证
    local = open('D:/vimage.jpg', 'wb')
    local.write(vimage.content)
    local.close()
    # 保存验证码到本地
    print('\n请查看D:\vimage.jpg')
    vcode = input('\n请输入验证码： ')
    while True:
        if vcode != '':
            break
        else:
            print('验证码不能为空！')
            vcode = input('\n请输入验证码： ')
    vcode = vcode.lower()
    # 转成全小写

    global username
    global password
    encoded = username + '=%%%' + password
    # print(encoded)
    postData = {
        'encoded': encoded,
        'RANDOMCODE': vcode,
    }
    # 构造postData

    PostUrl = PostUrl + '?encoded=' + encoded + '&RANDOMCODE=' + vcode
    r = requests.post(PostUrl, headers=headers, data=postData, cookies=cookie)
    r.cookies = cookie
    # 登录

    soup = BeautifulSoup(r.text, 'html.parser')
    while True:
        if soup.find(text='验证码错误!!') == '验证码错误!!':
            print('\n验证码错误，请重新登录')
            return 1
        elif soup.find(text='用户名或密码错误') == '用户名或密码错误':
            print('\n用户名或密码错误\n')
            username, password = auth()
            return 1
        else:
            print('\n登录成功！\n')
            return 0


def ScoreInq():
    ## MainUrl = 'http://inquiry.ecust.edu.cn/jsxsd/kscj/cjcx_query'
    ## r = requests.get(MainUrl, headers = headers, data = postData, cookies=r.cookies)
    InqUrl = 'http://inquiry.ecust.edu.cn/jsxsd/kscj/cjcx_list'
    InqUrl = InqUrl + '?kksj=' + xnxq() + '&kcxz=&kcmc=&xsfs=all'

    print('\n==============================')
    print('\n查询' + yr + '-' + yr2 + '学年第' + sm + '学期的成绩\n')
    print('================================')

    resp3 = requests.get(InqUrl, headers=headers, cookies=cookie)
    data = resp3.text
    # 查成绩

    soup = BeautifulSoup(data, "html.parser")
    tables = soup.find_all('table')

    tab = tables[1]
    print('\n【执行计划内课程】\n')
    tds = tab.find_all('td')
    # 找到成绩列表的第一项
    index = 2
    while index <= len(tds):
        print('名称：' + tds[index].getText())  # 名称
        index += 2
        print('学分：' + tds[index].getText())  # 学分
        index += 1
        print('属性：' + tds[index].getText())  # 属性
        index += 5
        print('成绩：' + tds[index].getText())  # 成绩
        index += 1
        print('绩点：' + tds[index].getText())  # 绩点
        index += 5
        print('')

    tab = tables[2]
    print('--------------------------------')
    print('\n【执行计划外课程】\n')
    tds = tab.find_all('td')
    # 找到成绩列表的第一项
    index = 2
    while index <= len(tds):
        print('名称：' + tds[index].getText())  # 名称
        index += 2
        print('学分：' + tds[index].getText())  # 学分
        index += 1
        print('属性：' + tds[index].getText())  # 属性
        index += 5
        print('成绩：' + tds[index].getText())  # 成绩
        index += 1
        print('绩点：' + tds[index].getText())  # 绩点
        index += 3
        print('')

    print('==============================')
    print('　　　　查　询　完　成　　　　')
    print('==============================')
    print('\n输入0查询其他学期')
    print('输入1退出成绩查询')
    op = input('\n请输入：')
    return op


def CourseInq():
    import xlwt
    InqUrl = 'http://inquiry.ecust.edu.cn/jsxsd/xskb/xskb_list.do'
    xnxq = xnxq()
    InqUrl = InqUrl + '?xnxq01id=' + xnxq

    print('\n==============================')
    print('\n查询' + yr + '-' + yr2 + '学年第' + sm + '学期的成绩\n')
    print('================================')

    resp3 = requests.get(InqUrl, headers=headers, cookies=cookie)
    data = resp3.text
    # 查课表


##    soup = BeautifulSoup(data, "html.parser")
##    tables = soup.find_all('table')
##
##    tab = tables[1]
##    print('\n【课程表】\n')
##    tds = tab.find_all('td')
##    # 找到课程表的第一格
##    index = 0
##    while index <= len(tds):
##        print(tds[index].getText()) # 代码未完成
##        index += 1
##    此部分代码未完成

# 以下是主程序

username, password = auth()
while login() == 1:
    pass
# 登录过程

print('1. 查询成绩')
call = input('请输入您想进行的操作：')
# 功能选单

if call == '1':
    while True:
        op = ScoreInq()
        if op == '1':
            break
elif call == '2':
    print('Function still under construction.')