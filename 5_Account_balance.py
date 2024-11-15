new_input = input()
total_sum = 0

while new_input != "NoMoreMoney":
    if float(new_input) < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {float(new_input)}")
    total_sum += float(input())
    new_input = input()         #tova koeto vyveda kato vhod ,pak
                                    # tryabva da se vyvede v
print(f"Total: {total_sum:.2f}")            # WHILE loop za da prodykji loop-a

