import shutil
with open('file1.txt','rb') as f1 , open('file2.txt','wb') as f2:
    shutil.copyfileobj(f1,f2)
    f1.close()
    f2.close()
