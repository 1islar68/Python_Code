def search(file_path):
    print("Searching...", end="")
    sections = []
    books = []
    with open("book.txt") as file:
        for line in file:
            if line.startswith("Section"):
                section_name = line.split(":")[1]
                sections.append(section_name.strip())
            else:
                books.append(line.strip())
    print("Done!")
    return (sections, books)

def save(file_path, data):
    print("Saving...", end="")
    with open(file_path, "w") as file:
        file.write(f"Section: {data[0]}\n")
        file.write(f"Book: {data[1]}\n")
    print("Done!")

def run():
    data = search("C:/Users/Admin/Desktop/Python Rafue/Python_Code/data/files/book.txt")
    save("C:/Users/Admin/Desktop/Python Rafue/Python_Code/data/files/book.txt", data)

run()