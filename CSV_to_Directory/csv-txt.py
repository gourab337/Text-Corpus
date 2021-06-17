# -*- coding: utf-8 -*-

import csv

csv_list = []
sl_no = []
hin = []
ben = []

with open('Sample CSV.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        try:
            csv_list.append([int(row[0]),row[1],row[2]])
            sl_no.append(int(row[0]))
            hin.append(row[1])
            ben.append(row[2])
        except:
            pass

'''for item in csv_list:
    print(item)
for item in ben:
    print(item)
for item in hin:
    print(item)
'''

file = open("csv_output.txt","a")

for item in hin:
    file.write('"<e><p><l>')
    file.write(str(item)) 
    file.write('</l><r><s n="num"/><s n="ord"/><s n ="m"/></r></p></e>"')
    file.write("\n")
file.close()


