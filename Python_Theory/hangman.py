import random
word_list=[]
N=int(input("Enter the number of lower letter words you need"))
for i in range(N):
    ele=(input("Enter element:"))
    word_list.append(ele)
print(word_list)
lives=5
chosen_word=random.choice(word_list)
# print(f"The chosen word is {chosen_word}") 
display=[]
for letter in chosen_word:
    display+='_'
print(display)
game_over=False
while(not game_over):
    guessed_letter=input("Guess a letter:").lower()
    for  position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if(guessed_letter not in chosen_word):
        lives=lives-1
        if(lives==0):
            game_over=True
            print("Try again Next time")
    if'_' not in display:
        game_over=True
        print('Congratulations you won')
        
