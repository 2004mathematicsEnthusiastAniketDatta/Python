res=0
with open('file1.txt','r') as f1:
    line=f1.readlines()
    words=f1.read().split()
    for word in words:
        i=words.index(word)
        if(i%2==0):
              res=word
f1.close()       
print(res)








