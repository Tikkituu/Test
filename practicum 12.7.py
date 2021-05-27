per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

dict_values = (per_cent.values())
money = float(input("Введите сумму вклада: "))
deposit = [money * i / 100 for i in dict_values]

print('deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать —',max(deposit))