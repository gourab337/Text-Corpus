# -*- coding: utf-8 -*-
def main():

    file  = open('sample_ben.txt', 'r').read()
    end_symbol  = "।"
    count = file.count(end_symbol)

    print(count)

main()