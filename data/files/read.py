def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}.\n", end="")
    print("...Done!")

def run():
    search("C:/Users/Admin/Desktop/Python Rafue/Python_Code/data/files/locations.txt")

run()