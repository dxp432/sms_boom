import datetime
import math
import win32api
import win32con
import time
import ctypes
import webbrowser
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import cv2
import numpy as np
import aircv as ac
import time
from PIL import ImageGrab


# 单击
def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    time.sleep(1)


# 滑动图块
def slip_pic(x, y, x_1, y_1):
    my_x_1_half = (x_1 - x)
    # my_x_2 = x + my_x_1_half
    # my_x_3 = x + my_x_1_half + my_x_1_half
    print(math.ceil(float(my_x_1_half)))
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(1)
    track_list = get_track(my_x_1_half)
    for track in track_list:
        x = x + track
        # print('for: track is ' + str(x))
        m.move(int(x), y_1)
        time.sleep(0.02)
    # m.move(int(my_x_2), y_1)
    # time.sleep(1)
    # m.move(int(my_x_3), y_1)
    # time.sleep(2)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    time.sleep(1)


# 双击
def double_click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    # https://blog.csdn.net/zhanglidn013/article/details/35988381
    # https://docs.microsoft.com/zh-cn/windows/desktop/inputdev/virtual-key-codes
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    time.sleep(0.2)


# 按下一个按钮
def press_one_key(key1):
    ctypes.windll.user32.keybd_event(key1, 0, 0, 0)
    # https://blog.csdn.net/zhanglidn013/article/details/35988381
    # https://docs.microsoft.com/zh-cn/windows/desktop/inputdev/virtual-key-codes
    ctypes.windll.user32.keybd_event(key1, 0, win32con.KEYEVENTF_KEYUP, 0)


# 关闭浏览器
def ctrl_w():
    time.sleep(2)
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(87, 0, 0, 0)
    win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    # print('ctrl_w')
    time.sleep(1)


# 打开浏览器
# webbrowser.open(url, new=0, autoraise=True)
# 在系统的默认浏览器中访问url地址，
# 如果new = 0, url会在同一个 浏览器窗口中打开；
# 如果new = 1，新的浏览器窗口会被打开;
# 如果new = 2 新的浏览器tab会被打开
def web_open(url):
    webbrowser.open(url, new=0)
    time.sleep(4)


# 模拟键盘输入字符串
def string_input(my_string):
    k.type_string(my_string)
    time.sleep(1)


# def youku_sms(my_phone_num):
#     # 点击手机输入框
#     click(1000, 400)
#     # 模拟键盘输入手机号
#     string_input(my_phone_num)
#     # 点击密码输入框
#     click(919, 462)
#     # 模拟键盘输入密码
#     string_input('tringidkde123')
#     # 点击密码确认输入框
#     click(905, 526)
#     # 模拟键盘输入密码
#     string_input('tringidkde123')
#     # 点击获取验证码
#     click(1042, 591)
#     # 关闭浏览器窗口
#     ctrl_w()


def acfun_sms(my_phone_num):
    # 点击手机输入框
    click(1233, 281)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击改变焦点
    click(1800, 510)
    # 点击获取验证码
    click(1332, 510)
    # 关闭浏览器窗口
    ctrl_w()


#
# def sina_sms(my_phone_num):
#     # 点击手机输入框
#     click(784, 266)
#     # 模拟键盘输入手机号
#     string_input(my_phone_num)
#     # 选择兴趣标签
#     click(707, 378)
#     # 选择密码框
#     click(716, 336)
#     # 模拟键盘输入密码
#     string_input('tringidkde123')
#     # 点击获取验证码
#     click(772, 438)
#     # 关闭浏览器窗口
#     ctrl_w()


def wy37_sms(my_phone_num):
    # 点击登录
    click(1420, 85)
    # 点击手机登录
    click(1152, 421)
    # 点击手机号输入框
    click(1039, 478)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1176, 479)
    # 关闭浏览器窗口
    ctrl_w()


def hupu_sms(my_phone_num):
    # 点击手机号输入框
    click(929, 359)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击智能验证
    click(940, 424)
    time.sleep(5)
    # 点击获取验证码
    click(1058, 511)
    # 关闭浏览器窗口
    ctrl_w()


