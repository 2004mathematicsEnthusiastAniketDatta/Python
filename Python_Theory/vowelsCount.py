count=0
with open('Diary.txt','r') as f:
    for lines in f:
        words=lines.split()
        for word in words:
            for letter in word:
                if letter in 'aeiouAEIOU':
                    count=count+1
f.close()
print("vowel count within file:",count)
