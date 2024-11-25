coin_change = float(input())

coin_counter = 0

while coin_change > 0:
    if coin_change >= 2:
        coin_change -= 2
    elif coin_change >= 1:
        coin_change -= 1
    elif coin_change >= 0.50:
        coin_change -= 0.50
    elif coin_change >= 0.20:
        coin_change -= 0.20
    elif coin_change >= 0.10:
        coin_change -= 0.10
    elif coin_change >= 0.05:
        coin_change -= 0.05
    elif coin_change >= 0.02:
        coin_change -= 0.02
    elif coin_change >= 0.01:
        coin_change -= 0.01

    coin_counter +=1
    coin_change = round(coin_change,2)

print(coin_counter)