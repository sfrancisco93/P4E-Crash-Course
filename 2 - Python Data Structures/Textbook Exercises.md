# Chapter 6
- Only assignment is in "Assignments" > Assignment 6.5.py
# Chapter 7
1. Write a program to read through a file and print the contents of the file (line by line) all in upper case.
```python
newFile = open('mbox-short.txt')
for line in newFile:
  print(line.upper())
```

2. Write a program to prompt for a file name, and then read through the file and look for lines of the form: __X-DSPAM-Confidence: 0.8475__

Once you get to this line, pull the line apart and extract the floating-point number.  Test with mbox.txt and mbox-short.txt files

``` python
fileName = input('Enter file name:')
rd = open(fileName)
spamConfidence = 0
count = 0
for line in rd:
    line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        spamConfidence = spamConfidence + float(line[20:])
        count = count + 1
print(spamConfidence / count)
```

3. Add an easter egg to your program:
``` python
fileName = input('Enter file name:')
if(fileName = 'na na boo boo'):
    print('Nah')
else:
    try:
        rd = open(fileName)
    except:
        print('File not found')
    spamConfidence = 0
    count = 0
    for line in rd:
        line.rstrip()
        if line.startswith('X-DSPAM-Confidence'):
            spamConfidence = spamConfidence + float(line[20:])
            count = count + 1
    print(spamConfidence / count)
```
