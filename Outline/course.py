import random


def create_outline():
    """
    TODO: implement your code here
    """
   
    course_topics = ["Introduction to Python", 
                "Tools of the Trade", 
                "How to make decisions", 
                "How to repeat code", 
                "How to structure data", 
                "Functions", 
                "Modules"] 
                
    print("Course Topics:") 
    
    for i in range(len(course_topics)): 
        course_topics[i] = "* " + course_topics[i] 
    
    for i in sorted(set(course_topics)): 
        print(i)

    
    pro = 0
    print("Problems:") 
    problems = ["Problem 1, ", "Problem 2, ", "Problem 3, "] 
    
    for i in sorted(course_topics): 
        print("{} : {}{}{}".format(i, problems[0], problems[1], problems[2])) 
    
  
    print("Student Progress:") 
    
    Stu_name = ("Mbali", "Zanele", "Tiny", "Nyari", "Adam") 
    Nr = (1,2,3,4,5)
    Status = ("[STARTED]", "[GRADED]", "[COMPLETED]")
    Problem = ("Problem 1 ", "Problem 2 ", "Problem 3 ") 

    topics = ("Introduction to Python", 
                "Tools of the Trade", 
                "How to make decisions", 
                "How to repeat code", 
                "How to structure data", 
                "Functions", 
                "Modules")
    

    Stu_pro = (Nr, Stu_name, topics, Problem, Status) 
    
    for i in range(len(Stu_pro)):
        if i < 2:
            print("{}. {} - {} - {} - {}".format(Nr[i], Stu_name[i], random.choice(topics), random.choice(Problem), (Status[0])))
        elif i < 4:
            print("{}. {} - {} - {} - {}".format(Nr[i], Stu_name[i], random.choice(topics), random.choice(Problem), (Status[1])))
        else:
            print("{}. {} - {} - {} - {}".format(Nr[i], Stu_name[i], random.choice(topics), random.choice(Problem), (Status[2])))
    


if __name__ == "__main__":
    create_outline()
