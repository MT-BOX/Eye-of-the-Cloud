from tkinter import *
import time
import face
from xpinyin import Pinyin

flag = 1


class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('人脸注册')
        self.root.geometry('300x200+300+150')
        self.canvas = Canvas(self.root, bg='white')
        self.canvas.pack(fill="both", expand=1)
        self.interface()

    def add_menu(self):
        self.y_add.place_forget()
        self.n_add.place_forget()
        self.isadd_lable.place_forget()
        self.add_lable = Label(self.canvas, text='请输入您的姓名', font=('Arial', 12), bg='white')
        self.username = Entry(self.canvas, font=('Arial', 12), bg='white', width=15)
        self.fix = Button(self.canvas, text='确定', font=('Arial', 12), width=10, command=self.add_face)
        self.add_lable.place(x=80, y=40)
        self.username.place(x=80, y=80)
        self.fix.place(x=90, y=130)
        # time.sleep(1)
        self.canvas.update()
        # time.sleep(1)

    def interface(self):
        self.isadd_lable = Label(self.canvas, text='是否进行人脸注册?', font=('Arial', 12), bg='white')
        self.y_add = Button(self.canvas, text='是', font=('Arial', 12), width=10, command=self.add_menu)
        self.n_add = Button(self.canvas, text='否', font=('Arial', 12), width=10, command=self.cancel_face)
        self.y_add.place(x=50, y=120)
        self.n_add.place(x=150, y=120)
        self.isadd_lable.place(x=80, y=60)
        self.root.mainloop()

    def add_success(self):
        self.add_lable.place_forget()
        self.username.place_forget()
        self.fix.place_forget()
        self.success_lable = Label(self.canvas,text='注册成功',font=('Arial', 12),bg='white')
        self.success_lable.place(x=120,y=70)
        self.canvas.update()
        time.sleep(2)
    def add_failed(self):
        self.add_lable.place_forget()
        self.username.place_forget()
        self.fix.place_forget()
        self.failed_lable = Label(self.canvas,text='注册失败',font=('Arial', 12),bg='white')
        self.failed_lable.place(x=120,y=70)
        self.canvas.update()
        time.sleep(2)
    # time.sleep(2)
    def add_face(self):
        global flag
        if self.username.get() != '':
            # print(self.username.get())
            username = self.username.get()
            p = Pinyin()
            username_pinyin = p.get_pinyin(username)
            username_pinyin = ''.join(username_pinyin.split('-'))
            # print(p.get_pinyin('汪林'))
            face.get_image(face.detected_image_name)
            detected_result = face.face_detected()
            if detected_result['error_msg'] == 'SUCCESS':
                face.face_cut(face.detected_image_name, detected_result)
                add_result = face.face_add(face.cut_image_name, username, username_pinyin)
                if add_result['error_msg'] == 'SUCCESS':
                    print('注册成功')
                    self.add_success()
                    flag = 1
                else:
                    print('注册失败')
                    self.add_failed()
                    flag = 0
            else:
                print('注册失败')
                self.add_failed()
                flag = 0
        else:
            flag = 0
        self.root.destroy()

    def cancel_face(self):
        global flag
        self.root.destroy()
        flag = 0

# menu = Interface()
# interface()
# p = Pinyin()
# username_pinyin = p.get_pinyin('汪林')
# username_pinyin = ''.join(username_pinyin.split('-'))
# print(username_pinyin)
