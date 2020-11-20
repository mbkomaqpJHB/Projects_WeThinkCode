import random


# TODO: Decompose into functions
def run_game():
    correct = False
    turns = 0
    code = generate_code()

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
     
    while not correct and turns < 12: #create a loop for the following functions
        answer = user_input(correct, turns)
        turns += 1
        validate_digit_position(answer, code, correct, turns)
        if correct_digits_and_position == 4: #after validation, break the loop if correct_digits_and_position == 4
            break

    print('The code was: '+str(code)) #display code


def generate_code(): #generate random code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8) # 8 possible digits
        code[i] = value
    return code #return generated code


def user_input(correct, turns):
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4 :
            print("Please enter exactly 4 digits.")
            continue
        else:
            return answer


def validate_digit_position(answer, code, correct, turns):
    global correct_digits_and_position
    global correct_digits_only
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
        
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))


if __name__ == "__main__":
    run_game()
