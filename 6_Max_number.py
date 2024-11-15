import sys #MAX and MIN NUMBER
max_number = -sys.maxsize  #naj_malkoto chislo v systemata


while True:
    command_or_num = input()
    if command_or_num == "Stop":
        break

    number = int(command_or_num)

    if number > max_number:
        max_number = number

print(max_number)
