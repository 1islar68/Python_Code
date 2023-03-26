def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    move = movements()
    print(f"{move[0]} for {move[1]} steps")
    print(f"{move[2]} for {move[3]} steps")
    print(f"{move[4]} for {move[5]} steps")
    print(f"{move[6]} for {move[7]} steps")

run()

