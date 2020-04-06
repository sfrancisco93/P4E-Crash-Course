# Chapter 6 - Strings
6.1 What is String
  - String is a sequence of characters
  - + means 'concatenate'
  - int(stringValue) to change to a number
6.2 Getting the length of a string using len

```
length = len(fruit)
first = fruit[0]
last = fruit[length - 1]
```

6.3 Traversal through a string with a loop

```
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1
```

6.4 String Slices

```
s = 'Test String'
test = s[0:4]
print test ## Prints 'Test'
```

6.5 Strings are immutable
  - You cannot access and change a character in a string.
    ex:
    ```
    greeting = 'hello world'
    letter = greeting[0]
    letter = 'J'
    TypeError: 'str' object does not support item assignment
    ```
      - Workaround:
        - You must concatenate the character with the rest of the string.
        ex:
        ```
        greeting = 'hello world'
        letter = 'J'
        greeting = 'J' + greeting[1:]
        print(greeting)
        ```
        Output: Jello world
6.6 Looping and counting
  - You can loop through each letter in a word if needed.
    ex for letter in word:
6.7 in Operator
  - in is a boolean operator that takes two string. Returns True if the first string appears in the second string.
  ex:
    ```
    >>> 'a' in 'banana'
    True
    >>> 'c' in 'kangaroo'
    False
    ```
6.8 String comparison
  - word == string
  - word >/< string ## Indicates alphabetical order

6.9 String methods
    - String is a Python object. As a result, Strings do have methods that you can call upon.
    ```
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
  6.10 Parsing Strings
    - You can find the index of a certain character.
      data.find('@') // Returns int value of index
