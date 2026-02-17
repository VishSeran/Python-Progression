
lines = ["this\n", "is\n", "a list\n", "of items\n"]

with open("textWrite.txt", "w") as writefile:
    writefile.write("this is first line\n")
    writefile.write("This is second line\n")
    
    for line in lines:
        writefile.write(line)
        
with open("text.txt", "r") as readText:
    with open("textwrite.txt", "a") as writeText:
        for line in readText:
            writeText.write(line)
        