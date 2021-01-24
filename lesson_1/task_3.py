"""
 По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
 проходящей через эти точки.

 Мат часть брал тут: https://zaochnik.com/spravochnik/matematika/prjamaja-ploskost/uravnenie-prjamoj-kotoraja-prohodit-cherez-dve-zad/
 """

x1 = float(input('Введит кординаты x для первой точки: '))
y1 = float(input('Введит кординаты y для первой точки: '))
x2 = float(input('Введит кординаты x для второй точки: '))
y2 = float(input('Введит кординаты y для второй точки: '))
if x1 == x2:
    print(f'x - {x1} = 0')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k}x {"+" if b >= 0 else "-"} {abs(b)}')
