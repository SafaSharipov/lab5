# -*- coding: cp1251 -*-



print("������� ������ (�� ������ ����� � ������)")
ms = [0] * 10
sm = 0
count = 0
for i in range(10):
    ms[i] = float(input())
    if ms[i] > 0:
        sm += ms[i]
print("����� ������������� ���������:", sm)
print("������������ �� ������:", sorted(ms, key=lambda x: abs(x))[-1])
print("������:", *ms)
print("��������������� ������:", *sorted(ms, reverse=True))

