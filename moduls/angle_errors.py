from transdeg import deg_to_rad, rad_to_str_dms, str_dms_to_rad
from random import uniform as rnd
from normalNumbers import normalNumbers
from math import pi, sqrt

t = normalNumbers

def angle_to_countdown(b, mb):
    b = deg_to_rad(b)       # перевод угла в радианы
    mb = deg_to_rad(mb)
    # возмем натуральное число из списка натуральных чисел
    ti = t.pop(0)           # возвращает элемент списка и удаляет его из списка
    # генерируем добавочное значение к углу
    br1 = rnd(0.0, float(pi))
    # прибавим к углу добавочное значение и внесем случайную погрешность
    kl_1 = b + br1 + ti*mb       # получаем отсчет с погрешностью
    # получим добавочное значение с погрешностью для второго отсчета по кругу
    kl_2 = br1 + t.pop(0)*mb
    # сгенерируем остальные два отсчета
    br2 = rnd(0.0, 2*(pi))
    kp_1 = b + br2 + t.pop(0)*mb
    kp_2 = br2 + t.pop(0)*mb
    # формируем список отсчетов
    c = [kl_1, kl_2, kp_1, kp_2]
    # исправляем углы которые больше 360 градусов
    for i in range(4):
        if c[i] > 2*pi:
            c[i] = c[i] - 2*pi
    # переводим радианы в градусы
    for i in range(4):
        c[i] = rad_to_str_dms(c[i])

    return c

angle = [
    219+37/60, 
    75+26/60+18/3600, 
    96+21/60+29/3600,
    150+24/60+14/3600,
    237+17/60+5/3600,
    126+22/60+35/3600,
    146+26/60+31/3600,
    152+19/60+54/3600,
    196+30/60+1/3600,
    63+32/60+52/3600,
    173+16/60+19/3600,
    162+25/60+45/3600
    ]

countdowns = []
for i in angle:
    countdowns.append(angle_to_countdown(i, 0.5/60))

for c in countdowns:
    print(c)


def test_on_f_dop(countdowns):
    """
    Тест на вхождение невязки по смоделированным
    результатам измерений в допустимую
    """
    
    def c_to_ang(c):
        c1, c2, c3, c4 = str_dms_to_rad(c[0]), str_dms_to_rad(c[1]), str_dms_to_rad(c[2]), str_dms_to_rad(c[3])
        if c1 < c2:
            c_kl = c1-c2+pi*2
        else:
            c_kl = c1-c2
        if c3 < c4:
            c_kp = c3-c4+pi*2
        else:
            c_kp = c3-c4
        
        return rad_to_str_dms((c_kl+c_kp)/2)
    
    ang = []
    for i in range(len(countdowns)):
        print(countdowns[i])
        ang.append(c_to_ang(countdowns[i]))
    
    f_izm = 0
    print('Углы измеренные')
    for i in ang:
        print(i)
        f_izm += str_dms_to_rad(i)
    print('Сумма измеренных углов:', rad_to_str_dms(f_izm))
    f_t = deg_to_rad(180)*(len(countdowns)-2)
    print('Теоретическая сумма углов:', rad_to_str_dms(f_t))
    f_pr = f_izm - f_t
    print('Невязка:', rad_to_str_dms(f_pr))
    f_dop = deg_to_rad(0.5/60)*sqrt(12)
    print('Допустимая невязка (0.5`):', rad_to_str_dms(f_dop))
    if f_pr < f_t or f_pr == f_t:
        print('Невязка в допуске!')
    else:
        print('Невязка не в допуске!')

test_on_f_dop(countdowns)
