
steps_goal = 10_000
current_steps = 0
#initiate
command = input() #"Going home" or steps as a string(e.g."1000")

#check the condition
while command != "Going home":
    steps = int(command) #int("1000") == 1000

    current_steps += steps #increase the steps
    if current_steps >= steps_goal:
        break #prekysvame loop-a

    # potential change
    command = input()

if command == "Going home":
    extra_steps = int(input())#sledvashtite vhodyashti danni
    current_steps += extra_steps

if current_steps >= steps_goal:
    diff = steps_goal - current_steps
    print("Goal reached! Good job!")
    print(f"{abs(diff)} steps over the goal!")
else:
    diff = steps_goal - current_steps
    print(f"{diff} more steps to reach goal.")