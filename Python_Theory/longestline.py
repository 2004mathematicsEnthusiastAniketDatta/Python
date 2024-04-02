with open('file3.txt','r') as f3:
    lines=f3.readlines()
    max_len=max(len(line) for line in lines)
    print([line for line in lines if len(line)==max_len])