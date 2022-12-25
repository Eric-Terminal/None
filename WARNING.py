from tkinter import messagebox
import time
A = input("警告标题：")
B = input("警告内容：")
time.sleep(5)
messagebox.showwarning(A,B)