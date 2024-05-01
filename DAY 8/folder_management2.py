import os

# remove file with entire data

if os.path.exists("code.txt"):
    os.remove("code.txt")
    print("File deleted successfully !")

else:
    print("File does not exist !")

