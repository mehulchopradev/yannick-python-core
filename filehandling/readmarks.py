import csv

with open('school/marks.csv') as fs:
    csvreader = csv.reader(fs)
    with open('school/totalmarks.csv', mode='w') as fo:
        csvwriter = csv.writer(fo, delimiter='|')
        for line in csvreader:
            csvwriter.writerow([line[0], float(line[1]) + float(line[2]) + float(line[3])])
