from wxpy import *
import dingding.DingDing as Ding
import time
directory ='C:\\Program Files (x86)\\ClockworkMod\\Universal Adb Driver'


bot = Bot(cache_path=True)
try:
    print('微信启动')
    time.sleep(10)
    my_friend = bot.friends().search('spirit', sex=MALE, city='苏州')[0]
    print('开始打卡')
    dingding = Ding.dingding(directory)
    dingding.goto_work(1)
    png=dingding.filename
    print(png)
    my_friend.send('打卡了打卡了')
    my_friend.send_image('D:\\dingding\\'+png)
except Exception as e:
    print(e)
    my_friend.send('打卡失败:'+e)
    exit()
embed()