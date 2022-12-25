import pygame  # 导入pygame库

pygame.init()  # pygame组件初始化
pygame.display.set_caption("Eric测试窗口")  # 设置窗口名称
height = 600  # 窗口高度变量
width = 400  # 窗口宽度变量
# 将设置窗口大小赋值给screen是方便以后贴图粘贴的方便
screen = pygame.display.set_mode([height, width])  # 设置窗口尺寸

while True: # 设置窗口循环事件
    for event in pygame.event.get():
    # 利用for循环将event在pygame自带的事件中遍历
        if event.type == pygame.QUIT: # 如果event的类型 = pygame退出事件的类型
            pygame.quit() # 则关闭窗口