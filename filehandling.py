file = open("file/hello.txt","r")
content = file.read()
print(content)
file.close()

file = open("file/write.txt",mode="w")
file.write("Hello World\n")
file.close()

file = open("file/write.txt",mode="w+")
file.write("Welcome to write mode from 0 position\n")
file.seek(0)
print(file.read())
file.close()
try:
    file = open("file/doesnotexist.txt","r")
    content = file.read()
    print(content)
    content2 = file.write("Trying to write in read mode")
except FileNotFoundError:
    print("File does not exist")
    file2 = open("file/doesnotexist.txt","w")
    file2.write(file.read())
