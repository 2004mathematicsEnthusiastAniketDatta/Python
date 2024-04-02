with open('first.txt','r')as f1, open('second.txt','w') as f2:
    for lines in f1:
        words=lines.split()
        for word in words:
            if word[0] in 'aeiouAEIOU':
                f2.write(word+'\n')
f1.close()
f2.close()