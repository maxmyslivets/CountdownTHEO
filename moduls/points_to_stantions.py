
# Чтение списка каталога точек экспортированных с автокада
with open("points.txt") as points:
    pointsCatalog = (points.read().split("\n"))
    if pointsCatalog[-1] == "":
        del pointsCatalog[-1]

# Создание списка имен точек
pointName = []
for point in pointsCatalog:
    pointName.append(point.split(",")[0])
print("Каталог экспортированных точек:\n", pointName)

# Создание списка точек ходов
lines = []
namber = 1
while True:
    pointLine = input(
        "Введите точки хода № %s в порядке их последовательности в ходе:\n" % str(namber)).split(",")

    # Проверка списка точек хода на существование в каталоге точек
    n_error = 0

    for point in pointLine:
        if point not in pointName:
            n_error += 1

    if n_error != 0:
        print("Найдено", n_error, "ошибок в введенном списке. Возможно какой-то из введенных точек нету в каталоге. Повторите ввод")
    
    else:   # Если ошибок нет, то предложить зокончить ввод точек хода или ввод точек следющего хода
        lines.append(pointLine)
        a = input("Введите '1', если хотите закончить ввод точек ходов.\nВведите '2', если хотите ввести точки следующего хода.\n")
        if a == '2':
            namber += 1
        elif a == '1':
            break
        else:
            print("Введено неверное значение... Начните ввод всех точек заново.")
            lines = []
            break

for i in range(len(lines)):
    print("Ход №", i+1, ":", lines[i])

text_st_0_p = ""
# Ввод пикетов для станций
for i in range(len(lines)):
    k = i + 1
    for st in lines[i]:
        #FIXME: Добавить проверку на ввод несуществующих пикетов
        line = []
        print("Ввод пикетов для хода № %s. Станции %s" % (i+1, lines[i]))
        line.append(k)
        line.append(st)
        picketList = input("Введите точку обнуления и пикеты для станции %s:" % st).split(",")
        for p in picketList:
            line.append(p)
        lineText = ""
        for l in line:
            lineText += str(l) + ","
        text_st_0_p += "\n" + str(lineText)[0:-1]

# Запись (ход, станция, обнуление, пикеты) в файл st_0_p.txt
with open("st-0-p.txt", "w") as st_0_p:
    st_0_p.write(text_st_0_p[1:])

print(
    """
    Произведена запись вида:
        № хода, cтанция, точка обнуления, пикеты...
    в файл st_0_p.txt
    """
)

# Проверка неиспользуемых точек из каталога
with open("st-0-p.txt", "r") as st_0_p:
    st_0_p_Catalog = (st_0_p.read().split("\n"))
    catalogPoints = []
    for i in range(len(st_0_p_Catalog)):
        stringPoint = st_0_p_Catalog[i].split(",")
        del stringPoint[0]
        for j in stringPoint:
            catalogPoints.append(j)
        
    catalogPointsNo = []
    for i in pointName:
        if i not in catalogPoints:
            catalogPointsNo.append(i)
    
    if len(catalogPointsNo) != 0:
        print("В обработку не попали точки: ", catalogPointsNo)
        input("Нажмите любю клавишу для завершения.")
    else:
        input("Все точки были выбраны в обработку. Нажмите любю клавишу для завершения.")
