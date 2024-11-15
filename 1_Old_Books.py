# number = 13
#
# while number < 100:
#     print(number)
#
#     number += 10

book_name = input()
book_checked = 0    #pomoshtna promenliva COUNTER(tya broy)
command = input()   #1.initialisation

while command != "No More Books":     #2.check
    new_book = command

    if new_book == book_name:
        break

    book_checked += 1

    command = input() #3.CHANGE CONDITION
if command == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {book_checked} books.")
else:
    print(f"You checked {book_checked} books and found it.")