import pyautogui
import pyperclip
import time

print(pyautogui.position())
#显示鼠标的x,y位置

words = "let me try，我钉钉版本太低了，没有办法主动连麦，周姐你连我,let me try(by Eric的代码我钉钉版本太低了，没有办法主动连麦，周姐你连我(by Eric的代码)"
#在这修改文本

time.sleep(5)#在这修改切换窗口的时间
for i in words.split("/n") * 10:#在这修改说的次数
    print(i)
    pyautogui.click(x=1240, y=866)
    pyperclip.copy(i)
    pyautogui.hotkey("command", "v")
    pyautogui.typewrite("\n")
    time.sleep(0.5)#在这修改间隔时间
