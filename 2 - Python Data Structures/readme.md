# Chapter 6 - Strings
## 6.1 What is String
  - String is a sequence of characters
  - + means 'concatenate'
  - int(stringValue) to change to a number
## 6.2 Getting the length of a string using len

``` python
length = len(fruit)
first = fruit[0]
last = fruit[length - 1]
```

## 6.3 Traversal through a string with a loop

``` python
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1
```

## 6.4 String Slices

``` python
s = 'Test String'
test = s[0:4]
print test ## Prints 'Test'
```

## 6.5 Strings are immutable
  - You cannot access and change a character in a string.
    ex:
    ``` python
    greeting = 'hello world'
    letter = greeting[0]
    letter = 'J'
    TypeError: 'str' object does not support item assignment
    ```
      - Workaround:
        - You must concatenate the character with the rest of the string.
        ex:
        ```python
        greeting = 'hello world'
        letter = 'J'
        greeting = 'J' + greeting[1:]
        print(greeting)
        ```
        Output: Jello world
## 6.6 Looping and counting
  - You can loop through each letter in a word if needed.
    ex for letter in word:
## 6.7 in Operator
  - in is a boolean operator that takes two string. Returns True if the first string appears in the second string.
  ex:
    ```bash
    >>> 'a' in 'banana'
    True
    >>> 'c' in 'kangaroo'
    False
    ```
## 6.8 String comparison
  - word == string
  - word >/< string ## Indicates alphabetical order

## 6.9 String methods
  - String is a Python object. As a result, Strings do have methods that you can call upon.
  ```python
  >>> stuff = 'hello world'
  >>> dir(stuff)
  ['capitalize', 'casefold', 'center', 'count', 'encode',
  'endswith' , 'expandtabs', 'find', 'format', 'format_map',
  'index' , 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
  'isidentifier' , 'islower', 'isnumeric', 'isprintable',
  'isspace' , 'istitle', 'isupper', 'join', 'ljust', 'lower',
  'lstrip' , 'maketrans', 'partition', 'replace', 'rfind',
  'rindex' , 'rjust', 'rpartition', 'rsplit', 'rstrip',
  'split' , 'splitlines', 'startswith', 'strip', 'swapcase',
  'title' , 'translate', 'upper', 'zfill']
  >>> help(str.capitalize)
  Help on method_descriptor:
  capitalize(...)
  S.capitalize() -> str
  Return a capitalized version of S, i.e. make the first character
  have upper case and the rest lower case.
  ```
## 6.10 Parsing Strings
  - You can find the index of a certain character.
    data.find('@') // Returns int value of index

# Chapter 7 - Files
---
## Glossary
  catch - To prevent an exception from terminating a program using the try and except statements
  newline - A character in a file indicating a new line, used to split a file into separate lines
  Pythonic - A technique that works elegantly in Python
  Quality Assurance - Team focused on insuring overal quality of a software product
  text file - Sequence of characters stored in permanent storage like a hard drive
---
## 7.1 Persistence
  - This chapter will cover the abilty to access Secondary Memory, which does not erase after termination of script
## 7.2 Opening Files
  - When opening a file, you are sending the OS the file name to look for.
  ex.
  ```python
  >>> newFile = open('file.txt')
  >>> print(newFile)
  <_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>
  ```
  - If the file opening is successful, OS returns a file hand
    - File Handle is used to read the data
  - If the file opening is not successful, the OS will return 'No such file or directory'
## 7.3 Text files and lines
  - newlines are used to break txt files into several lines
    ```python
    test = 'Hello\nWorld' ## prints Hello and World in separate lines
    ```
## 7.4 Reading Files
  - Once you receive the file hand, use a for loop to read through each line in the file:
  EX below returns the number of lines in a files
  ```python
    fhand = open('file.txt')
    count = 0
    for line in fhand:
      count = count + 1
    print('Line Count:', count)
  ```
## 7.5 Searching through a file
  - You can use the `var.startswith(stringVal)` command to find a certain line in a txt file.
  - Make sure to use line.rstrip() to eliminate any newLines from being printed
    ex:
    ```python
    fhand = open('file.txt')
    for line in fhand:
      line.rstrip() ## Eliminate any newLine values
      if(line.startsWith('From:')):
        print(line)
    ```
## 7.6 Letting the user choose the file name
  - Using input() to have user enter the fileName
## 7.7 Using try, except, and opening
  - A try/except block is a common way to prevent an invalid file location
    ```python
    fileName = input('Enter file name: ')
    try:
      newFile = open(fileN
  ```ame)
    except:
      print('File not found')
      exit()
    for line in newFile:
      print(line)
    ```
## 7.8 Writing Files
  - Pass the 'w' mode as a second parameter to indicate you are writing a file
  - Once successfully opened, you can use .write() to add to file.
    - Make sure to add a \n at the end of each line you append as it is not added automatically
  - Once finished writing, you must make sure to close the file to make sure the data is physically written
  ex:
  ``` bash
  >>> fout = open('newFile.txt.', 'w')
  >>> print(fout)
  <_io.TextIOWrapper name='output.txt' mode='w' encoding='cp1252'>
  >>> line1 = 'Hello World\n'
  >>> fout.write(line1)
  >>> fout.close()
  ```
