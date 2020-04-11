##
# Write code using find() and string slicing (see section 6.1) to
# extract the number at the end of the line below. Convert the
# extracted value to a floating point number and print it out.
##

test = "X-DSPAM-Confidence:     0.8475";
start = test.find('0')
value = float(test[start:start+6])
print(value)
