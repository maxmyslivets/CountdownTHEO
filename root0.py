'''
----------------------------------------------||
----CountdownTHEO--on--Python36-----------------------||
--------------------------------------------------||
----by.mikky1206------------------------------||
------------------------------------------||
'''


from tkinter import *
from tkinter import ttk
import os


root_0 = Tk()
root_0.title('CountdownTHEO')
root_0.geometry('600x400+383+184')
root_0.resizable(False, False)


img0 = PhotoImage(file='root0.gif')
img = Label(root_0, image=img0, width=600, height=400)
img.pack()


'''_______________Button 1_______________'''


def btn1():
    os.startfile(r'root_1.py')
    root_0.quit()


btn = ttk.Button(root_0, text='2T5K', width=15)
btn.bind('<Button-1>', lambda event: btn1())
btn.place(x=10, y=20)


'''_______________Button 2_______________'''


def btn2():
    os.startfile(r'root_4(2).py')
    root_0.quit()


btn = ttk.Button(root_0, text='2T30', width=15)
btn.bind('<Button-1>', lambda event: btn2())
btn.place(x=10, y=60)


'''

#_______________Button 3_______________


def btn3():
    os.startfile(r'root_3.py')
    root_0.quit()


btn = ttk.Button(root_0, text='3Т2КП', width=15)
btn.bind('<Button-1>', lambda event: btn3())
btn.place(x=10, y=100)


#_______________Button 4_______________


def btn4():
    os.startfile(r'root_4.py')
    root_0.quit()


btn = ttk.Button(root_0, text='2T30(П)', width=15)
btn.bind('<Button-1>', lambda event: btn4())
btn.place(x=10, y=140)
'''

'''_______________Button 5_______________'''


def btn5():
    root_0.quit()


btn = ttk.Button(root_0, text='Выход', width=15)
btn.bind('<Button-1>', lambda event: btn5())
btn.place(x=470, y=350)

root_0.mainloop()