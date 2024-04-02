import filecmp
f1=r'C:\Users\ANIKET\OneDrive\Desktop\Python_Theory\file1.txt'
f2=r'C:\Users\ANIKET\OneDrive\Desktop\Python_Theory\file2.txt'
result=filecmp.cmp(f1,f2,shallow=False)
print(result)
