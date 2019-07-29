import random

print('Welcome!!!')
print('This is the Hangman game')

with open('words.txt') as f:
    text = f.read().splitlines()

lives = 0 # setting the lives to deafult 0
count = 0 # setting the counter to 0


'''user selects the difficulty'''
while True:
    try:
        user_input = input('Please enter your difficulty, choose between easy, medium or hard')

        if user_input == 'easy'.lower():
            lives = 10
            print('You play on easy level and have', lives, 'lives')
            break
        elif user_input == 'medium'.lower():
            lives = 7
            print('You play on medium level and have', lives, 'lives')
            break
        elif user_input == 'hard'.lower():
            lives = 5
            print('You play on hard level and have', lives, 'lives')
            break
    except ValueError:
        print('Please enter a proper answer')

'''generating the random number adn choosing the secret word according to it'''
number = random.randint(0, len(text) - 1)
chosen = text[number]

'''displayed and used letters'''
display =[]
display.extend(chosen)
used_letters = []
used_letters.extend(display)

for i in range(len(display)):
    display[i] = '-'
print(display)

while lives > 0:
    '''asking for user letter input '''
    letter = input('Please enter a letter to guess the word')
    letter = letter.lower()
    print('you have', lives, 'chances')
    for i in range(len(chosen)):
        '''if the player guessed the letter, printing the letter and removing it from the used letter list, 
        so the program does not reduce the player's life, if the player enters it again'''
        if chosen[i] == letter and letter in used_letters:
            display[i] = letter
            print(chosen[i])
            print('You guessed the letter')
            used_letters.remove(letter)
            count += 1
    if letter not in display:
        '''if the player did not guess the letter, life is deducted by 1'''
        lives = lives - 1

    print('You have', lives, ' more chances')
    print(' '.join(display))
    if count == len(chosen):
        '''if the secret word is guessed, it prints out a message to the user'''
        print('Congratulations, you are the best')
        break
    else:
        print('Sorry, you are busted')
print('The secret word was', chosen)

