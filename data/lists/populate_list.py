def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    move = directions()
    for i in range(len(move)):
        print("{}:{}".format(i,move[i]))
    index = int(input())
    return move[index]

def run():
    route = []
    print("Working out escape route...")
    for i in range(5):
        route.append(menu())
    print(f"Escape route: {route}")

run()

