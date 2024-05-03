import random
import time
com=["rock","paper","scissor"]

#REPEITION
def user_win():
    print("--------------------YOU WIN--------------------","\n        THE COMPUTER'S CHOICE WAS:",computer)
    user_win +=1
    user_win_count+=1
    print()

def user_lose():
    print("--------------------YOU LOSE--------------------","\n       THE COMPUTER'S CHOICE WAS:",computer)
    computer_win +=1
    computer_win_count+=1
    print()
    

    


rcc=input("ARE YOU INTERESTED IN PLAYING 'ROCK-PAPER-SCISSOR' (Y/N)? ").strip().lower()
print()

if rcc not in ["y","yes"]:
    print("------------------------------------------------------------------------")
    print()
    print("ALRIGHT, NO WORRIES, WE ARE ALWAYS AVAILABLE TO PLAY WITH YOU.")
    print("PLEASE COMEBACK ANYTIME TO PLAY WITH US.")
    print("\n---------------------------------THANK YOU------------------------------")
    
else:
    print("A SET OF THIS GAME HAS 3 ROUNDS IN IT , AT THE END YOU'LL BE DISPLAYED YOUR WIN COUNT.")
    set=input("ENTER HOW MANY SETS OF 'ROCK-PAPER-SCISSOR' YOU WOULD LIKE TO PLAY (IN NUMBERS):").strip()
    print()
    print()
    print()
    set_num=int(set)
    user_win_count=0
    user_set_count=0
    computer_win_count=0
    computer_set_count=0
    set_draw=0
    final_draw_count=0
    disq=0
    for g_set in range(set_num):
        user_win=0
        user_set=0
        computer_win=0
        computer_set=0
        draw=0
        for rounds in range(3):
            random.seed(time.perf_counter())
            rec=random.randint(0,2)
            computer=com[rec]
            ans=input("ENTER ANY ONE B/W (ROCK, PAPER or SCISSOR):").strip().lower()
            if ans=="rock" and computer=="paper":
                print("--------------------YOU LOSE--------------------","\n       THE COMPUTER'S CHOICE WAS:",computer.upper())
                computer_win +=1
                computer_win_count+=1
                print()
                
            elif ans=="rock" and computer=="scissor":
                print("--------------------YOU WIN--------------------","\n        THE COMPUTER'S CHOICE WAS:",computer.upper())
                user_win +=1
                user_win_count+=1
                print()
 
            elif ans==com[1] and computer==com[0]:
                print("--------------------YOU WIN--------------------","\n        THE COMPUTER'S CHOICE WAS:",computer.upper())
                user_win +=1
                user_win_count+=1
                print()

            elif ans==com[1] and computer==com[2]:
                print("--------------------YOU LOSE--------------------","\n       THE COMPUTER'S CHOICE WAS:",computer.upper())
                computer_win +=1
                computer_win_count+=1
                print()

            elif ans==com[2] and computer==com[0]:
                print("--------------------YOU LOSE--------------------","\n       THE COMPUTER'S CHOICE WAS:",computer.upper())
                computer_win +=1
                computer_win_count+=1
                print()

            elif ans==com[2] and computer==com[1]:
                print("--------------------YOU WIN--------------------","\n        THE COMPUTER'S CHOICE WAS:",computer.upper())
                user_win +=1
                user_win_count+=1
                print()

            elif ans==computer:
                print("----------------------DRAW----------------------","\n       THE COMPUTER'S CHOICE WAS:",computer.upper())
                draw+=1
                final_draw_count+=1
                print()

            else:
                print("----PLEASE WRITE FROM (ROCK, PAPER or SCISSOR) WITH CORRECT SPELLING AND TRY AGAIN----:")
                disq+=1
                print()
                


        for i in range(1):
            if computer_win > user_win:
                computer_set_count+=1

            elif computer_win < user_win:
                user_set_count+=1

            elif draw==3:
                set_draw+=1

            elif computer_win==user_win:
                set_draw+=1
                
            else:
                pass
                
            print()         
            print()
            print()

    print("             \\\YOU'VE SUCCESSFULLY CLEARED THIS GAME\\\                ")
    print("-------------------------------RESULTS----------------------------------")
    print()
    print("USER'S SET WINS:",user_set_count,     "        COMPUTER'S SET WINS:",computer_set_count)
    print("USER'S ROUND WINS:",user_win_count,   "      COMPUTER'S ROUND WINS:",computer_win_count)
    print("ROUND DRAWS COUNT:",final_draw_count,  "     SET DRAWS COUNT:",set_draw)
    print()
    print("DISQUALIFIED COUNT IF USER DIDN'T ENTER THE CORRECT SPELLING:",disq)
    print()
    print()
    print("PLEASE COME BACK ANYTIME TO PLAY WITH US, IT WAS FUN PLAYING WITH YOU.")
    print("-------------------------------THANK YOU--------------------------------")
    
        

