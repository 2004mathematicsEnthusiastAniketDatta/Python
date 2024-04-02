def multiplelinewrite():
    with open('MYFILE.txt', 'w') as file:
        line=input("Enter a line:")
        while True:
           file.write(line)
           more_line=input("Do you want to enter more line(y/n):").lower()
           if more_line=='y':
               line=input("\n Enter a line:")   
           elif more_line=='n':
               break
        file.close()
multiplelinewrite()