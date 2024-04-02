with open('file1.txt','r') as f1:
    lines=f1.readlines()
n=int(input("Enter the line number: "))
with open('file2.txt','w') as f2:
    for line in lines:
        if line.rstrip("\n")!=line:
            f2.write(line)
f1.close()
f2.close()