from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry('200x100')  # 窗口尺寸
top.title('按钮')  # 窗口初始标题
def anniu():
    messagebox.showinfo("一个小按钮", "Hello wrold!")  # 响应
B = Button(top, text="点我", command=anniu)  # 按钮属性
B.pack()
top.mainloop()

