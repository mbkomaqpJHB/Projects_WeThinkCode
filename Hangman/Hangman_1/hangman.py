#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    with open(file_name, 'r') as file:
        words = file.readlines()

    return (words)

  
def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    ri = random.randint(0, len(words) - 1)
    rw = words[ri]

    li = random.randint(0, len(rw) - 2)
    rl = rw[li]
    
    sword = "_"
    f_word = rw[:li] + sword + rw[li + 1:]
    print("Guess the word: " + f_word)
    return rw




def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    return input("Guess the missing letter: ")


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

