import random
#lists
teams = [254,1678,2403,1323]
question1 = ["The Cheesy Poofs","Citrus Circuits","Plasma Robotics","MadTown Robotics"]
question2 = ["2022","2015","Never","2023"]
question3 = []

#choose team
team = (random.randint(1, len(teams))-1)

print("FRC team quiz")
print("you will have to answer up to 3 questions about a random FRC team")
start=input("press y to start ")
if(start=="y"):
    difficulty=input("Select a difficulty(Hard,Medium,Easy) ")
if(difficulty=="Hard"):
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
            answer3=input("How many blue banners did " + str(teams[team]) +" get this last season")
        if(answer3==question3[team]):
            print("Correct!")
            print("You Won!!!")