def hongheng_sms(my_phone_num):
    # 点击手机号输入框
    click(1179, 273)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1350, 334)
    # 再点击获取验证码，以确保真正获取验证码
    click(1350, 334)
    # 关闭浏览器窗口
    ctrl_w()


def job51_sms(my_phone_num):
    # 点击验证码登录模块
    click(1174, 284)
    # 点击手机号输入框
    click(981, 382)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1242, 476)
    # 关闭浏览器窗口
    ctrl_w()


def zhipin_sms(my_phone_num):
    # 点击注册
    click(1209, 761)
    # 滑动滑块
    slip_pic(934, 555, 1212, 555)
    # 点击手机号输入框
    click(1029, 480)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1177, 628)
    # 关闭浏览器窗口
    ctrl_w()


def kanzhun_sms(my_phone_num):
    # 点击短信登录
    click(1029, 413)
    # 滑动滑块
    slip_pic(817, 515, 1107, 515)
    # 点击手机号输入框
    click(897, 446)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1068, 581)
    # 关闭浏览器窗口
    ctrl_w()


def xueqiu_sms(my_phone_num):
    # 点击登录
    click(1357, 98)
    # 点击短信
    click(816, 433)
    # 点击手机号输入框
    click(912, 489)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1095, 489)
    # 关闭浏览器窗口
    ctrl_w()


def lvmama_sms(my_phone_num):
    # 点击手机验证码登录
    click(1370, 214)
    # 点击手机号输入框
    click(1178, 286)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1370, 340)
    # 关闭浏览器窗口
    ctrl_w()


def itjuzi_sms(my_phone_num):
    # 点击手机验证码登录
    click(1053, 314)
    # 点击手机号输入框
    click(871, 417)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1119, 500)
    # 再次点击获取验证码，确保点中
    click(1119, 500)
    # 点击智能检测
    click(1119, 500)
    # 关闭浏览器窗口
    ctrl_w()


def sspai_sms(my_phone_num):
    # 点击登录
    click(1473, 100)
    # 点击注册
    click(1039, 657)
    # 点击手机号输入框
    click(866, 417)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1076, 698)
    # 滑动滑块
    slip_pic(800, 730, 1111, 730)
    # 关闭浏览器窗口
    ctrl_w()


def woodo_sms(my_phone_num):
    # 点击注册
    click(1232, 666)
    # 点击手机注册
    click(1194, 337)
    # 点击手机号输入框
    click(1143, 393)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1264, 442)
    # 再次点击获取验证码
    click(1264, 442)
    # 关闭浏览器窗口
    ctrl_w()


def uzer_sms(my_phone_num):
    # 点击手机号输入框
    click(839, 476)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1058, 476)
    # 再次点击获取验证码
    click(1058, 476)
    # 关闭浏览器窗口
    ctrl_w()


def rabbitpre_sms(my_phone_num):
    # 点击注册
    click(1515, 100)
    # 点击手机注册
    click(968, 679)
    # 点击手机号输入框
    click(848, 468)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1054, 525)
    # 再次点击获取验证码
    click(1054, 525)
    # 关闭浏览器窗口
    ctrl_w()


def zcool_sms(my_phone_num):
    # 点击手机号输入框
    click(900, 351)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    slip_pic(814, 409, 1111, 409)
    # 焦点离开输入框（点击空白处），激活验证码
    click(610, 406)
    # 点击获取验证码
    click(973, 467)
    # 再次点击获取验证码
    click(973, 467)
    # 关闭浏览器窗口
    ctrl_w()


def pic58_sms(my_phone_num):
    # 点击手机注册
    click(1260, 555)
    # 点击手机号输入框
    click(1463, 361)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    slip_pic(1301, 424, 1578, 424)
    # 点击获取验证码
    click(1547, 484)
    # 再次点击获取验证码
    click(1547, 484)
    # 关闭浏览器窗口
    ctrl_w()


