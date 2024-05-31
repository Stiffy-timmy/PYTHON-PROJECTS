import csv
import random
from datetime import datetime, timedelta
import os
import sys

registrationNO = 1
csv_records_copy = []



# def exit():
#     exitInput = input("Do You Want To Exit This Entire Application Now ? (Y/N) ").strip().lower()
#     if exitInput in ['n','no'] or exitInput not in ['y','yes','n','no']:
#         print("Redirecting You To The Initial Registration Centre.....")
#         user_check()
    
#     else:
#       # To exit the program
#         # sys.exit()

#       # To forcefully terminate the program
#         print()
#         os._exit(0)

#     return exitInput


# ----CSV File(Entry)----
def file_write_1():
    global registrationNO
    global csv_records_copy

    with open ("registration.csv", "a", newline="") as fobj:
        record = []
        f = csv.writer(fobj)
        f.writerow(["Registration_Number","Name","Age","Gender"])
        print()
        while True:

            regisNo = str(registrationNO) 
            name = input("Enter your name: ").strip().lower()
            age = input("Enter your Age: ").strip()
            gender = input("Enter your Gender (Male / Female / Others): ").strip().lower()
            individuals = [regisNo, name, age, gender]
            record.append(individuals)
            print("Thank you for using our service!...")
            print()
            registrationNO += 1
            choice = input("Do You Want To Continue Registration For More Patients (Y/N) ? ").strip().lower()
            print()
            if choice in ['n','no'] or choice not in ['y','yes','n','no']:
                break
            
        f.writerows(record)
    

def file_write_2():
    global registrationNO
    global csv_records_copy

    with open ("registration.csv", "a", newline="") as fobj:
        record = []
        f = csv.writer(fobj)
        print()
        while True:
            
            regisNo = str(registrationNO)
            name = input("Enter your name: ").strip().lower()
            age = input("Enter your Age: ").strip()
            gender = input("Enter your Gender (Male / Female / Others): ").strip().lower()
            individuals = [regisNo, name, age, gender]
            record.append(individuals)
            print(f"Thank you for using our service!...")
            print()
            registrationNO += 1
            choice = input("Do You Want To Continue Registration For More Patients (Y/N) ? ").strip().lower()
            print()
            if choice in ['n','no'] or choice not in ['y','yes','n','no']:
                break
        csv_records_copy = record.copy()
        f.writerows(record)


# ----CSV File(Display-ALL-patients)----
def read_csv_in_chunks(start_index, chunk_size):
    records = []
    with open ("registration.csv","r") as file:
        csv_reader = csv.DictReader(file)
        for idx, row in enumerate (csv_reader, start=1):
            if idx < start_index:
                continue
            records.append(row)

            if len(records) == chunk_size:
                yield records
                records = []

        if records: #Yielding any remaining records
            yield records


# ----Sorting And Prioritizing Patients----
def prioritize_records(records):
    global csv_records
    prioritized = [record for record in records if int(record['Age']) > 60]
    others = [record for record in records if int(record['Age']) <= 60]
    sorted_records = prioritized + others
    for idx, record in enumerate(sorted_records, start=1):
        record['Registration_Number'] = str(idx)
    
    return sorted_records


# ----Function to print time slots----
def print_records_with_time(records, start_time):
    print("\n       Entry Time\t\t     Time Slot\t\t        Patient Slot")
    parent_time_slot = start_time.strftime("%I:%M %p") + " " + "Onwards Sharply"
    print(f"{parent_time_slot}\t\t\t\t\t\t", end="")
    for i, record in enumerate(records):
        time_slot = start_time.strftime("%I:%M %p")
        end_time = start_time + timedelta(minutes=4)
        end_hour = end_time.hour
        end_minute = end_time.minute
        if end_minute >= 60:
            end_hour += 1
            end_minute -= 60
        end_time_str = f"{end_hour:02d}:{end_minute:02d} {end_time.strftime('%p')}"
        print(f"\n\t\t{time_slot} - {end_time_str}\t\t{record['Name']}, Age: {record['Age']}, Gender: {record['Gender']}, Registration Number: {record['Registration_Number']}")
        start_time = end_time
    print("\n")

    # # Got a solution to escaping the cursor struck here
    # print("All Data Collected.....")
    # exit()



