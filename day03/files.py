# We Can read and write from and into files 
# our_file = 'newfile.txt'

# file = open(our_file, 'a')
# file.write('\nThis text for test2')

# file.close()
# file = open(our_file, 'r')
# print(file.read())
# file1 = open(our_file, 'r')
# file1.read()
with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content!")

# open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read())
    f.seek(5)
    print(f.read())
    
    
# f = open("demofile.txt", "r")
# print(f.seek(1))