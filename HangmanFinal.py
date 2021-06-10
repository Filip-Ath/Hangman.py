import random

words_list = ['mindless', 'inexpensive', 'stupendous', 'wriggle', 'shivering', 'righteous', 'redundant', 'plausible',
              'psychedelic', 'amusement', 'appliance', 'beginner', 'brick', 'concerned', 'abyss', 'matrix', 'bikini']
# A word list

chosen_word = random.choice(words_list)
# Picks a random word from word_list

name = input("Enter your name : ")
# User enters his/her name


print("Welcome", name, "!\n", "Let's play Hangman !", "Find the word in 8 turns", "\n",
      "The word has  *", len(chosen_word), "*  letters")
# Prints welcome message ,name of the user , length of random word

letters = []
# An empty list ,where user's typed letters are stored
wrong_letters = []
# An empty list ,where wrong picks-letters are stored ,later printed

turns = 8
# Tried/lives user's


def correct_n_dashes():
    hidden = ""
    for char in chosen_word:
        if char in letters:
            hidden += char
        else:
            hidden += "_"
    return hidden
# For every letter in chosen_word ,this function stores/index a corresponding letter ,otherwise generates a dash "_"


while turns > 0:
    print("....................................\n")
    hidden_word = correct_n_dashes()
    if hidden_word == chosen_word:
        print("Congrats ! You are a Champ !")
        exit()
    print(hidden_word)
    chose_letter = input("Please, chose a letter ")
    if chose_letter in letters:
        print("already used")

    letters.append(chose_letter)
    if chose_letter in chosen_word:
        print("Correct ! ")
    else:
        wrong_letters.append(chose_letter)
        print("Please,chose another letter.", "Already used letters", wrong_letters)
        turns -= 1
        print("Remaining lives : ", turns)
    if turns == 0:
        print("You lost, try again.The word was:", chosen_word)

# Loops for 8 turns  , when user finds the correct word loop exits and users wins
# Otherwise
# a) chosen letter is typed twice , user gets a message "already used"
# b) If letter is correct , user gets a message "Correct"
# c) Else , the wrong letter is stored in the wrong_letter list ,user gets message to try another letter and prints
# wrong_letters list  , remaining turns/lives to beat the game