# ----Main Read Function (For All Registration)
def main_read():
    start_index = 1
    slot_range = 5
    start_time = datetime.strptime("08:00 AM", "%I:%M %p")
    working_hours_end = datetime.strptime("08:00 PM", "%I:%M %p")
    parent_time_slot = 1
    while start_time < working_hours_end:
        for chunk in read_csv_in_chunks(start_index, slot_range):
            sorted_records = prioritize_records(chunk)
            print_records_with_time(sorted_records, start_time)
            start_index += slot_range
            start_time += timedelta(minutes=slot_range * 4)  # Adjusted for 20 mins per patient slot
        parent_time_slot += 1


# ----Individual Search And Display----
def search(name, age):
    with open ("registration.csv","r") as file:
        reader = csv.reader(file)
        file.__next__()
        found = False
        for rcc in reader: 
              #CSV file doesn't contain nested lists because of reader.writerows
            if  name in rcc[1].strip().lower() and rcc[2].strip() == age:
                print()
                print(f"Name: {rcc[1]},  Age: {rcc[2]},  Gender: {rcc[3]},  Registration_Number: {rcc[0]}")
                found = True
               

        if not found:
            print()
            print("Unfortunately The Details Are Not Available or It Seems The Userinput Was not Correct.\nPlease Try Again...")
                

           

# ----Non Volatile Programming----
def save_value(a):
    with open ("value.txt","a") as file:
        file.write(str(a)+"\n")


def load_latest_value():
    try:
        with open("value.txt","r") as file:

            #Readline(s) = returns a list containing all lines in a (.txt) file
            lines=file.readlines() 
            if lines:
                return int(lines[-1])
            else:
                return 0
            
    except:
        return 0


# ----SubMain Function----
def user_check():
    while True:
        print()
        print()
        print("------This Is The Registraion Centre For Vaccination------")
        print("To Get Into The Registration Process (Press 1)\nTo Display Your Individual Registration Data (Press 2)\nTo Display Everyone's Registration Data (Press 3)\n(Press Any Other Key to Quit The Menu) ")
        userInput = input("Enter Your Response: ").strip()
        if userInput == "1":
            file_open_count = load_latest_value()
            file_open_count += 1
            save_value(file_open_count)

            # If file is opened for the first time w.r.t to opening it more than once
            if file_open_count == 1:
                file_write_1()
                choice = input("Do You Want To Continue The Initial Registration Process Or looking Into The Patient's History (Y/N) ? ").strip().lower()
                if choice in ['n','no'] or choice not in ['y','yes','n','no']:
                    break

            else:
                file_write_2()
                choice = input("Do You Want To Continue The Initial Registration Process Or looking Into The Patient's History (Y/N) ? ").strip().lower()
                if choice in ['n','no'] or choice not in ['y','yes','n','no']:
                    break
        
        elif userInput == "2":
            while True:
                print()
                nme = input("Please Enter The Patient's (First Name): ").strip().lower()
                ag = input("Please Enter The Patient's Age: ").strip()
                search(nme,ag)
                print()
                choice = input("Do You Want To Continue Searching (Y/N) ? ").strip().lower()
                print()
                if choice in ["n","no"] or choice not in ['y','yes','n','no']:
                    break
            
            innerInput = input("Do You Want To Continue The Initial Registration Process Or looking Into The Patient's History (Y/N) ? ").strip().lower()
            if innerInput in ['n','no'] or innerInput not in ['y','yes','n','no']:
                break

        elif userInput == "3":
            main_read()
            
                   
        else:
            break
        
    print("Thank You For Using This Application...")
    print()


# ----MAIN---
def main():
    user_check()



main()
