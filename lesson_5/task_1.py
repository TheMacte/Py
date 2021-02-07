"""
 1. Пользователь вводит данные о количестве предприятий,
 их наименования и прибыль за 4 квартала (т.е. 4 числа) для каждого предприятия.
 Программа должна определить среднюю прибыль (за год для всех предприятий)
 и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import Counter


def business():
    losers, winners = [], []  # Списки тех у кого прибыль выше и ниже среднего
    total = 0  # Средняя прибыль
    average = Counter()  # Массив средних прибылей, необзодим для дальнейших операций
    brute = Counter()  # Сколько каждая компания заработала в средне за год

    cnt_company = int(input('Введите количество компании '))

    for i in range(cnt_company):
        name = input(f'Введите назвние компании №{i + 1} ')
        for q in range(4):
            quarter = float(input(f'Введите прибыль {name} за {q + 1}-ый квартал '))
            brute[name] += quarter
            total += quarter

    for company in brute:
        average[company] = total / len(brute)

    brute.subtract(average)  # Использую свойства Counter для определения кто заработал выше, а кто ниже среднего

    for company in brute:
        if brute[company] > 0:
            winners.append(company)
        else:
            losers.append(company)
    return losers, winners


loser, winner = business()

print(f'Компании заработавшие выше среднего: {winner} \n'
      f'Компании заработавшие ниже среднего: {loser}')
