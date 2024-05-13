import os
import sys
import shutil

def iterFile(name):
    with open(name) as f:
        seen = set()
        count = 0
        for line in f:
            count += 1
            line_lower = line.lower()
            if line_lower in seen and line_lower.strip() != "":
                print("File:", os.fsdecode(os.path.basename(name)), " -> ", str(count) + ": ", line)
            else:
                seen.add(line_lower)

def iterDir(directory):
    if (os.listdir(directory)):
        print("/" + os.fsdecode(os.path.basename(directory)))
        print()

    for file in os.listdir(directory):
        filename = os.path.join(directory, file)
        if (os.path.isfile(filename) and os.fsdecode(os.path.basename(filename)) != "gh-codetwin"):
            ext = os.path.splitext(os.fsdecode(os.path.basename(filename)))[1]
            if (ext == ".py" or ext == ".c" or ext == ".cpp" or ext == ".java"):
                iterFile(filename)
        elif (os.path.isdir(filename) and os.fsdecode(os.path.basename(filename))[0] != "."):
            iterDir(filename)

print("Start:\n")
#directory = os.fsencode(os.getcwd())
directory = os.fsencode(sys.argv[1])
iterDir(directory)
#print(directory)

path = os.path.join(sys.argv[1], ".github")
if(not os.path.exists(path)):
    os.mkdir(path)

path = os.path.join(sys.argv[1] + "/.github", "workflows")
if(not os.path.exists(path)):
    os.mkdir(path)

shutil.copyfile('.github/workflows/learn-github-actions.yml', sys.argv[1] + "/.github/workflows/codetwin-github-actions.yml")

shutil.copyfile('codetwin.py', sys.argv[1] + "/codetwin.py")
