# -*- coding: cp1251 -*-


print("������� ������ (�� ������ ����� � ������)")
ms = [0] * 10
sm = 0
for i in range(10):
    ms[i] = int(input())
    if ms[i] > 0:
        sm += ms[i]
print("����� ������������� ���������:", sm)
print("������:", *ms)

