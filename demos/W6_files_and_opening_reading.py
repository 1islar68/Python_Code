import os

path = os.getcwd()
os.chdir('./staff/')
path = os.getcwd()
print(f"My path is {path}")

with open("data.txt", 'r') as file:
    for line_data in file:
        line_data = line_data.rstrip("\n")
        fname, lname, depart, loc = line_data.split(', ')
        print("==========================")
        print("Firstname: ", fname)
        print("Lastname: ", lname)
        print("Department: ", depart)
        print("Location: ", loc)
        print("==========================")

        #print(line_data.strip())

#path=path+"\\"+"students"
#os.chdir('./staff/')
#path = os.getcwd()
#print(path)
#os.chdir('../students/')
#path = os.getcwd()
#print(path)

#for file in os.listdir(path):
 #   print(file)
