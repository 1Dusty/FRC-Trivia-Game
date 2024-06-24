import random
#lists
teams = [254,1678,2403,1323,118,148,2056,1690]
question1 = ["The Cheesy Poofs","Citrus Circuits","Plasma Robotics","MadTown Robotics","Robonauts","Robowranglers","OP Robotics","Orbit"]
question2 = ["2022","2015","Never","2023","2015","2018","Never","2024"]
question3 = ["3","4","1","3","8","2","5","5"]
question4 = ["California","California","Arizona","California","Texas","Texas","Canada","Israel"]
question5 = ["Yes","No","No","No","Yes","No","No","No"]

#choose team
team = (random.randint(1, len(teams))-1)

print("FRC team quiz")
print("you will have to answer up to 3 questions about a random FRC team")
start=input("press y to start")
if(start=="y"):
    difficulty=input("Select a difficulty(Easy, Medium, Hard, Expert, Expert+)")
if(difficulty=="Expert+"):
    questions=5
elif(difficulty=="Expert"):
    questions=4
elif(difficulty=="Hard"):
    questions=3
elif(difficulty=="Medium"):
    questions=2
else:
    questions=1
print("You will have to answer " + str(questions) + " questions about FRC team " + str(teams[team]))
answer1=input("What is team " + str(teams[team]) +"'s team name?")
if(answer1==question1[team]):
    print("Correct!")
    if(questions==1):
        print("You Won!!!")
    else:
        answer2=input("When did " + str(teams[team]) +" last win the world championship?")
        if(answer2==question2[team]):
            print("Correct!")
            if(questions==2):
                print("You Won!!!")
            else:
                answer3=input("How many blue banners did " + str(teams[team]) +" get this last season?")
                if(answer3==question3[team]):
                    print("Correct!")
                    if(questions==3):
                        print("You Won!!!")
                    else:
                        answer4=input("Where is " + str(teams[team]) +" from?(what state, or country if outside of us)")
                        if(answer4==question4[team]):
                            print("Correct!")
                            if(questions==4):
                                print("You Won!!!")
                            else:
                                answer5=input("did team " + str(teams[team]) +" have a turret on their robot this year?")
                                if(answer5==question5[team]):
                                    print("Correct!, You win!!!")
                        else:
                            print("incorrect, the answer was " + question4[team])
                else:
                    print("incorrect, the answer was " + question3[team])
        else:
            print("incorrect, the answer was " + question2[team])
else:
    print("incorrect, the answer was " + question1[team])