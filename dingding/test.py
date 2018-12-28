import dingding.DingDing as Ding
import time
directory ='C:\\Program Files (x86)\\ClockworkMod\\Universal Adb Driver'

time.sleep(10)

dingding = Ding.dingding(directory)
png=dingding.goto_work(1)
print(dingding.filename)
