c=0
with open('INDIA.txt','r') as f:
    for lines in f:
        lines=lines.title()
        words=lines.split()
        for word in words:
            if word=='India':
                c+=1
f.close()
print("The word India occurs",c,"times in the file")