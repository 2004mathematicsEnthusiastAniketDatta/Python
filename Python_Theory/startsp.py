with open('Diary.txt','r') as f:
    for lines in f:
         if(lines[0]=='p' or lines[0]=='P'):
                print(lines)
         