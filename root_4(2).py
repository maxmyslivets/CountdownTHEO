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


root1 = Tk()
root1.title('CountdownTHEO - 2T30')
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


h1 = 'СКО измерения гор. угла одним приемом =20"'
h2 = 'СКО измерения вертикального угла =30"'
h3 = 'Диапазон измерения верт.углов  +60..-55 град.'
h4 = 'отсчетное устройство - шкаловая система'
h5 = 'Увеличение трубы =20X'
h6 = 'Диапазон рабочих температур  -40..+50 С '
h7 = 'Габаритные размеры 140х130х230 мм'
h8 = 'Масса теодолита =2.3 кг'

labelT = Label(frameH, text='2Т30', bg='#333', fg='#fff', font='arial 16')
labelT.place(x=10, y=250)

label(frameH, "Цена деления лимба =60'", 10, 350)
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
hm = Spinbox(frameCE, width=7, from_=0, to=59.0)
hm.place(x=85*2+40, y=100)

vg = Spinbox(frameCE, width=7, from_=-359, to=359)
vg.place(x=(85+40+400), y=100)
vm = Spinbox(frameCE, width=7, from_=0, to=59.0)
vm.place(x=85*2+40+400, y=100)


'''_____________import Img____________'''


img_C1 = PhotoImage(file='2т30.gif')

imgC1 = Label(frameC, image=img_C1, width=396, height=400)
imgC1.place(x=198, y=-2)


'''_____________def btn_CE_____________'''


def btn_CE(hg, hm, vm, vg):

    imgC1 = Label(frameC, image=img_C1, width=396, height=400)
    imgC1.place(x=198, y=-2)

    canvasCh = Canvas(frameC, width=1, height=30, bg='#333')
    labelCh = Label(frameC, text=str(hg), bg='#333', fg='#fff', font='arial 16')

    canvasCv = Canvas(frameC, width=1, height=30, bg='#333')
    labelCv = Label(frameC, text=str(vg), bg='#333', fg='#fff', font='arial 16')

    xx = 336
    d = 1.95

    xCh = xx+d*hm
    canvasCh.place(x=xCh, y=207)

    labelCh.place(x=xCh - 7, y=250)

    if vg > 0 or vg == 0:

        xCv = xx + d * vm
        canvasCv.place(x=xCv, y=128)

        labelCv.place(x=xCv - 7, y=95)

    elif vg < 0:

        xCv = (xx + d * 60) - d * vm
        canvasCv.place(x=xCv, y=128)

        labelCv.place(x=xCv - 7, y=95)


'''_____________Button CE_____________'''


btnCE = ttk.Button(frameCE, text='Показать отсчет', width=100)
btnCE.bind('<Button-1>', lambda event: btn_CE(int(hg.get()),
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

    vg1 = r.randint(-359, 359)
    vm1 = r.randint(0, 59)

    print(hg1, hm1)
    print(vg1, vm1)

    btn_CE(hg1, hm1, vm1, vg1)


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