from bug import *
from visualization import *
import os
from tkinter import *
if __name__=='__main__':
    root = Tk()
    root.title('电影信息爬取')
    root.geometry('500x500+500+200')
    # 个人信息
    lb_message = Label(root, text='请依次点击：', font=('宋体', 16))
    #文本框
    tx = Text(root)
    #绑定到三个button的三个方法
    def function1():
        url = get_url(tx)
        url.main()
    def function2():
        if os.path.exists('detail_url.xlsx'):
            movie = analyse('detail_url.xlsx',tx)
            movie.main()
        else:
            tx.delete("1.0",END)
            tx.insert(END,'\n\n请先进行第一步操作\n')
    def function3():
        if os.path.exists('movie.xlsx'):
            vi = visual('movie.xlsx',tx)
            vi.main()
        else:
            tx.delete("1.0",END)
            tx.insert(END,'\n\n请先进行第二步操作\n')
    #三个步骤
    bt_url = Button(root, text='详情页url爬取', font=('宋体', 16), command=function1)
    bt_movie = Button(root, text='电影信息爬取', font=('宋体', 16),command=function2)
    bt_pic = Button(root,text='图片分析',font=('宋体', 16),command=function3)
    #放置
    lb_message.pack()
    bt_url.pack()
    bt_movie.pack()
    bt_pic.pack()
    tx.pack()
    root.mainloop()




