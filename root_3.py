'''
------------------------------------------------------||
----CountdownTHEO--on--Python36-----------------------||
------------------------------------------------------||
----by.mikky1206@gmail.com----------------------------||
------------------------------------------------------||
'''


from tkinter import *
from tkinter import ttk
import os
from math import pi, cos, sin, radians, acos, asin


root1 = Tk()
root1.title('CountdownTHEO - T30')
root1.geometry('1200x700+70+5')
root1.resizable(False, False)


'''_____________Canvas.create_line______________'''


canvasLine = Canvas(root1, width=10, height=710, bg='#333')
canvasLine.place(x=390, y=-10)

canvasLine.create_line(400, 0, 400, 700)


'''_____________Frames_____________'''


frameH = Frame(root1, width=391, height=700, bg='#333')
frameH.place(x=0, y=0)

frameTC = Frame(root1, width=800, height=50, bg='#333')
frameTC.place(x=400, y=0)

frameC = Frame(root1, width=800, height=400, bg='#333')
frameC.place(x=400, y=50)

frameCE = Frame(root1, width=800, height=400, bg='#333')
frameCE.place(x=400, y=450)


'''_____________Information in frameH_____________'''


img1 = PhotoImage(file='root1.gif')
img = Label(frameH, image=img1, width=391, height=245)
img.place(x=-5, y=-5)


def label(frame, textL, xL, yL):
    nameL = Label(frame, text=textL, bg='#333', fg='#fff', font='arial 9')
    nameL.place(x=xL, y=yL)


h1 = 'СКО измерения гор. угла одним приемом  30"'
h2 = 'СКО измерения вертикального угла  30"'
h3 = 'Цена деления уровня при алидаде горизонтального круга  45`'
h4 = 'Поле зрения зрительной трубы  2 град.'
h5 = 'Увеличение трубы  20X'
h6 = 'Коэффициент нитяного дальномера  100'
h7 = 'Цена деления лимба  10`'
h8 = 'Погрешность отсчитывания  0.5`-1`'

labelT = Label(frameH, text='Т30', bg='#333', fg='#fff', font='arial 16')
labelT.place(x=10, y=250)

label(frameH, "Цена деления лимба = 10'", 10, 350)
label(frameH, h1, 10, 450)
label(frameH, h2, 10, 470)
label(frameH, h3, 10, 490)
label(frameH, h4, 10, 510)
label(frameH, h5, 10, 530)
label(frameH, h6, 10, 550)
label(frameH, h7, 10, 570)
label(frameH, h8, 10, 590)

labelTC = Label(frameTC, text='Поле зрения отсчетного устройства микроскопа теодолита', bg='#333', fg='#fff', font='arial 12')
labelTC.place(x=180, y=20)

label(frameCE, 'Горизонтальный круг', 130, 70)
label(frameCE, 'Вертикальный круг', 530, 70)

label(frameCE, 'Ввод отсчетов', 360, 30)


'''____________Entry____________'''


hg = Spinbox(frameCE, width=7, from_=0, to=359)
hg.place(x=85+40, y=100)
hm = Spinbox(frameCE, width=7, from_=0, to=59)
hm.place(x=85*2+40, y=100)

vg = Spinbox(frameCE, width=7, from_=0, to=359)
vg.place(x=(85+40+400), y=100)
vm = Spinbox(frameCE, width=7, from_=0, to=59)
vm.place(x=85*2+40+400, y=100)


'''___________Canvas create____________'''

