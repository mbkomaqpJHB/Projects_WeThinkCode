import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    code_master = [0,0,0,0]
    for i in range(4):
        code = random.randint(1, 8)
        while code in code_master: 
            code = random.randint(1, 8)
        code_master[i] = code
        
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    
    turns = 12
    
    while turns > 0:
        user_input = input("Input 4 digit code: ")
        if len(user_input) != 4 and user_input is not int:
            print("Please enter exactly 4 digits.")
            #user_input = input("Input 4 digit code: ")
            continue
        
        #evaluate
        correct_place = 0
        not_correct = 0
        for i in range(len((user_input))):
            if int(user_input[i]) == code_master[i]:
                correct_place += 1
            elif int(user_input[i]) in code_master:
                not_correct += 1
        
        print("Number of correct digits in correct place:    ", correct_place)
        print("Number of correct digits not in correct place:", not_correct)
        if correct_place == 4:
            print("Congratulations! You are a codebreaker!")
            break
        else:
            turns -= 1
            print("Turns left:", turns)
        
    print("The code was: ", *code_master, sep = "")


if __name__ == "__main__":
    run_game()
