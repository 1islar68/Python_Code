def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    move = directions()
    for i in range(len(move)):
        print("{}:{}".format(i, move[i]))

def run():
    menu()

run()