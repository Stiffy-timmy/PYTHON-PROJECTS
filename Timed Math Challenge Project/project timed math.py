
#HOW TO USE eval() function in python.(it vaildates a string expression as a normal expression only if it is SYMANTIC
#and meaningful)
import random
import time

operator=["+","-","*","/"]
min_operand=3
max_operand=12
total_problems=10

def generateQuestions():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operate=random.choice(operator)

    expr = str(left) + " " + operate + " " + str(right)
    answer=eval(expr)
    ans=round(answer,2)
    print(expr,ans)
    return expr, ans

#SEE the writing technique for multiple ASSIGNMENT
#TO KEEP ASKING UNTILL USER INPUTS THE CORRECT ANSWER, USE (while loop)

input("Press Enter to start!")
print("-----------------")
start_time=time.time()

for i in range(total_problems):
    expr,ans=generateQuestions()
    while True:
        guess=input("Problem #" + str(i+1) + ": " + expr + "=")
        if guess==str(ans):
            break

end_time=time.time()
total_time=end_time-start_time
#Rouunding off the time to the nearest digit
totalTime=round(end_time-start_time,2)
print("-----------------")
print("Nice work! you finished in",total_time,"seconds!")
print("Nice work! you finished in",totalTime,"seconds!")