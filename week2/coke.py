amount = 50
coins = [5, 10, 25]

while amount > 0:
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))

    if coin in coins:
        amount = amount - coin

print("Change Owed:", abs(amount))
