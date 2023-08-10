# Wriing Code for KBC Game
# First we have to import libraries like random and time to use in our code
import random
import time
# Second we have to write a code to welcome the candidate
for i in range(80):
    print("*", end="")
    time.sleep(0)
print()
print("\t\t\t Welcome to")
print("\t\t\tKon Banega Crorepati (Pak Version)")
for i in range(80):
    print("*", end="")
    time.sleep(0)
print()
a= input("Enter Your Name:")
for i in range(80):
    print("*", end="")
    time.sleep(0)
print()
print("OK", a, "Let's Start The Game")
time.sleep(1)
questions= ["What is the capital of Pakistan",
            "Who is the current Prime Minister of Pakistan", "Who is the most popular leader in Pakistan", "Which is the famous and historic city of Pakistan?", "Who have won Noble Prize in 1979?"]
answer = ["Islamabad", "Shehbaz Sharif", "Imran Khan", "Lahore", "Abdus Salam"]
wronganswer = [["Karachi", "Multan", "Sialkot"], ["Nawaz Sharif", "Asif Ali Zardari", "Imran Khan"],["Nawaz Sharif","Maryam Nawaz","Bilawal Bhuto"],["Multan", "Faisalabad", "Peshawar"],["Malala Yousaf Zai", "DR AQ Khan","Jameel Farooqi"]]
attempquestion = []
count = 1
amount = 0
while True:
    while True:
        selectquestion = random.choice(questions)
        if selectquestion in attempquestion:
            pass
        elif selectquestion not in attempquestion:
            attempquestion.append(selectquestion)
            questionindex= questions.index(selectquestion)
            correctanswer= answer[questionindex]
            break
    optionlist= []
    inoptionlist= []
    optioncount= 1
    while optioncount<4:
        optionselection=random.choice(wronganswer[questionindex])
        if optionselection in inoptionlist:
            pass
        elif optionselection not in inoptionlist:
            optionlist.append(optionselection)
            inoptionlist.append(optionselection)
            optioncount += 1
    optionlist.append(correctanswer)
    alreadydisplay=[]
    optiontodisplay=[]
    a1=True
    while a1:
        a=random.choice(optionlist)
        if a in alreadydisplay:
         pass
        else:
            alreadydisplay.append(a)
            optiontodisplay.append(a)
            a1=not True
    a1=True
    while a1:
        b = random.choice(optionlist)
        if b in alreadydisplay:
            pass
        else:
            alreadydisplay.append(b)
            optiontodisplay.append(b)
            a1 = not True
    a1 = True
    while a1:
        c = random.choice(optionlist)
        if c in alreadydisplay:
            pass
        else:
            alreadydisplay.append(c)
            optiontodisplay.append(c)
            a1 = not True
    a1 = True
    while a1:
        d = random.choice(optionlist)
        if d in alreadydisplay:
            pass
        else:
            alreadydisplay.append(d)
            optiontodisplay.append(d)
            a1 = not True
    right_answer=""
    if correctanswer==a:
        right_answer="a"
    elif correctanswer==b:
        right_answer="b"
    elif correctanswer==c:
        right_answer="c"
    elif correctanswer==d:
        right_answer="d"
    print("--------------------------------------------------------------------------------------------")
    print("\t\t\tAmount Win - ", amount)
    print("--------------------------------------------------------------------------------------------")
    time.sleep(1)
    print("\n\t\tQuestion ", count, " on your Screen")
    print("--------------------------------------------------------------------------------------------")
    time.sleep(1)
    print("  |  Question - ", selectquestion)
    print("--------------------------------------------------------------------------------------------")
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  A. ", a)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  B. ", b)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  C. ", c)
    print("\t-----------------------------------------------------------------------------")
    time.sleep(1)
    print("\t|  D. ", d)
    print("\t-----------------------------------------------------------------------------")
    useranswer = input("\t\tEnter Correct Option\t   or \t press Q to quit.\n\t\t\t...").lower()
    if useranswer == right_answer:
        if count == 1:
            amount = 1000000
        elif count == 2:
            amount = 2000000
        elif count == 3:
            amount = 5000000
        elif count == 4:
            amount = 10000000
        elif count == 5:
            amount = 50000000
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("*********************************************************************************")
            print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
            print("\t\t\t|||||||||| You Won The Game ||||||||||")
            print("*********************************************************************************")
            print("\n\n\t\t You Won Rs. ", amount)
            print()
            break
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("*********************************************************************************")
        print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
        print("\t\t\t|||||||||| Right Answer ||||||||||")
        print("*********************************************************************************")
        count += 1
    elif useranswer == "q":
        print("\n\n\t\t You Won Rs. ", amount)
        break
    else:
        print("*********************************************************************************")
        print("\t\t\tWrong Answer")
        print("*********************************************************************************")
        print("\n\n\t\t \tYou Won Rs. ", amount)
        print("*********************************************************************************")

        break
