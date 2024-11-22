cake_height = int(input())
cake_width = int(input())

all_cake_pieces = cake_height * cake_width

command = input()
current_pieces = 0


while command != "STOP":
    cake_pieces = int(command)

    all_cake_pieces -= cake_pieces

    if all_cake_pieces <= 0:
        break

    command = input()

if all_cake_pieces >= 0 :
    print(f"{all_cake_pieces} pieces are left.")
else:
    diff = all_cake_pieces - current_pieces
    print(f"No more cake left! You need {-all_cake_pieces} pieces more.")
