import random

L_1 = []
L_2 = []
L_all = []
L_all_bezpov = []
L_all_ob = []
L_all_unik = []
L_minmax = []
lenght = random.randint(10, 20)


for i in range(lenght):
    elem1 = random.randint(-50, 50)
    L_1.append(elem1)
    elem2 = random.randint(-50, 50)
    L_2.append(elem2)
    if elem1 == elem2:

        L_all_ob.append(elem1, elem2)

        L_all_bezpov.append(elem1)
    if elem1 != elem2:
        L_all_unik.append(elem1)
    if elem2 != elem1:
        L_all_unik.append(elem2)


L_all.append(L_1)
L_all.append(L_2)

L_minmax.append(min(L_1))
L_minmax.append(min(L_2))
L_minmax.append(max(L_1))
L_minmax.append(max(L_2))

print("Первый список", L_1)
print("Первый список", L_2)
print("Общий список", L_all)
print("Список уникальных чисел", L_all_unik)
print("Список с общими чисел", L_all_ob)
print("Списоодинаковых чисел без повторения", L_all_bezpov)
print("Мин и макс значения списков", L_minmax)