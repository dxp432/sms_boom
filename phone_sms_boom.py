import win32api
import win32con
import time
import ctypes
import webbrowser
from pykeyboard import PyKeyboard
from pymouse import PyMouse


# 单击
def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    time.sleep(1)


# 滑动图块
def slip_pic(x, y, x_1, y_1):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(1)
    m.move(x_1, y_1)
    time.sleep(1)
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
    print('ctrl_w')
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


def xunlei_sms(my_phone_num):
    # 点击短信登录
    click(1434, 235)
    # 点击手机号输入框
    click(1224, 315)
    # 输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1465, 382)
    # 关闭浏览器窗口
    ctrl_w()


def youku_sms(my_phone_num):
    # 点击手机输入框
    click(1000, 400)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击密码输入框
    click(919, 462)
    # 模拟键盘输入密码
    string_input('tringidkde123')
    # 点击密码确认输入框
    click(905, 526)
    # 模拟键盘输入密码
    string_input('tringidkde123')
    # 点击获取验证码
    click(1042, 591)
    # 关闭浏览器窗口
    ctrl_w()


def acfun_sms(my_phone_num):
    # 点击手机输入框
    click(1233, 281)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1332, 510)
    # 关闭浏览器窗口
    ctrl_w()


def sina_sms(my_phone_num):
    # 点击手机输入框
    click(784, 266)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 选择兴趣标签
    click(707, 378)
    # 点击获取验证码
    click(772, 438)
    # 关闭浏览器窗口
    ctrl_w()


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


def ithome_sms(my_phone_num):
    # 点击手机号输入框
    click(859, 360)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1046, 423)
    # 关闭浏览器窗口
    ctrl_w()


def onlinedown_sms(my_phone_num):
    # 点击手机号输入框
    click(1384, 273)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1537, 318)
    # 关闭浏览器窗口
    ctrl_w()


def douban_sms(my_phone_num):
    # 点击手机号输入框
    click(1266, 273)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1380, 315)
    # 关闭浏览器窗口
    ctrl_w()


def five8_sms(my_phone_num):
    # 点击手机号输入框
    click(843, 252)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1069, 252)
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


def chinahr_sms(my_phone_num):
    # 点击登录模块
    click(1480, 140)
    # 点击验证码登录
    click(1039, 307)
    # 点击手机号输入框
    click(835, 386)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(1080, 386)
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


def xiachufang_sms(my_phone_num):
    # 滑动滑块
    slip_pic(933, 403, 1202, 403)
    # 点击手机号输入框
    click(1073, 330)
    # 模拟键盘输入手机号
    string_input(my_phone_num)
    # 点击获取验证码
    click(980, 485)
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


if __name__ == '__main__':
    # 定义鼠标键盘实例
    k = PyKeyboard()
    m = PyMouse()

    # 手机号
    my_phone = input("请输入手机号(然后回车):")

    # 打开浏览器的一个窗口，始终保持有一个窗口，就不怕chrome就被关闭了。
    web_open('http://www.hao123.com')

    # 循环
    for my_index in range(0, 100):
        # 迅雷
        web_open('http://i.xunlei.com/xluser/login.html')
        xunlei_sms(my_phone)

        # 优酷
        web_open('https://account.youku.com/register.htm')
        youku_sms(my_phone)

        # acfun 注册
        web_open('https://www.acfun.cn/reg/')
        acfun_sms(my_phone)

        # 新浪注册
        web_open('https://login.sina.com.cn/signup/signup')
        sina_sms(my_phone)

        # 37网游
        web_open('https://www.37.com/')
        wy37_sms(my_phone)

        # 虎扑
        web_open('https://passport.hupu.com/register')
        hupu_sms(my_phone)

        # 纵横中文网
        web_open('https://passport.zongheng.com/')
        hongheng_sms(my_phone)

        # IT之家
        web_open('https://my.ruanmei.com/?page=register')
        ithome_sms(my_phone)

        # 华军软件园
        web_open('https://user.onlinedown.net/register')
        onlinedown_sms(my_phone)

        # 豆瓣
        web_open('https://www.douban.com/')
        douban_sms(my_phone)

        # 58
        web_open('https://passport.58.com/reg')
        five8_sms(my_phone)

        # 前程无忧
        web_open('https://login.51job.com/login.php')
        job51_sms(my_phone)

        # 中华英才网
        web_open('http://www.chinahr.com/')
        chinahr_sms(my_phone)

        # BOSS-----滑块
        web_open('https://login.zhipin.com/?ka=header-login')
        zhipin_sms(my_phone)

        # 看准-----滑块
        web_open('https://www.kanzhun.com/login/')
        kanzhun_sms(my_phone)

        # 雪球
        web_open('https://xueqiu.com/')
        xueqiu_sms(my_phone)

        # 下厨房-----滑块
        web_open('https://www.xiachufang.com/auth/login/')
        xiachufang_sms(my_phone)

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
        web_open('https://passport.zcool.com.cn/regPhone.do?appId=1006&cback=https://my.zcool.com.cn/focus/activity')
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

        print('-----循环次数-----' + str(my_index + 1))

        time.sleep(100)