def tuchong_sms(my_phone_num):
    # 点击注册
    click(1791, 127)
    # 点击非二维码输入框
    click(1388, 320)
    # 点击手机输入框
    click(1068, 424)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1311, 500)
    # 再次点击获取验证码
    click(1311, 500)
    # 关闭浏览器窗口
    ctrl_w()


def cli_sms(my_phone_num):
    # 点击注册
    click(1513, 100)
    # 点击手机输入框
    click(672, 542)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(826, 590)
    # 关闭浏览器窗口
    ctrl_w()


def yun163_sms(my_phone_num):
    # 点击手机输入框
    click(832, 389)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击智能验证
    click(1057, 455)
    # 点击获取验证码
    click(1056, 518)
    # 关闭浏览器窗口
    ctrl_w()


def my_22_sms(my_phone_num):
    # 点击空白区域
    click(1300, 462)
    # 点击手机输入框
    click(930, 462)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击空白区域
    click(1300, 462)
    # 点击获取验证码
    click(1110, 516)
    time.sleep(4)
    for my_index in range(1, 6, 1):
        my_find_x_f = get_find_x()
        if my_find_x_f == 0:
            print('my_find_x_f is 0')
            # 点击刷新
            click(1075, 712)
            time.sleep(2)
        else:
            print(my_find_x_f)
            my_int = 849 + 52 + math.ceil(float(my_find_x_f))
            slip_pic(849, 666, int(my_int), 666)
            print('滑动了，跳出循环')
            break
    print('已经跳出循环')
    # 关闭浏览器窗口
    ctrl_w()


def qiyu_sms(my_phone_num):
    # 点击手机输入框
    click(857, 417)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击智能验证
    click(937, 479)
    time.sleep(3)
    # 点击获取验证码
    click(1086, 545)
    # 关闭浏览器窗口
    ctrl_w()

def get_find_x():
    screen_grab()
    canny()
    find_x = 0
    try:
        if matchImg('yzm_screencap.png', '1.png') is not None:
            print("1！")
            find_x = str(matchImg('yzm_screencap.png', '1.png')['result'][0])
        elif matchImg('yzm_screencap.png', '2.png') is not None:
            print("2！")
            find_x = str(matchImg('yzm_screencap.png', '2.png')['result'][0])
        elif matchImg('yzm_screencap.png', '3.png') is not None:
            print("3！")
            find_x = str(matchImg('yzm_screencap.png', '3.png')['result'][0])
        elif matchImg('yzm_screencap.png', '4.png') is not None:
            print("4！")
            find_x = str(matchImg('yzm_screencap.png', '4.png')['result'][0])
        elif matchImg('yzm_screencap.png', '5.png') is not None:
            print("5！")
            find_x = str(matchImg('yzm_screencap.png', '5.png')['result'][0])
        elif matchImg('yzm_screencap.png', '6.png') is not None:
            print("6！")
            find_x = str(matchImg('yzm_screencap.png', '6.png')['result'][0])
        elif matchImg('yzm_screencap.png', '7.png') is not None:
            print("7！")
            find_x = str(matchImg('yzm_screencap.png', '7.png')['result'][0])
        else:
            find_x = 0
            print('没有匹配,find_x is :' + str(find_x))
    except Exception as e:
        print(e)
        print("这里有个异常")
    return find_x


# 对比两张图，找到坐标。
def matchImg(imgsrc, imgobj):
    # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj, 0.5)
    # 0.9、confidence是精度，越小对比的精度就越低 {'confidence': 0.5435812473297119,
    # 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.alipay_leave0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
    return match_result


def screen_grab():
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    bbox = (900, 420, 1129, 611)
    im = ImageGrab.grab(bbox)
    # 参数 保存截图文件的路径
    im.save('yzm_screencap.png')


