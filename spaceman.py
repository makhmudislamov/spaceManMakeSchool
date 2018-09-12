import random
import sys

sea_names = ['Adriatic', 'Caspian', 'Tyrrhenian', 'Amundsen']
cartoon_chars = ['Betty Boop', 'Elmer Fudd', 'Foghorn Leghorn', 'Tasmanian Devil']
wrong_etters = []
correct_letters = []
space = " _ "
word = [random.choice(sea_names), random.choice(cartoon_chars)]


# getting user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input


def select_theme(function_code):

    # print('Enter 1 seaNames or 2 cartoonChars')
    if function_code == '1':
        print ('sea name')
        print(space * len(random.choice(sea_names)))
        return word

    elif function_code == '2':
        print('Cartoon')
        print(space * len(random.choice(cartoon_chars)))
        return word

    elif function_code == '3':
        print('bye')
        return False

    else:
        print('Uknown option')
        return True
        


def check_letter(letter):
    letter = user_input('Enter Letter: ')
    for letter in word:
        print("working")
    else:
        print('not working')


running = True
while running:
    selection = user_input('Enter 1 seaNames or 2 cartoonChars ')
    running = select_theme(selection)



    


# array that holds sea names - done
# array that holds cartoon characters' names - done
# array wrongLetters - done
# array correctLetters - done
# function that randomly pulls out a word from themed array and prints as _ _ _ _ _ _  - done
# function that checks if the guessed letter exists in the word
# function for adding wrong guessed letters to array wrongLetters and prints the whole array
# function for adding correct guessed letters to array correctLetters and replaces "_" with the letter
# function that counts trials and prints out


# word = "cat"
# guess = input("Make a guess: ")


# print(space * len(word))
# found = list()
# wrong = []


# def checkLetter():
#     if guess in word:
#         found.append(guess)
#     else:
#         print("nothin")


# print(found)


# checkLetter()
