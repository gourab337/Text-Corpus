# -*- coding: utf-8 -*-
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

my_file = os.path.join(THIS_FOLDER, 'Hin_Small.txt')
my_file2 = os.path.join(THIS_FOLDER, 'Hin_Small_2.txt')

f1 = open(my_file2, 'a')
f = open(my_file, 'r')
#count_lines = 0   # number of lines: 80237
#step = 5    # to get ~20,000 lines (some lines are big)
#count = 0
itr = 1
for line in f:
    #count += 1
    #if (count%step == 0):
        #f1.write(str(itr))
        f1.write(f"{itr:05n}") 
        f1.write('. ')
        f1.write(line)
        f1.write('\n')
        itr += 1

f.close()
f1.close()

