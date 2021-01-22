
def robot_name():
    '''
    get robot name from user
    return input to upper
    '''

    robot = input("What do you want to name your robot? ")
    print(robot.upper() + ": Hello kiddo!")
    return robot.upper()


def direction_input(robot):
    '''
    get user commands
    seperate letters and numbers
    return outputs
    '''

    user_command = input(robot.upper() + ": What must I do next? ")
    word_input = "".join(i for i in user_command if not i.isnumeric()) #takes only the word in an input
    num = ''.join([i for i in user_command if i.isdigit()]) #takes only the number in an input 
    
    return word_input.lower(), num, user_command


def off_help_command(robot, word_input):
    '''
    display off and help command
    '''

    off = robot + ": Shutting down.."
    hlp = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move me forward
BACK - move me back
RIGHT - turn right
LEFT - turn left
SPRINT - make a player sprint"""
        
    if word_input.strip() == "off": 
        print(off)
        return (off) 
    else:
        print(hlp)
        return hlp


def update_position(robot, x, y):
    '''
    show robot position
    '''

    update = " > " + robot + " now at position ({},{}).".format(x,y)
    print(update)
    return update


def forward_command(robot, num, x, y, degree):  
    '''
    move robot forward depending on the direction its facing
    '''

    x_max = x+int(num)
    y_max = y+int(num)
    
    if x_max in range(-101, 101) and y_max in range(-101, 201):
        if degree == 90 or degree == -270: 
            x += int(num)
          
        elif degree == 180 or degree == -180:   
            y -= int(num)
        
        elif degree == 270 or degree == -90:    
            x -= int(num)
            
        else:
            y += int(num)
        print(" > " + robot + " moved forward by " + num + " steps.")
    else:
        print(robot + ": Sorry, I cannot go outside my safe zone.")

    update_position(robot, x, y)
    robot_commands(robot, x, y, degree)
    return " > " + robot + " moved forward by " + num + " steps."


def back_command(robot, num, x, y, degree):
    '''
    move robot forward depending on the direction its facing
    '''

    x_max = x+int(num)
    y_max = y+int(num)
    
    if x_max in range(-101, 101) and y_max in range(-201, 201):
        if degree == -90 or degree == 270:
            x += int(num)
        
        elif degree == -180 or degree == 180:
            y += int(num)
       
        elif degree == -270 or degree == 90:
            x -= int(num)
        
        else: 
            y -= int(num)
        print(" > " + robot + " moved back by " + num + " steps.")
    else:
        print(robot + ": Sorry, I cannot go outside my safe zone.")

    update_position(robot, x, y)
    robot_commands(robot, x, y, degree)
    return " > " + robot + " moved back by " + num + " steps."


def right_command(robot, x, y, degree):
    '''
    turn robot right
    '''

    degree += 90
    print(" > " + robot.upper() + " turned right.")
    update_position(robot, x, y)
    robot_commands(robot, x, y, degree)
    return " > " + robot + " turned right."


def left_command(robot, x, y, degree):
    '''
    turn robot left
    '''

    degree -= 90
    print(" > " + robot.upper() + " turned left.")
    update_position(robot, x, y) 
    robot_commands(robot, x, y, degree)       
    return " > " + robot + " turned left."


def sprint_command(robot, num, x, y, degree):
    '''
    move robot forward n times
    update position
    '''

    for i in range(int(num)):
        last_v = int(num)
        last_v -= i
        print(" > " + robot.upper() + " moved forward by {} steps.".format(last_v))
        y += last_v

    update_position(robot, x, y)
    robot_commands(robot, x, y, degree)
    return " > " + robot + " now at position ({},{}).".format(x,y)


def robot_commands(robot, x, y, degree):
    '''
    handles user commands
    '''

    word_input, num, user_command = direction_input(robot)
    
    if word_input.strip() == "forward":
        return forward_command(robot, num, x, y, degree)
    
    elif word_input.strip() == "back":
        return back_command(robot, num, x, y, degree)

    elif word_input.strip() == "off":
        return off_help_command(robot, word_input)
        
    elif word_input.strip() == "help":
        off_help_command(robot, word_input)      
    
    elif word_input.strip() == "right":
        return right_command(robot, x, y, degree)
        
    elif word_input.strip() == "left": 
        return left_command(robot, x, y, degree)
    
    elif word_input.lower().strip() == "sprint":
        return sprint_command(robot, num, x, y, degree)
    
    else:
        print(robot+": Sorry, I did not understand '"+user_command+"'.")

    return robot_commands(robot, x, y, degree)
        
            
def robot_start():
    """This is the entry function, do not change"""
    x = 0
    y = 0
    degree = 0
    robot = robot_name()
    robot_commands(robot, x, y, degree)
    
    
if __name__ == "__main__":
    robot_start()
