import os

# remove data/text from file without deleting the file

file=open("demo.txt","r+")
file.seek(0)
file.truncate()