import os

# getcwd() --> will return the current working directory 
print(os.getcwd())
# C:\Users\Admin\Downloads\Python

# mkdir --> will make a new folder
# os.mkdir("C:/Users/Admin/Downloads/Python/demo")


# listdir --> will return the list of files inside the given path
print("---------------------")
print(os.listdir("C:/Users/Admin/Downloads/Python/demo"))

# os.path.exists(“path of a folder/file) --> will return True if the path/file exists or else return False
print("---------------------")
print(os.path.exists("C:/Users/Admin/Downloads/Python/demo/lol.png"))


# root, ext = os.path.splitext(“path of a folder/file) ---> will split the file into root name and extension

root, ext = os.path.splitext("C:/Users/Admin/Downloads/Python/demo/lol.png")

print("---------------------")
print(root)

print("---------------------")
print(ext)

# ---------------------------------------------------------------------

import shutil

# source = "C:/Users/Admin/Downloads/Python/demo/hello.txt"

# destination =  "C:/Users/Admin/Downloads/Python/demo/hello_copied.txt"

# shutil.copy(source, destination)

source = "C:/Users/Admin/Downloads/Python/demo/test.txt"

destination =  "C:/Users/Admin/Downloads/Python/demo/test_moved.txt"

shutil.move(source, destination)