def canny():
    # 读入图像
    lenna = cv2.imread("yzm_screencap.png", 0)
    # 图像降噪
    lenna = cv2.GaussianBlur(lenna, (5, 5), 0)
    # Canny边缘检测，50为低阈值low，150为高阈值high
    canny = cv2.Canny(lenna, 150, 190)
    cv2.imwrite('yzm_screencap.png', canny)


def get_track(distance):
    # 拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    # 匀变速运动基本公式：
    # ①v=v0+at
    # ②s=v0t+(1/2)at²
    # ③v²-v0²=2as
    #
    # :param distance: 需要移动的距离
    # :return: 存放每0.2秒移动的距离
    # 初速度
    v = 0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t = 0.1
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks = []
    # 当前的位移
    current = 0
    # 到达mid值开始减速
    mid = distance * 4 / 5

    distance += 10  # 先滑过一点，最后再反着滑动回来

    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = 2  # 加速运动
        else:
            a = -3  # 减速运动

        # 初速度
        v0 = v
        # 0.2秒时间内的位移
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))

        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t

    # 反着滑动到大概准确位置
    for i in range(3):
        tracks.append(-2)
    for i in range(4):
        tracks.append(-1)
    return tracks


def booking_sms(my_phone_num):
    # 点击手机输入框
    click(920, 424)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1071, 501)
    # 关闭浏览器窗口
    ctrl_w()


def sogou_sms(my_phone_num):
    # 点击手机输入框
    click(1229, 361)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1439, 418)
    time.sleep(4)
    for my_index in range(1, 6, 1):
        my_find_x_f = get_find_x()
        if my_find_x_f == 0:
            print('my_find_x_f is 0')
            # 点击刷新
            click(1075, 712)
            time.sleep(2)
        else:
            print(my_find_x_f)
            my_int = 849 + 52 + math.ceil(float(my_find_x_f))
            slip_pic(849, 666, int(my_int), 666)
            print('滑动了，跳出循环')
            break
    print('已经跳出循环')
    # 关闭浏览器窗口
    ctrl_w()


def gfan_sms(my_phone_num):
    # 点击手机输入框
    click(1231, 556)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1415, 603)
    # 关闭浏览器窗口
    ctrl_w()


def d_sms(my_phone_num):
    # 点击手机输入框
    click(792, 305)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    click(796, 387)
    # 模拟键盘输入密码
    string_input('tringidkde123')
    click(816, 493)
    # 点击获取验证码
    click(963, 634)
    # 关闭浏览器窗口
    ctrl_w()


def changba_sms(my_phone_num):
    # 滑动滑块
    slip_pic(890, 422, 1088, 422)
    # 点击手机号输入框
    click(893, 308)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1051, 366)
    # 关闭浏览器窗口
    ctrl_w()


def eoemarket_sms(my_phone_num):
    # 点击
    click(1479, 104)
    # 点击手机输入框
    click(874, 218)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1047, 295)
    # 点击获取验证码
    click(1047, 295)
    time.sleep(4)
    for my_index in range(1, 6, 1):
        my_find_x_f = get_find_x()
        if my_find_x_f == 0:
            print('my_find_x_f is 0')
            # 点击刷新
            click(1075, 712)
            time.sleep(2)
        else:
            print(my_find_x_f)
            my_int = 849 + 52 + math.ceil(float(my_find_x_f))
            slip_pic(849, 666, int(my_int), 666)
            print('滑动了，跳出循环')
            break
    print('已经跳出循环')
    # 关闭浏览器窗口
    ctrl_w()


def credit_sms(my_phone_num):

    # 点击手机号输入框
    click(447, 306)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(695, 372)
    # 关闭浏览器窗口
    ctrl_w()


def j5i_sms(my_phone_num):
    click(1527, 99)
    # 点击手机号输入框
    click(834, 448)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1059, 448)
    # 关闭浏览器窗口
    ctrl_w()