def createCanvas(hg, hm, vm, vg):
    hg = 360-hg
    hm = 60-hm
    vm = 60-vm
    vg = 360-vg
    # обозначаем размер и свойства виджета Canvas, и положение
    canvasFrame = Canvas(frameC, width=381, height=381,
                        bg="#333", highlightthickness=0)
    canvasFrame.place(x=219, y=19)
    # строим поле зрения отсчетного устройства
    canvasFrame.create_oval(0, 0, 380, 380, outline="white")
    # строим внутренние элементы
    canvasFrame.create_line(0, 380/2-1, 380, 380/2-1, fill="white")
    canvasFrame.create_line(0, 380/2+1, 380, 380/2+1, fill="white")
    canvasFrame.create_line([(1-cos(asin(0.35)))*380, 380*3/4,
                            380/2-380/32, 380*3/4,
                            380/2-380/32, 380*3/4+380/16,
                            380/2+380/32, 380*3/4+380/16,
                            380/2+380/32, 380*3/4,
                            (cos(asin(0.35)))*380, 380*3/4], fill="white")
    canvasFrame.create_line([(1-cos(asin(0.35)))*380, 380*1/4,
                            380/2-380/32, 380*1/4,
                            380/2-380/32, 380*1/4-380/16,
                            380/2+380/32, 380*1/4-380/16,
                            380/2+380/32, 380*1/4,
                            (cos(asin(0.35)))*380, 380*1/4], fill="white")
    canvasFrame.create_line(380/2, 380*2/6, 380/2, 380*4/6, fill="white")
    canvasFrame.create_text(380/2, 380*1/4-10, text="В", fill="white")
    canvasFrame.create_text(380/2, 380*3/4+10, text="Г", fill="white")
    
    # построение отсчетных штрихов
    for i in [0, 3, 6, 9, 12, 16]:
        canvasFrame.create_line(380/2+380/16*vm/10-380/16*i, 380/2-1,
                                380/2+380/16*vm/10-380/16*i, 380/2-1-380/7, fill="white")
        canvasFrame.create_line(380/2+380/16*vm/10+380/16*i, 380/2-1,
                                380/2+380/16*vm/10+380/16*i, 380/2-1-380/7, fill="white")
    for i in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]:
        canvasFrame.create_line(380/2+380/16*vm/10-380/16*i, 380/2-1,
                                380/2+380/16*vm/10-380/16*i, 380/2-1-380/7/2, fill="white")
        canvasFrame.create_line(380/2+380/16*vm/10+380/16*i, 380/2-1,
                                380/2+380/16*vm/10+380/16*i, 380/2-1-380/7/2, fill="white")
    for i in [0, 3, 6, 9, 12, 16]:
        canvasFrame.create_line(380/2+380/16*hm/10-380/16*i, 380/2+1,
                                380/2+380/16*hm/10-380/16*i, 380/2+1+380/7, fill="white")
        canvasFrame.create_line(380/2+380/16*hm/10+380/16*i, 380/2+1,
                                380/2+380/16*hm/10+380/16*i, 380/2+1+380/7, fill="white")
    for i in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]:
        canvasFrame.create_line(380/2+380/16*hm/10-380/16*i, 380/2+1,
                                380/2+380/16*hm/10-380/16*i, 380/2+1+380/7/2, fill="white")
        canvasFrame.create_line(380/2+380/16*hm/10+380/16*i, 380/2+1,
                                380/2+380/16*hm/10+380/16*i, 380/2+1+380/7/2, fill="white")
    
    # построение значений углов
    canvasFrame.create_text(380/2+380/16*vm/10-380/16*0, 380/2-1-380/5,
                            text=str(360-vg+1), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*vm/10-380/16*-6, 380/2-1-380/5,
                            text=str(360-vg), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*vm/10-380/16*-12, 380/2-1-380/5,
                            text=str(360-vg+3), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*vm/10-380/16*6, 380/2-1-380/5,
                            text=str(360-vg), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*vm/10-380/16*12, 380/2-1-380/5,
                            text=str(360-vg-1), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*hm/10-380/16*0, 380/2+1+380/5,
                            text=str(360-hg+1), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*hm/10-380/16*-6, 380/2+1+380/5,
                            text=str(360-hg+2), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*hm/10-380/16*-12, 380/2+1+380/5,
                            text=str(360-hg+3), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*hm/10-380/16*6, 380/2+1+380/5,
                            text=str(360-hg), fill="white", font=14)
    canvasFrame.create_text(380/2+380/16*hm/10-380/16*12, 380/2+1+380/5,
                            text=str(360-hg-1), fill="white", font=14)


createCanvas(10, 42, 28, 24)


'''_____________Button CE_____________'''


btnCE = ttk.Button(frameCE, text='Показать отсчет', width=100)
btnCE.bind('<Button-1>', lambda event: createCanvas(int(hg.get()),
                                                    float(hm.get()),
                                                    float(vm.get()),
                                                    int(vg.get())))

btnCE.place(x=95, y=150)


'''_____________def menu_______________'''


def btn_menu():

    os.startfile(r'root0.py')
    root1.quit()


'''_____________Button menu____________'''


btnCE = ttk.Button(frameCE, text='    Выход в меню    ')
btnCE.bind('<Button-1>', lambda event: btn_menu())

btnCE.place(x=593, y=200)


def gen_count():
    import random as r

    global hg1, hm1, vg1, vm1

    hg1 = r.randint(0, 359)
    hm1 = r.randint(0, 59)

    vg1 = r.randint(0, 359)
    vm1 = r.randint(0, 59)

    print(hg1, hm1)
    print(vg1, vm1)

    createCanvas(hg1, hm1, vm1, vg1)


def gen_prov(hg, hm, vg, vm):
    import math as m

    root02 = Tk()
    root02.geometry('370x120+600+300')
    frame02 = Frame(root02, width=370, height=120, bg='#333')
    frame02.place(x=0, y=0)



    if hg == hg1 and m.fabs(hm - hm1) <= 1 and vg == vg1 and m.fabs(vm - vm1) <= 1 :
        text = ' Верно!'
    else: text = 'Не верно!\n' + 'Горизонтальный круг: ' + str(hg1) + 'град ' + str(hm1) + 'мин' + '\nВертикальный круг: ' + str(vg1) + 'град ' + (str(vm1)) + 'мин'

    txt = Label(frame02, text=text, bg='#333', fg='#fff', font='arial 12')
    txt.place(x=50, y=12)
    '''
    btn = ttk.Button(root02, text='Ok')
    btn.bind('<Button-1>', lambda event: quit())
    btn.pack()
    '''


btnCE = ttk.Button(frameCE, text='Сгенерировать', width=20)
btnCE.bind('<Button-1>', lambda event: gen_count())

btnCE.place(x=95, y=200)

btnCE = ttk.Button(frameCE, text='Проверить', width=20)
btnCE.bind('<Button-1>', lambda event: gen_prov(int(hg.get()),
                                                float(hm.get()),
                                                int(vg.get()),
                                                float(vm.get())))

btnCE.place(x=250, y=200)


root1.mainloop()
