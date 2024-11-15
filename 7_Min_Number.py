min_number = 10000000000000

while True:
    command_or_num = input()
    if command_or_num == "Stop":
        break

    number = int(command_or_num)

    if number < min_number:
        min_number = number

print(min_number)

