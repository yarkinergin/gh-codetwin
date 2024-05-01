import os

def iterFile(name):
    with open(name) as f:
        seen = set()
        count = 0
        for line in f:
            count += 1
            line_lower = line.lower()
            if line_lower in seen and line_lower.strip() != "":
                print("File:", name, " -> ", str(count) + ": ", line)
            else:
                seen.add(line_lower)

def iterDir(directory):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if (os.path.isfile(filename) and filename != "gh-codetwin"):
            iterFile(filename)
        elif (os.path.isdir(filename) and filename[0] != "."):
            print(filename)
            iterDir(filename)

print("Start:")
directory = os.fsencode(os.getcwd())
print(directory)
iterDir(directory)
    
