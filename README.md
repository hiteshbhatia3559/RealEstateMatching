Problem statement
```
I am a RE investor and currently I purchase data from (2) sources, so there are two different lists: Absentee owners and vacant properties. It would be nice to know when I have a property that is on BOTH lists (absentee and vacant). 

What might make this different is how to keep all information available- would it be a type of .csv file database? I have just started, so my data is under 5,000 lines I would guess. 

I would like to have a MASTER list for absentee owners, a MASTER list for vacant owners, and then a MATCH list showing that there is a property that is on (2) lists. As noted above .csv files will need to always be added to MASTER lists in order to Save my information and also I need to prevent saving duplicate property info. 

Once there is matching information (a property is on 2 lists), then the information is forwarded to the MATCH list.

```

Instructions
``` 
1. Download and install Python 3.5 from here : Install Python 3.5 from here and make sure pip and python point to Python 3.5 : https://www.python.org/ftp/python/3.5.0/python-3.5.0-amd64.exe
2. Install pandas by opening a command prompt in the project directory and typing 'pip install pandas'
3. Finally, type 'main.py absentee.xlsx vacant.xlsx', where the names are substituded with the filenames
3.5 For the data provided, use 'main.py JAXAbsenteeOwnerList0218.xlsx JAXVacantPropertyList0218.xlsx'
4. If a MATCH.csv does not exist, the program will create one (there will never be a duplicate)
5. If a MATCH.csv exists in the same project directory, the MATCH.csv will automatically be read and merged, 
and a new MATCH.csv will be generated that will have data from the previous run and this one
```

NOTE:
```
1. The Excel files MUST be in the same format and layout they are currently, otherwise the program may require changes in order to run correctly
2. There is no limitation to the data being stored
```