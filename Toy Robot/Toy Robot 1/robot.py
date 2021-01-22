

# TODO: Decompose into functions
def move_square():
    size = 10 #changed from size 10 to 20 because output has a size of 20
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def dancing_square():
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20") 
        for j in range(4):
            size = 20 #never defined
            degrees = 90 #was called before it was defined
            print("* Move Forward " + str(size))
            print("* Turn Right " + str(degrees) + " degrees")
            

def crop_circles():
    print("Crop circles - 4 circles")
    length = 20 #was never defincd
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()


def move():
    move_square()
    move_rectangle()
    move_circle()
    dancing_square()
    crop_circles()


def robot_start():
    #move_shapes() because it deals with moving the shapes 
    move() 


if __name__ == "__main__":
    robot_start()
