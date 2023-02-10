# -*- coding: cp1251 -*-



print("Введите массив (по одному числу в строке)")
ms = [0] * 10
sm = 0
count = 0
for i in range(10):
    ms[i] = float(input())
    if ms[i] > 0:
        sm += ms[i]
print("Сумма положительных элементов:", sm)
print("Максимальный по модулю:", sorted(ms, key=lambda x: abs(x))[-1])
print("Массив:", *ms)
print("Отсортированный массив:", *sorted(ms, reverse=True))

