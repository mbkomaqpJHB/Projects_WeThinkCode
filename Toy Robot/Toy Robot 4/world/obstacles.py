
import turtle
import random

square_list = []

#sqaure
def obstacle_text():
    '''
    create square
    randomly place created squares
    append position to list
    '''

    global square_list
    square_list = []

    random_sqares = range(random.randint(1, 10))
    
    for i in random_sqares:
        x = random.randint(-100,100)
        y = random.randint(-200,200)

        square_list.append((x, y))


def obstacle():
    '''
    create square
    randomly place created squares
    append position to list
    '''

    global square_list
    sqre = turtle.Turtle()
    sqre.hideturtle()
    sqre.pensize(5)
    sqre.speed(0)
    
    random_sqares = range(random.randint(1, 10))
    
    for i in random_sqares:
        x = random.randint(-100,100)
        y = random.randint(-200,200)
        sqre.penup()
        sqre.goto(x,y)
        sqre.pendown()
        
        for side in range(4):
            sqre.fd(4)
            sqre.lt(90)
        
        square_list.append((x, y))
       

def is_position_blocked(x, y):
    '''
    check if future position has obstacle
    '''
    global square_list
    
    for pos in square_list:
        if x in range(pos[0], pos[0]+4) and y in range(pos[1], pos[1]+4):
                return True

    return False


def is_path_blocked(x1, y1, x2, y2):
    '''
    checks whether there's no obstacles in future path
    '''
    
    while x1 == x2 and y1 <= y2:
        if is_position_blocked(x1, y1):
            return True
        y1 += 1
    while y1 == y2 and x1 <= x2:
        if is_position_blocked(x1, y1):
            return True
        x1 += 1
    while x1 == x2 and y1 >= y2:
        if is_position_blocked(x1, y1):
            return True
        y1 -= 1
    while y1 == y2 and x1 >= x2:
        if is_position_blocked(x1, y1):
            return True
        x1 -= 1
    return False


def get_obstacle_position():
    '''
    print obstacles positions
    '''
    
    global square_list
    
    if len(square_list) != 0:
        print("There are some obstacles:")
        for i in square_list:
            print("- At position {},{} (to {},{})".format(i[0],i[1],i[0]+4,i[1]+4))

