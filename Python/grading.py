
game_in_session = True

while game_in_session == True:
    userGrade = int(input("hello, what is your grade: "))

    if userGrade <= 100 and userGrade >=90:
        print("you scored an A !")
    if userGrade <= 89 and userGrade >=80:
        print("you scored an b !")
    if userGrade <= 79 and userGrade >=70:
            print("you scored an c !")
    if userGrade <= 69 and userGrade >=60:
        print("you scored an failed !")

    game_in_session = input("do you have another grade?")

    if game_in_session == "yes":
        game_in_session = True
    else: game_in_session = False
