def start_game():
    choice = raw_input("You wake up in a room with a door and a lamp. What do you do?")
    if choice == "open" or choice == "door":
        first_room()
    elif choice == "lamp":
        print "The lamp looks nice."
        start_game()
    else:
        start_game()
        
def first_room():
    choice = raw_input("You enter a room that has a tunnel leading left and a tunnel leading right. Which direction do you go?")
    if choice == "left":
        second_left()
    elif choice == "right":
        second_right()
    else:
        first_room()

def second_left():
    choice = raw_input("You enter a room that has three boxes in it. Which one do you open?")
    if choice == "1" or choice == "2" or choice == "3":
        box()
    else:
        second_left()

def second_right():
    choice = raw_input("You enter a room that has a painting and a door. What do you do?")
    if choice == "painting":
        inspect_painting()
    elif choice == "open" or choice == "door":
        second_left()
    else:
        second_right()

def inspect_painting():
    choice = raw_input("The painting isn't a painting at all: it's a door! Do you go through the door?")
    if choice == "yes":
        secret_door()
    elif choice == "no":
        second_right()
    else:
        inspect_painting()
    
def box():
    choice = raw_input("You hear a ticking noise. What do you do?")
    if choice == "look" or choice == "wait" or choice == "scream" or choice == "defuse":
        print "KABOOM! You died."
    elif choice == "run":
        kaboom()
    else:
      box()
        
def kaboom():
    choice = raw_input("The box explodes, destroying all three boxes and revealing a staircase. Do you walk down the staircase?")
    if choice == "yes":
        staircase()
    elif choice == "no":
        print "What are you waiting for? An acheivement? You go down the staircase anyway."
        staircase()

def secret_door():
    choice = raw_input("Behind the painting there is a tunnel with three paths. The second path has light eminating from it. Which path do you take?")
    if choice == "1":
        print "You fell to your death. You died."
    elif choice == "2":
        sunlight("!")
    elif choice == "3":
        print "You fall down a chute."
        staircase()
    else:
        secret_door()
        
def staircase():
    choice = raw_input("You see a chest and a door. What do you do?")
    if choice == "chest":
        treasure()
    elif choice == "door" or choice == "open":
        sunlight("!")

def treasure():
    choice = raw_input("The chest is full of gold! Do you bring it with you?")
    if choice == "yes":
        sunlight(" with lots of gold!")
    elif choice == "no":
        sunlight("!")
        
def sunlight(var):
    print "You climb out of the tunnel into sunlight. You escaped the dungeon" + var
    
start_game()
