number = int(input())
sum = 0 #global variable

while True:
    new_input = int(input())
    sum += new_input

    if sum >= number:
        break

print(sum)