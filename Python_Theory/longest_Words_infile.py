with open('file1.txt','r') as f1:
    words=f1.read().split()
    max_len=max(len(wd) for wd in words)
    print([wd for wd in words if len(wd)==max_len])