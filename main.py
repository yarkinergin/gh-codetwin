import os

def iterFile(name):
    with open(name) as f:
        seen = set()
        for line in f:
            line_lower = line.lower()
            if line_lower in seen and line_lower.strip() != "":
                print("*******" ,name , line)
            else:
                seen.add(line_lower)

def iterDir(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        if (os.path.isfile(filename)):
            iterFile(filename)
        elif (os.path.isdir(filename) and filename[0] != "."):
            iterDir(filename)

print("sasda")
directory = os.fsencode(os.getcwd())
print(directory)
iterDir(directory)
    
