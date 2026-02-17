##dierct read from a file but we need to close the file object 
""" fileSeran = open("text.txt","r")
fileSeran.name
fileSeran.mode 

fileStuff = fileSeran.read()
print(fileStuff)

fileSeran.close() """

## using with method it is automatically close the file object
##with open("text.txt","r") as file1:
    ##fileDetails = file1.read()
    ##fileLines = file1.readlines()
    ##print(fileDetails)
    ##print(fileLines)
    
    ##fileLine = file1.readline()
    ##print(fileLine)
    
   ## fileLine = file1.readline()
    ##print(fileLine)
    ##fileLine = file1.readline()
   ## print(fileLine) """
    
with open("text.txt","r") as file1:
    line1 = file1.readline()
    line2 = file1.readline()
    line3 = file1.readline()
    
    print(line1)
    if "important" in line2:
        print(line2)
    else:
        print('nothing')
        
    if "important" in line3:
        print(line3)
    else:
        print("nothing")
        
    file1.seek(4) # Move to the 11th byte (0-based index)
    characters = file1.read(3) # Read the next 5 characters
    print(characters)


