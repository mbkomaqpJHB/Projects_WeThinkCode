import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    letter_index = random.randint(0, len(word) - 1)
    random_letter = word[letter_index]
    secret_word = '_'*len(word)
    new_word = secret_word[:letter_index] + word[letter_index] + secret_word[letter_index + 1:]
    return new_word


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    # for i in range(len(original_word)):
    #     if char in answer_word[i]:
    #         #print(char, end = "")
    #         return True
    #     else:
    #         return False

    i = 0
    for letter in original_word:
        if letter == char and answer_word[i] == "_":
            return True
        i += 1

    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):

    n_word = list(answer_word)
    i = 0
    for letter in original_word:
        if char in letter and answer_word[i] in "_":
            n_word[i] = char
        i += 1
    new_word = "".join(n_word)
    return new_word


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/----\n|\n|\n|\n|\n_______")
    
    elif number_guesses == 3:
        print("/----\n|   0\n|\n|\n| ")

    elif number_guesses == 2:
        print("/----\n|   0\n|   |\n|   |\n|  ")
    
    elif number_guesses == 1:
        print("/----\n|   0\n|  /|\\\n|   |\n| ")
   
    else:
        print("/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______")
    
    print()

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    
    print("Guess the word: "+answer)
    guesses = 4

    while answer != word:
        guess = get_user_input()
        if guess.lower() == "quit" or guess.lower() == "exit":
            print("Bye!")
            break
        elif is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            do_wrong_answer(answer, guesses)
            guesses -= 1
        
        if guesses < 0:
            print("Sorry, you are out of guesses. The word was:",word)
            break


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    run_game_loop(selected_word, current_answer)

