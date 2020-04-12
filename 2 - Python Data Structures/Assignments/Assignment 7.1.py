##
# Write a program that prompts for a file name, then opens that file and reads
# through the file, and print the contents of the file in uppercase. Use the
# file words.txt to produce the output below.
##

fileName = input('Enter file name: ')
try:
    newFile = open(fileName)
except:
    print('Error, file does not exist')

for line in newFile:
    print(line.rstrip().upper())
