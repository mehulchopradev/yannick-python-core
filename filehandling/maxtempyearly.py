from glob import glob
from fileinput import input
import csv

# dict data structure
yeartemp = {}

basepath = 'weather_data_input'
weatherdatafiles = glob(basepath + '/weather_data_set_*')

with input(files=weatherdatafiles) as f:
    csvreader = csv.reader(f, delimiter='|')
    for line in csvreader:
        # tokens = line.rstrip('\n').split('|') # remove the trailing \n when reading a line from the file
        if len(line) == 5 and line[4] != '' and line[4] != 'NA':
            year = int(line[1])
            temp = float(line[4])

            if year not in yeartemp:
                yeartemp[year] = temp # adding an entry in the dictionary
            else:
                tempfound = yeartemp[year]
                if temp > tempfound:
                    yeartemp[year] = temp # update an entry in the dictionary

print(yeartemp)
