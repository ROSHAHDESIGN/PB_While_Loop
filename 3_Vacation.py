needed_money = float(input())
money_avaliable = float(input())


#deistviya "save" ili "spend"

#pomoshtni promenlivi
days_counter = 0
spending_counter = 0

while money_avaliable < needed_money and spending_counter < 5: #ako dnite sa > 5
    spend_or_save = input() #command-a na loop-a se chete SPEND or SAVE comand-a
    money = float(input())  #stoynostta na parite
    days_counter += 1       #broyat na dnite koito se trupat
    if spend_or_save == "save": #PROVERKA dali pesti
        money_avaliable += money
        spending_counter = 0
    elif spend_or_save == "spend":
        money_avaliable -= money #parite se namalyat
        spending_counter += 1
        if money_avaliable < 0: #parite sa po-malko ot 0
            money_avaliable = 0
if spending_counter == 5:
    print(f"You can't save the money.")
    print(days_counter)

if money_avaliable >= needed_money:
    print(f"You saved the money for {days_counter} days.")

