import random
import time
import mysql.connector as c
con=c.connect(host='localhost',
              user='root',
              passwd='prajurjyaask007',
              database='quiz')

#APPRECIATIONS

aps=["-----OUTSTANDING, THE ANSWER IS CORRECT----","----EXCEPTIONALLY GOOD, YOUR ANSWER IS CORRECT----",
     "----MARVELOUS, MAYBE YOU ARE A GENIUS----","----SPLENDID, IT'S THE CORRECT ANSWER----",
     "----IMPRESSIVE, YOU SEEM TO BE A COMPETITIVE ONE----","----PHENOMENAL, YOUR ANSWER IS CORRECT----",
     "----NOTEWORTHY, MAYBE IT ISN'T SO TOUGH FOR YOU----","---EXPLEMERY, THE ANSWER IS CORRECT----",
     "----OUTSTANDING, YOU'VE GOT THE CORRECT ANSWER----","----TOP-NOTCH, YOU ARE DOING GREAT----",
     "----AWE-INSPIRING, MAYBE WE NEED TO RAISE THE QUESTION'S DIFFICULTY LEVEL----",
     "----BRILLIANT, THE ANSWER IS CORRECT----"]

cursor=con.cursor()
print("We would like you to play this quiz game with us\nAre you interested(Y/N)?")
response=input("Enter your response:").strip().lower()
print()
if response not in ["y","yes"]:
        print("---------------------------------------------------------------------------------------")
        print()
        print("ALRIGHT, NO WORRIES, WE ARE ALWAYS AVAILABLE TO PLAY WITH YOU.")
else:
        print("That's the spirit, you will be asked some MCQs.\nPlease follow the instructions and give it your all.")
        print()

        query="select*from booklet"
        cursor.execute(query)
        data=cursor.fetchall()


        for list in data:
                for tuple in range(5):   #range is 5 because i don' want to print the answers also
                    print(list[tuple])
                ans=input("Enter your answer (option / Full answer from the option):").strip().lower()
                for tup in range(5,6):
                    ans2=list[tup].partition("-")
                    if ans in ans2:
                            random.seed(time.perf_counter())
                            num=random.randint(0,11)
                            print(aps[num])
                    
                    else:
                        print("Unfortunately you've got it wrong, the correct answer is:","".join(ans2))
                print()

if response in ["y","yes"]:            
        print()
        print("---------------------------------------------------------------------------------------")
        print()
        print("CONGRATULATIONS, YOU'VE SUCCCESSFULLY CLEARED THIS GAME.")
        print("BY ANY CHANCE IF YOU'VE GOT SOME OF THE ANSWERS WRONG, DON'T BE DEMOTIVATED.\nIT'S ALL ABOUT MAKING PROGRESS, WE NEED TO IMPROVE OUR SKILLS AND NEVER STOP LEARNING.")
        print()
        print("PLEASE COMEBACK ANYTIME TO TEST YOUR SKILLS.\n")
        print("---------------------------------------THANK YOU---------------------------------------")
else:
        print("PLEASE COMEBACK ANYTIME TO TEST YOUR SKILLS.\n")
        print("---------------------------------------THANK YOU---------------------------------------")
        

