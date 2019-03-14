import pandas as pd
import csv
import sys

def get_match(df1,df2):
    match = set()
    try:
        with open('MATCH.csv','r') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            match = set(reader)
    except:
        print("No existing MATCH.csv file found, a new one will be made...\n")

    for absentee in df1['Absentee Property Address']:
        for vacancy in df2['Street Name 2 ']:
            if absentee.lower() == vacancy.lower():
                match.add(absentee)

    with open('MATCH.csv', 'w') as csvfile:
        file = csv.writer(csvfile, delimiter=',')
        for item in match:
            file.writerow(item)

    return "Done"

if __name__ == "__main__":
    arguments = sys.argv
    print(len(arguments))
    if len(arguments) != 3:
        print(arguments)
        print("Please give correct arguments, program is shutting down")
        exit()
    df1 = pd.read_excel(arguments[1])
    df2 = pd.read_excel(arguments[2])
    print(get_match(df1,df2))
