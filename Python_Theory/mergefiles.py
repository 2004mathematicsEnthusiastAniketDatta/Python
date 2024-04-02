with open('file1.txt','r') as f1, open('file2.txt','r') as f2, open ('file3.txt','w') as f3:
    for line in f1:
        f3.write(line+'\n')
    for line in f2:
        f3.write(line)
    f1.close()
    f2.close()
    f3.close()