"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'silent', 'reversed']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# history list
history = []

#for replay silent
silent = 0


def history_command(command):
    """
    calls global list
    appends list with user input
    returns appended list
    """

    global history
    history.append(command)
    return history


def replay_command(robot_name, command):
    """
    get list
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    return
    """
    
    global history

    count = 0
    for i in range(len(history)):
        command = history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1] #delete last updated record

    his_mov = " > {} replayed {} commands.".format(robot_name, count)
    return True, his_mov
    

def replay_silent(robot_name, command):
    """
    get list, get silent global variable
    set silent to 1
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    return
    """
    
    global history
    global silent

    silent = 1
    count = 0
    for i in range(len(history)):  
        command = history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]
    
    his_mov = " > {} replayed {} commands silently.".format(robot_name, count)
    return True, his_mov, 0


def replay_reversed(robot_name, command):
    """
    get list
    reverse list
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    reverse list to its original format
    return
    """

    global history

    reverse_history = history[::-1]
    count = 0
    for i in range(len(reverse_history)):
        command = reverse_history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]
        
    reverse_history = history[::-1]
    his_mov = " > {} replayed {} commands in reverse.".format(robot_name, count)
    return True, his_mov


def replay_reversed_silent(robot_name, command):
    """
    get list, get silent variable
    reverse list
    set silent to 1
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    reverse list to its original state 
    return
    """

    global history
    global silent

    reverse_history = history[::-1]
    silent = 1
    count = 0
    for i in range(len(reverse_history)):
        command = reverse_history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]
   
    reverse_history[::-1]
    his_mov = " > {} replayed {} commands in reverse silently.".format(robot_name, count)
    return True, his_mov, 0


def replay_reversed_num(robot_name, command, n):
    """
    get list
    reverse list and start count from the back [start:end:step]
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    return list to its original state
    return
    """

    global history

    reverse_history = history[-n::-1]
    count = 0
    for i in range(len(reverse_history)):
        command = reverse_history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]
   
    reverse_history[::-1]
    his_mov = " > {} replayed {} commands in reverse.".format(robot_name, count)
    return True, his_mov


def replay_num_silent(robot_name, command, n):
    """
    get list, get silent variable
    initialize silent to 1
    reverse list starting from the back going forward
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    return list to its original state
    return
    """

    global history
    global silent

    silent = 1
    reverse_history = history[-n::]
    count = 0
    for i in range(len(reverse_history)):
        command = reverse_history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]
   
    reverse_history[::-1]
    his_mov = " > {} replayed {} commands silently.".format(robot_name, count)
    return True, his_mov, 0


def limit_range(robot_name, command, n):
    """
    get list
    set range to start from the back going forward
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    return
    """

    global history
    range_history = history[-n::]
    
    count = 0
    for i in range(len(range_history)):
        command = range_history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]

    his_mov = " > {} replayed {} commands.".format(robot_name, count)
    return True, his_mov


def limit_range_silent(robot_name, command, n):
    """
    get list, get silent variable
    initialize silent to 1
    set range to start from the back
    set silent to 1
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    return
    """

    global history
    global silent

    silent = 1
    range_history = history[-n::]
    count = 0
    for i in range(len(range_history)):
        command = range_history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]

    his_mov = " > {} replayed {} commands silently.".format(robot_name, count)
    return True, his_mov, 0


def limit_range_nm(robot_name, command, n, m):
    """
    get list
    set range to start from n to m
    assign count to 0 for the number of commands repeated
    for each item in history that will be replayed
    call the handle command function
    add count after each item has been replayed
    delete last appended replayed command from history
    return
    """

    global history

    range_history = history[-n:-m:]
    count = 0
    for i in range(len(range_history)):
        command = range_history[i]
        handle_command(robot_name, command)
        count += 1
        del history[-1]

    his_mov = " > {} replayed {} commands.".format(robot_name, count)
    return True, his_mov


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name.upper()


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    splits arg1 into 2 parts
    find digit in command
    """

    (command_name, arg1) = split_command_input(command)
    com = arg1.split(' ')
    num1 = ''.join([i for i in arg1 if i.isdigit()]) 
    
    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1)) or (str(arg1).lower() == 'silent') or (str(arg1).lower() == 'reversed') or (str(arg1).lower() == 'reversed silent') or ('silent' in com) or num1 #(num[0]+'-'+num[1] in num)


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay previous commands
REPLAY SILENT - silently replay commands
REPLAY REVERSED - reverse replay commands
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    
    global silent
    global history

    (command_name, arg) = split_command_input(command)
    
    if command_name == 'off':
        history = []
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
        history_command(command)
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
        history_command(command)
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
        history_command(command)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
        history_command(command)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
        history_command(command)
    
    elif command_name == 'replay':
        arg1 = arg.split(' ')
        if arg == '':
            (do_next, command_output) = replay_command(robot_name, command)
        
        elif arg == 'silent':
            (do_next, command_output, silent) = replay_silent(robot_name, command)
            
        elif arg == 'reversed':
            (do_next, command_output) = replay_reversed(robot_name, command)
       
        elif arg == 'reversed silent':
            (do_next, command_output, silent) = replay_reversed_silent(robot_name, command)
        
        else:
            arg2 = arg.split('-')
            if len(arg1) == 2:
                if arg1[0].isdigit() and arg1[1] == 'reversed':
                    (do_next, command_output) = replay_reversed_num(robot_name, command, int(arg1[0]))
                
                elif arg1[0].isdigit() and arg1[1] == 'silent':
                    (do_next, command_output, silent) = replay_num_silent(robot_name, command, int(arg1[0]))
                
                else:
                    (do_next, command_output, silent) = limit_range_silent(robot_name, command, int(arg1[1]))
            
            elif len(arg2) == 2:
                (do_next, command_output) = limit_range_nm(robot_name, command, int(arg2[0]), int(arg2[1]))
            
            elif arg.isdigit():
                (do_next, command_output) = limit_range(robot_name, command, int(arg1[0]))
            
            else:
                output(robot_name, "Sorry, I did not understand '"+command+"'.")
                command_output = get_command(robot_name)
                return

    if silent == 0 or command_name is True:
        print(command_output)
        show_position(robot_name)
    else:
        pass
    
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
    
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
