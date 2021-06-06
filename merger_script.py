# Put this script in the same location of the text files

firstfile = "sample_ben.txt"  #  Enter the name of Output File 
for i in range (1,70527,60):
    secondfile = "article_" + str(i) + ".txt"
    f1 = open(firstfile, 'a+')
    f2 = open(secondfile, 'r')
    print(i)
    f1.write(f2.read())
    f1.seek(0)
    f2.seek(0)
    f1.close()
    f2.close()
