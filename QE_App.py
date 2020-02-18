#!/usr/bin/python3

"""
This program computes for a given sample: Average siblings, Favourite foods and Births per month
Usage: QE_App.py inputfile.json/csv

The program assumes input is well-formatted and valid


"""



import sys
import json
import re
import csv
from datetime import datetime,timezone,timedelta
import calendar
from collections import Counter




""" convert timestamp and timezone offset to date/month
Args: timestamp, timezone offset in hour and minutes
Returns: month as string

"""
def convert_timestamp(timestamp_val,hour_delta,min_delta):

    newtimezone = timezone(timedelta(hours = hour_delta,minutes = min_delta))

    try:
        dt = datetime.fromtimestamp(timestamp_val,tz=newtimezone)
    except OverflowError:
        print("timestamp too large")
        sys.exit(1)

    month_str = calendar.month_name[dt.month]

    return month_str




""" process input json file

"""
def compute_json(input_file):

    # use json library to load json data
    person_list = json.load(input_file)


    num_of_persons = len(person_list)

    total_num_siblings = 0
    favourite_foods = {}
    birthday_months = {}

    for item in person_list:
        for key in item:
            if(key == 'siblings'):
                total_num_siblings += int(item[key])

            if(key == 'favourite_food'):
                food_type = item[key]
                if(food_type not in favourite_foods):
                    favourite_foods[food_type] = 1
                else:
                    favourite_foods[food_type] += 1


        
            if(key == 'birth_timezone'):
                timezone_val = item[key]

            if(key == 'birth_timestamp'):
                timestamp_val = int(item[key])
                # change timestamp into secs
                timestamp_val_sec = int(timestamp_val/1000)


        timezone_slist = timezone_val.split(':')
        hour_offset = int(timezone_slist[0])
        min_offset = int(timezone_slist[1])

        month_str = convert_timestamp(timestamp_val_sec,hour_offset,min_offset)
        if(month_str not in birthday_months):
            birthday_months[month_str] = 1
        else:
            birthday_months[month_str] += 1



    avg_num_siblings = round(total_num_siblings/num_of_persons)


    # printing output could be moved into a separate function
    print("\n")
    print("Average siblings: ", avg_num_siblings)



    dict_counter = Counter(favourite_foods)
    top_three = dict_counter.most_common(3)

    print("\n")
    print("Favourite foods: ")
    print(top_three[0][0], top_three[0][1])
    print(top_three[1][0], top_three[1][1])
    print(top_three[2][0], top_three[2][1])

    # to be simplified
    print("\n")
    print("Births per month: ")
    if('January' in birthday_months):
        print('January', birthday_months['January'])

    if('February' in birthday_months):
        print('February', birthday_months['February'])

    if('March' in birthday_months):
        print('March', birthday_months['March'])

    if('April' in birthday_months):
        print('April', birthday_months['April'])

    if('May' in birthday_months):
        print('May', birthday_months['May'])

    if('June' in birthday_months):
        print('June', birthday_months['June'])

    if('July' in birthday_months):
        print('July', birthday_months['July'])

    if('August' in birthday_months):
        print('August', birthday_months['August'])

    if('September' in birthday_months):
        print('September', birthday_months['September'])

    if('October' in birthday_months):
        print('October', birthday_months['October'])

    if('November' in birthday_months):
        print('November', birthday_months['November'])

    if('December' in birthday_months):
        print('December', birthday_months['December'])




    return(avg_num_siblings,top_three,birthday_months)





""" process input csv file

"""
def compute_csv(input_file):

    # use csv library to read csv file
    csvreader = csv.reader(input_file)

    header_row = next(csvreader)

    total_num_siblings  = 0

    favourite_foods = {}
    birthday_months = {}

    i=0
    for row in csvreader:
        total_num_siblings += int(row[2])
        i += 1

        food_type = row[3]
        if(food_type not in favourite_foods):
            favourite_foods[food_type] = 1
        else:
            favourite_foods[food_type] += 1

        timezone_val = row[4]
        timestamp_val = int(row[5])
        timestamp_val_sec = int(timestamp_val/1000)


        timezone_slist = timezone_val.split(':')
        hour_offset = int(timezone_slist[0])
        min_offset = int(timezone_slist[1])

        month_str = convert_timestamp(timestamp_val_sec,hour_offset,min_offset)
        if(month_str not in birthday_months):
            birthday_months[month_str] = 1
        else:
            birthday_months[month_str] += 1


    avg_num_siblings = round(total_num_siblings/i)

    print("\n")
    print("Average siblings: ", avg_num_siblings)


    dict_counter = Counter(favourite_foods)
    top_three = dict_counter.most_common(3)

    print("\n")
    print("Favourite foods: ")
    print(top_three[0][0], top_three[0][1])
    print(top_three[1][0], top_three[1][1])
    print(top_three[2][0], top_three[2][1])


    print("\n")
    print("Births per month: ")
    if('January' in birthday_months):
        print('January', birthday_months['January'])

    if('February' in birthday_months):
        print('February', birthday_months['February'])

    if('March' in birthday_months):
        print('March', birthday_months['March'])

    if('April' in birthday_months):
        print('April', birthday_months['April'])

    if('May' in birthday_months):
        print('May', birthday_months['May'])

    if('June' in birthday_months):
        print('June', birthday_months['June'])

    if('July' in birthday_months):
        print('July', birthday_months['July'])

    if('August' in birthday_months):
        print('August', birthday_months['August'])

    if('September' in birthday_months):
        print('September', birthday_months['September'])

    if('October' in birthday_months):
        print('October', birthday_months['October'])

    if('November' in birthday_months):
        print('November', birthday_months['November'])

    if('December' in birthday_months):
        print('December', birthday_months['December'])



    return(avg_num_siblings,top_three,birthday_months)





""" main function to enable importing module

"""
def main():
    numargs = len(sys.argv)


    if(numargs != 2):
        print("usage: QE_App.py inputfile.json/csv")
        sys.exit(1)


    # check file extension is json or csv
    split_list = sys.argv[1].split('.')

    if(re.match('^json$|^csv$',split_list[1],re.IGNORECASE) is None):
        print("not the correct extesion")
        print("usage: QE_App.py inputfile.json/csv")
        sys.exit(1)


    ext_type = split_list[1].lower()


    filearg = sys.argv[1]
    print("input file is: ", filearg)

    try:
        input_file = open(filearg)
    except:
        print("can't open input file, check file path or file exists")
        exit(1)




    if(ext_type == "json"):
        print("processing json input")
        compute_json(input_file)

    else:
        print("processing csv input")
        compute_csv(input_file)


    input_file.close()





if __name__ == '__main__':
    main()

