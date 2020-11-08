
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

for i in range(len(lines)):
    print("Ход №", i+1, ":", lines[i])

