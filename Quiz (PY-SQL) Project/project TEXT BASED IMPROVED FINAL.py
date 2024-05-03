import random
booklet={"1. What is the capital of India?":["a. Delhi\n b. Mumbai\n c. Chennai\n d. Gujrat",["a","delhi"]],
         "2. What is 2+2?":["a. 3\n b. 4\n c. 10\n d. 1",["b","4"]]}

#FUNCTIONS
def question_call(dict):
    
    for i in dict:
        global ans
        print(i,"\n",dict[i][0])
        ans=input("Enter your answer (option / Full answer from the option):").strip().lower()
        
        if ans in dict[i][1]:
            print("Absolutely correct")
        else:
            print("Unfortunately you've got it wrong. The correct answer is:",". ".join(dict[i][1]))
        print()
 


#--MAIN--
                                                                                       
print("We would like you to play this quiz game with us")
ans=input("Are you interested in playing(Y/N)?").strip().lower()
print()
if ans not in ['y','yes']:
    print("Alright, no worries. we are always available to play with you")
    print()
    print("Please comeback anytime to test your skills\n-----THANK YOU-----")
else:
    print("That's the spirit, you will be asked some MCQs.\nPlease follow the instructions and give it your all.")
    print()
    question_call(booklet)
    print()
    print("Congratulations, you've successfully cleared this game.")
    print("By any chance, if you got some of the answers wrong, don't be demotivated.\nIt's all about making progress, we need to improve our skills and never stop learning.")
    print()
    print("Please comeback anytime to test your skills.\n-------------THANK YOU-------------")
    
