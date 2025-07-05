# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is a sample file.\nPython is fun!")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
