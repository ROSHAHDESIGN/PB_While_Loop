space_width = int(input())
space_length = int(input())
space_height = int(input())

available_space = space_width * space_length * space_height
command = input()

while command != "Done":
    boxes_count = int(command)

    available_space -= boxes_count
    if available_space <= 0:
        break

    command = input()



if available_space >= 0:
    print(f"{available_space} Cubic meters left.")
else:
    print(f"No more free space! You need {-(available_space)} Cubic meters more.")