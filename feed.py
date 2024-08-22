import os
file_path = "new_file2.txt"
with open(file_path, "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a new file.")