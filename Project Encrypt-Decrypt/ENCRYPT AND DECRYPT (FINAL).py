import random
import csv

#THERE'S SOMETHING WRONG WITH RANDOM MODULE 
#key1=["$*76_+76","HY_87$||( &j","@^$|{__Hj6>$@_2"]
#key2=["$%89&","h_252_%$@","_&76^_}"]


def encrypt(str,key1="@^90:*$b+w",key2="6^_|{}"):
    with open("words.csv","a",newline='') as fobj:
        write=csv.writer(fobj)
        write.writerow(["encrypted","decrypted"])
        

  
        lst=str.split()
        random.shuffle(lst)
        join_list=[]
        for i in lst:
            str_encrypt=key1.join(i)
            join_list.append(str_encrypt)

        final_encrypt=key2.join(join_list)
        write.writerow([final_encrypt,str])
        
    
        print()
        print("ENCRYPTION SUCCESSFULL.....")
        print("YOUR ENCRYPTED MESSAGE IS:",final_encrypt)


      
        
def encrypt_search(code):
    try:
        with open("words.csv","r") as fobj:
            reader=csv.reader(fobj)
            flag=0
            for rec in reader:
                if rec[0]==code:
                    print("DECRYPTED MESSAGE IS:",rec[1])
                    flag=1
                    
            if flag==0:
                print("ENCRYPTED MESSAGE IS INVALID.")
    except:
                    
        #INCASE THE FILE ITSELF DOESN'T EXIST, WE NEED TO GIVE SOME KIND OF ERROR MESSAGE TO THE USER AS WE ARE OPENING THIS IN "READ" MODE...
        print("ENCRYPTION-DECRYPTION LIBRARY DOESN'T EXIST....")
        
    
    
        

print("THIS IS A PROGRAM TO HELP USER EITHER ENCRYPT OR DECRYPT A MESSAGE.")
print("TO ENCRYPT A MESSAGE (PRESS:- 1)\nTO DECRYPT A MESSAGE (PRESS:- 2)")
response=input("ENTER YOUR RESPONSE FROM ABOVE:").strip().lower()
print()
if response=="1":
    m_pass=input("ENTER MASTER PASSWORD:").strip().lower()
    print()
    
    if m_pass=="prajurjya":
        print("MASTER PASSWORD IS CORRECT, YOU'VE SUCCESSFULLY ENTERED THE WORKSPACE.")
        string=input("ENTER A MESSAGE (SENTENCE/WORD) YOU WANT TO ENCRYPT:").strip().lower()
        #random.shuffle(key1)
        #random.shuffle(key2)

        print("YOUR ENCRYPTED MESSAGE IS BEING PROCESSED.")
        encrypt(string)    
            
    else:
        print("MASTER PASSWORD IS INCORRECT.")

elif response=="2":
    m_pass=input("ENTER MASTER PASSWORD:").strip().lower()
    print()
    
    if m_pass=="prajurjya":
        print("MASTER PASSWORD IS CORRECT, YOU'VE SUCCESSFULLY ENTERED THE WORKSPACE.")
        e_message=input("ENTER THE ENCRYPTED MESSAGE:").strip().lower()
        encrypt_search(e_message)

    else:
        print("MASTER PASSWORD IS INCORRECT.")

else:
    print("PLEASE ENTER A VALID RESPONSE FROM THE GIVEN INSTRUCTIONS.")
        
    
    
       
