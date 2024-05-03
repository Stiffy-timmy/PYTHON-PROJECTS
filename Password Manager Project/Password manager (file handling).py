import csv
import os


#IMPORTANT FUNCTION TO HELP THE SYSTEM REMEMBER VALUES
def save_value(a):
    with open ("value.txt","a") as file:
        file.write(str(a)+"\n")
        

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
    

#FUNCTIONS

def write1():
    with open("passwords.csv","a",newline="") as fobj:
            
            f=csv.writer(fobj)
            
            f.writerow(["sl_no","category (app/website)","name of (app/website)","passwords"])
            
            record=[]
            while True:
                sl=input("Enter serial number: ").strip().lower()
                cat=input("Enter category (app/website): ").strip().lower()
                name=input("Enter name of (app/website): ").strip().lower()
                password=input("Enter the respective password: ").strip().lower()
                rec=[sl,cat,name,password]
                record.append(rec)
                choice=input("You want to write more records into the file (Y/N)? ").strip().lower()
                print()
                if choice in ['n','no']:
                    break
            f.writerows(record)
            print()
            print("Records have successfully been inserted.")
            print("All operations are completed.")


def write2():
     with open("passwords.csv","a",newline="") as fobj:
           
            f=csv.writer(fobj)
            record=[]
            while True:
                sl=input("Enter serial number: ").strip().lower()
                cat=input("Enter category (app/website): ").strip().lower()
                name=input("Enter name of (app/website): ").strip().lower()
                password=input("Enter the respective password: ").strip().lower()
                rec=[sl,cat,name,password]
                record.append(rec)
                choice=input("You want to write more records into the file (Y/N)? ").strip().lower()
                print()
                if choice in ['n','no']:
                    break
            f.writerows(record)
            print()
            print("Records have successfully been inserted.")
            print("All operations are completed.")


def show1():
    file=input("Enter the file you are looking out for: ")+".csv"
    st_file=file.strip().lower()
    abs=os.path.abspath(st_file)
    if os.path.isfile(abs):
        print("File exists, you may read the contents.")
        print()
        with open("passwords.csv","r") as fobj:
            read=csv.reader(fobj)
            for data in read:
                print(data)
            print()
            print("All records have successfully been displayed.")
    else:
        print("File doesn't exist.")
        

def show2():
    print("As you are opening this file again, we would like to display the previous contents so that you can write new records into it accordingly. ")
    print()
    with open("passwords.csv","r") as fobj:
            read=csv.reader(fobj)
            for data in read:
                print(data)
            print()
            print("All records have successfully been displayed.")
            print("you may begin writing new contents now.")
            print()
    

        
    

#--MAIN--
print("To (WRITE) new passwords into the file (PRESS:- 1)\nTo (SEE) previous passwords from file (PRESS:- 2)")
res=input("Enter your response: ").strip()
print()

if res=='1':
    master_password=input("Enter the master password: ").strip().lower()
    print()
    
    if master_password=='prajurjya':
        print("Master password is correct, you've successfully entered the workspace.")
        file_count=load_latest_value()
        file_count+=1
        save_value(file_count)
        print("Till now, the number of times you have opened this file is:",file_count)
        print()

        if file_count==1:
            write1()

        else:
            show2()
            write2()
    else:
        print("Master_password is incorrect, run the program and try again.")
        

elif res=='2':
    master_password=input("Enter the master password: ").strip().lower()
    print()

    if master_password=='prajurjya':
        print("Master password is correct, you've successfully entered the workspace.")
        show1()
        
    else:
        print("Master_password is incorrect, run the program and try again.")
        

else:
    print("Please run the program again and press from the choices provided correctly.")
    
        
        



















    
    
