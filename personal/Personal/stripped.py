filename = 'text.txt'
filedata = ""

with open(filename, "r") as infile:
    for line in infile.readlines():
        if line != "\n":
            filedata += line

with open(filename, "w") as outfile:
    outfile.write(filedata)