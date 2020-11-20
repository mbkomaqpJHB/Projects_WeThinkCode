


# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():  
    try:
        shapes = ["pyramid", "square", "triangle", "rectangle", "diamond", "oval"]
    
        while True:

            user_input = input(' Shape?:')
            if user_input.lower() in shapes:
                return user_input.lower()
            
    except AssertionError:
        print("it can't be blank and must be a valid shape!)")
        return get_shape()

# TODO: Step 1 - get height (it must be int!)
def get_height(): 
    try:
        height = int(input(' Height?:')) 
        if height > 80:
            print("Must be below 80") 
            get_height()
        elif height <= 0:
            print("Must be positive")
            get_height()
        
        return height
    except ValueError:
        height = int(input(' Height?:'))
    
    return height

# TODO: Step 2
def draw_pyramid(height, outline): 
    if outline is False: 
        k = 0
        for i in range(1, height + 1):
            for gap in range(1, (height - i) + 1):
                print(end=" ")
            
            while k != 2*i - 1:
                print("*", end="")
                k += 1
            k = 0
            print("")
            
    else: 

        for i in range(1, height + 1): 
            for j in range(1, 2*height):

                if i == height or i+j == height+1 or j-i==height-1: 
                    print("*", end="") 
                else: 
                    print("", end=" ") 
            print()

# TODO: Step 3
def draw_square(height, outline): 
    if outline is False: 
        for i in range(0, height): 
            for j in range(0, height): 
                print("*", end = "") 
        
            print("")

    else: 
        mid = height - 2 
        print("*"*height) 
        for s in range(mid): 
            print("*" + " "*mid + "*") 
        print("*"*height)

# TODO: Step 4
def draw_triangle(height, outline): 
    if outline is False:
        for i in range(0, height): 
            for j in range(0 , i + 1): 
                print("*", end = "") 
            
            print("")
    else: 
        for i in range(0, height - 1): 
            for j in range(0, i + 1): 
                if j == 0 or j == i or j == height - 1: 
                    print("*", end = "") 
                else: 
                    print(" ", end = "") 
            
            print("")
        
        for j in range(0, height): 
            print("*", end = "") 
        print("")


def draw_rectangle(height, outline): 
    if outline is False: 
        for i in range(0, height): 
            for j in range(0, (height+height)*2): 
                print("*" , end = "") 
            
            print("")
    else: 
        mid = ((height+height)*2) - 2 
        
        print("*"*((height+height)*2)) 
        
        for i in range(0, height - 2): 
            print("*" , " "*(mid - 2), "*") 
            
        print("*"*((height+height)*2), end = "") 
        print("") 
        

def draw_diamond(height, outline): 
    if outline is False: 
        for i in range(height): 
            print(" "*(height-i), "*"*(i*2+1)) 
            
        for i in range(height-2, -1, -1): 
            print(" "*(height - i), "*"*(i*2+1)) 
            
    else: 
        for i in range(height): 
            print(" "*(height-i), "*", end="") 
            
            if i >= 1: 
                print(" "*(2*i - 1) + "*", end ="") 
            print("")

        for i in range(height-2, -1, -1): 
            print(" "*(height - i) , "*", end = "")

            if i >= 1: 
                print(" "*(2*i-2) , "*", end = "") 
            print("")


def draw_oval(height, outline): 
    if outline is False: 
        just = (height - 2) 
        for i in range(0, height): 
            for j in range(0, just): 
                if((j == 0 or j == just - 1) and (i != 0 and i!= height - 1)): 
                    print("*", end = "") 
                elif ((i == 0 or i == height - 1) and (j > 0 and j< just - 1)): 
                    print("*", end= "") 
                elif ((i >= 1 and i < height - 1) and (j >= 1 and j < just)):
                    print("*", end= "")
                else: 
                    print(end= " ") 
            
            print("") 
    
    else:
        just = (height - 2) 
        for i in range(0, height): 
            for j in range(0, just): 
                if((j == 0 or j == just - 1) and (i != 0 and i!= height - 1)): 
                    print("*", end = "") 
                elif ((i == 0 or i == height-1) and (j > 0 and j< just-1)): 
                    print("*", end= "") 
                else: 
                    print(end= " ") 
            
            print("") 


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline): 
    if shape == "pyramid": 
        draw_pyramid(height, outline) 
    elif shape == "square": 
        draw_square(height, outline) 
    elif shape =="triangle": 
        draw_triangle(height, outline) 
    elif shape == "rectangle": 
        draw_rectangle(height, outline) 
    elif shape == "diamond": 
        draw_diamond(height, outline) 
    else: draw_oval(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline(): 
    outline_input = input("Outline only? (y/n) :") 
    if outline_input.lower() == "n" or outline_input.lower() == "":
        return False
    else:
        return True



if __name__ == "__main__": 
    shape_param = get_shape() 
    height_param = get_height() 
    outline_param = get_outline() 
    draw(shape_param, height_param, outline_param)

