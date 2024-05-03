#IMPORTANT CONCEPTS REGARDING FOR MAKING (SYSTEM --- NON-VOLATILE)
def save_value(a):
    with open ("value.txt","a") as file:
        file.write(str(a)+"\n")
        print("value of a saved successfully")
        print("saved values is",a)

def load_latest_value():
    try:
        with open("value.txt","r") as file:
            lines=file.readlines()
            if lines:
                return int(lines[-1])

            else:
                return 0
    except:
        return 0




#after performing some task
p=load_latest_value()
a=p+1

save_value(a)


print("latest value of a =",a)
