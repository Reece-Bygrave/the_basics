import random, time

#list of words to be used during the game
winning_words = ['computer', 'programming','elephant','sunshine','butterfly','chocolate','adventure','guitar','kangaroo','telescope','zebra','dragonfly','fireworks','rainbow','ocean']
#number of attempts that will be used by the user if == 0 then game will end
attempts = 5



print("#### Hangman ####\n")
time.sleep(1)

#a loop to ask the user if they want to play the game
while True:
    want_to_play = input("Want to play? Y/N\n")

    if want_to_play == "y" or want_to_play == "Y":
        print("Let the game begin!!\n")
        break

    elif want_to_play == "n" or want_to_play == "N":
        print("No problem, bye now!")
        quit()

    else:
        print("Input not recognised, please Enter y or n")

#loop to ask the user if they know the rules
while True:
    know_the_rules = input("Do you know the rules of hangman?\n")
    if know_the_rules == "Y" or know_the_rules == "y":
        print("Great! Lets get started.\n")
        break
        
    elif know_the_rules == "N" or know_the_rules == "n":
        print("Here is how the rules work\n")
        print("1. You have",attempts,"attempts to guess the word correctly\n")
        print("2. You will guess 1 letter at a time and when a correct letter is guessed it will appear in the space of the word where that letter should reside\n")
        print("3. If all attempts are used, then the game will finish\n")
        print("Now you know the rules, lets get started!\n")
        break

    else:
        print("Input not recognised, please enter y or n\n")    


#generate a random index
random_index = random.randint(0, len(winning_words) -1) # 'len(winning_words) -1)' is the last index of the list. -1 is becasue lists are indexed from 0. this gives the highest vaild index in the list

#store random word from list into a var
random_word_in_list = winning_words[random_index]

#creating a var that will store the len of the random word
length_of_random_word = len(random_word_in_list)


while True:
    print(random_word_in_list)
    print("There are",length_of_random_word,"letters in the winning word\n")
    
    if attempts != 1:
        print("You have",attempts,"attempts\n")
    elif attempts == 1:
        print("Watch out! you only have.",attempts,"left")

    letter_in_word = input("Guess a letter\n")

    if letter_in_word in random_word_in_list:
        print(f"The letter '{letter_in_word}' is within the winning word\n")
    else:
        print(f"The letter '{letter_in_word}' is not in the winning word\n")
        attempts += -1
        

    if attempts == 0:
        print("GAMEEEEEE OVER")
        break
        













