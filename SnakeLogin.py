import tkinter as tk
from tkinter import messagebox


def confirm():
    global right_pd
    username = entry_username.get()
    password = entry_password.get()
    if username == "ijiajia" and password == "1028":
        messagebox.showinfo("登录成功", "欢迎进入贪吃蛇游戏！")
        window.quit()
        right_pd = True
    else:
        global count
        count -= 1
        messagebox.showerror("登录失败", f"用户名或密码错误，你还有{count}次机会，请重新输入！")
    if count == 0:
        window.quit()


# def register():
#     messagebox.showinfo("注册", "请前往官网进行注册！")
window = tk.Tk()
window.title("贪吃蛇登录")
window.geometry("500x300+400+300")

label_title = tk.Label(window, text="贪吃蛇", font=("Arial", 20))
label_title.pack()

label_username = tk.Label(window, text="用户名：")
label_username.place(x=100, y=100)
entry_username = tk.Entry(window)
entry_username.place(x=180, y=100)

label_password = tk.Label(window, text="密码：")
label_password.place(x=100, y=150)
entry_password = tk.Entry(window, show="*")
entry_password.place(x=180, y=150)

button_login = tk.Button(window, text="登录", command=confirm)
button_login.place(x=220, y=200)

count = 3
right_pd = False

# button_register = tk.Button(window, text="注册", command=register)
# button_register.place(x=180, y=110)

def login():
    window.mainloop()
    return right_pd


if __name__ == '__main__':
    login()
