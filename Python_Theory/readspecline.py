with open('file1.txt','r') as f1:
    line=f1.readlines()
    n=int(input('Enter the line number: '))
    print(line[n-1])
    f1.close()