failed_threshold = int(input()) #broya pozvoleni ocenki

#broyach za uprajneniq koito sa resheni
solved_problems_count = 0
#broyach nezadovolitelni ocenki
failed_times = 0
#suma na vsichki ocenki
grades_sum = 0
#koya e poslednata zadacha
last_problem = " "
#dali se e provalil ili NE
has_failed = True

#pyrvi sluchai na while
while failed_times < failed_threshold:
    problem_name = input()  #imeto na zadachata
    if problem_name == "Enough":
        has_failed = False
        break #prekratyava loop-a

    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_threshold} poor grades.")
else:
    print(f"Average score: {grades_sum / solved_problems_count:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")
