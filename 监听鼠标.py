# 导入鼠标监听器
from pynput.mouse import Listener

# 监听鼠标移动的方法
def on_move(x, y):
    print('鼠标移动到{0}'.format((x, y)))


# 监听鼠标点击的方法
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('按下于' if pressed else '松开于', (x, y)))



# 监听鼠标滚轮的方法
def on_scroll(x, y, dx, dy):
    print('滚动于{0}'.format((x, y)))


# 注册三个监听方法的监听器
def main():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

if __name__ == '__main__':
    main()