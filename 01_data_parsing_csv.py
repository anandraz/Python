# @copyright-2021

import csv //CSV module

# take the input data from user and return data in form of list
def data(i):
    print("Event: ", i)

    my_list= []  # created empty list

    start_timestamp = int(input("Start Timestamp:"))
    my_list.append(start_timestamp)

    end_timestamp = int(input("End Timestamp:"))
    my_list.append(end_timestamp)

    return my_list

# create csv, open csv and parsing the user data into csv
def data_parse(my_list):

    file_object= open(rec_name + '.csv', 'a', newline= '')

    write_object= csv.writer(file_object)

    write_object.writerow(my_list)

# asking user to continue
def user_input():
    print("still you want to enter the data:")
    check= int(input("Continue press 1 exit 0: "))

    return check

rec_name = str(input("Enter the rec name: "))

i=1
while(1):
    my_list= data(i)
    i+=1

    data_parse(my_list)

    print("***********************************************************************************")
    check= user_input()

    if check== 1:
        continue
    elif check==0:
        exit(1)
    else:
        print("*************wrong enter*****************")
        check= user_input()




