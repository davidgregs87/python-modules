# UNICODE CHARACTER DATABASE
import unicodedata as ucd
import string

d = 'orange'
print("the string is:", d)
d_utf = d.encode()
print("the encoded string is: ", d_utf)


print(ucd.bidirectional("\u6760"))