if __name__ == '__main__':
    # 定义鼠标键盘实例
    k = PyKeyboard()
    m = PyMouse()

    # 手机号
    my_phone = input("请输入手机号(然后回车):")


    # 打开浏览器的一个窗口，始终保持有一个窗口，就不怕chrome就被关闭了。
    # web_open('http://www.hao123.com')
    my_time = datetime.datetime.now()

    while 1 == 1:
        my_time = datetime.datetime.now()
        # 定时
        if (my_time.hour == 7) or (my_time.hour == 15):

            print('-----开始-----' + str(datetime.datetime.now()))

            # 豆瓣
            # 迅雷13988715878
            # 优酷
            # 新浪注册
            # 华军软件园
            # 中华英才网

            # 我爱我家
            web_open('https://bj.5i5j.com/')
            j5i_sms(my_phone)

            # 我爱卡
            web_open('https://h5.51credit.com/www/login/regist.html')
            credit_sms(my_phone)

            # eoemarket_sms
            web_open('http://www.eoemarket.com/')
            eoemarket_sms(my_phone)

            # 唱吧
            web_open('https://changba.com/official_login.php')
            changba_sms(my_phone)

            # 当乐网
            web_open('https://oauth.d.cn/auth/goRegister.html')
            d_sms(my_phone)

            # 机峰
            web_open('http://www.gfan.com/login.html')
            gfan_sms(my_phone)

            # 爱名网 -------------图-滑块
            web_open('https://my.22.cn/register.html')
            my_22_sms(my_phone)

            web_open('http://qiyukf.com/register/signup?tag=register')
            qiyu_sms(my_phone)

            web_open('https://account.booking.com/register')
            time.sleep(5)
            booking_sms(my_phone)

            web_open('https://mall.sogou.com/register')
            sogou_sms(my_phone)


            # acfun 注册
            web_open('https://www.acfun.cn/reg/')
            acfun_sms(my_phone)

            # 37网游
            web_open('https://www.37.com/')
            wy37_sms(my_phone)

            # 虎扑
            web_open('https://passport.hupu.com/register')
            hupu_sms(my_phone)

            # 纵横中文网
            web_open('https://passport.zongheng.com/')
            hongheng_sms(my_phone)

            # 前程无忧
            web_open('https://login.51job.com/login.php')
            job51_sms(my_phone)

            # BOSS-----滑块
            web_open('https://login.zhipin.com/?ka=header-login')
            zhipin_sms(my_phone)

            # 看准-----滑块
            web_open('https://www.kanzhun.com/login/')
            kanzhun_sms(my_phone)

            # 雪球
            web_open('https://xueqiu.com/')
            xueqiu_sms(my_phone)

            # # 下厨房-----滑块
            # web_open('https://www.xiachufang.com/auth/login/')
            # xiachufang_sms(my_phone)

            # 驴妈妈
            web_open('https://login.lvmama.com/nsso/login')
            lvmama_sms(my_phone)

            # IT橙子-----点击智能验证
            web_open('https://www.itjuzi.com/login')
            itjuzi_sms(my_phone)

            # 少数派--------滑块
            web_open('https://sspai.com/')
            sspai_sms(my_phone)

            # 吾道
            web_open('https://www.woodo.cn/login')
            woodo_sms(my_phone)

            # uzer
            web_open('https://uzer.me/u/signup')
            uzer_sms(my_phone)

            # 兔展
            web_open('https://www.rabbitpre.com/')
            rabbitpre_sms(my_phone)

            # 站酷-----------滑块
            web_open(
                'https://passport.zcool.com.cn/regPhone.do?appId=1006&cback=https://my.zcool.com.cn/focus/activity')
            zcool_sms(my_phone)

            # 千图----------滑块
            web_open('https://www.58pic.com/enroll')
            pic58_sms(my_phone)

            # 图虫
            web_open('https://stock.tuchong.com/home')
            tuchong_sms(my_phone)

            # 草料
            web_open('https://cli.im/')
            cli_sms(my_phone)

            # 网易云
            web_open('https://id.163yun.com/register')
            yun163_sms(my_phone)

            time.sleep(30)
        else:

            print('不是指定时间，等待....' + str(datetime.datetime.now()))
            time.sleep(60 * 5)
