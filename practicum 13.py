tickets = int(input('Number of tickets: '))
price = 0

for result in range(tickets):
    age = int(input('Age'))
    if age < 18:
     price += 0
    elif 18 <= age < 25:
     price += 990
    elif age >= 25:
     price += 1390
if tickets > 3:
        price = price - (price * 0.1)
print('Amount of payment', price)
