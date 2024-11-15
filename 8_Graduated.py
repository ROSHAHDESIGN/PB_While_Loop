student = input() #imeto
grade = 1 # clasa, zapochva ot 1
score = 0 #ocenkata
max_tries = 0

while True:
    new_score = float(input()) #poluchava ocenka, na baza neq se validira
    if new_score < 4: #kogato ocenkata e po-malka ot 4;
        max_tries += 1  # ima pravo na 1 opit
        if max_tries > 1:
            print(f"{student} has been excluded at {grade} grade")
            break #trybva da spre
        continue #prekratyava iteration, no loop-a prodyljava

    score += new_score
    if grade == 12: #uspeshniya scenarii v koyot zavyrshva
        print(f"{student} graduated. Average grade: {score/12:.2f}")
        break #tuk loop-a prekratyava zashtoto e stignal 12

    grade += 1 #uvelichava clas-a s 1 do 12

