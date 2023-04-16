import re
import sys
txt = "if i was made from a broken mould"
x = re.search("^if.*mould$",txt)
print(x)

print(sys.byteorder)

s = "Open the portal of the multiverse"
match = re.search(r'portal', s)
print('Start Index:', match.start())
print('End Index:', match.end())

#Learning how to use Meta-characters in RegEX

# "\"" is used for explaining the character following it
# "^"  is used for matching the beginning of a search
# "$"  is used for matching the end of a search
# "." matching any character except newline
# "|" means OR (matches any character separated by it)
# "?" matches 0 or 1 occurences
 
string = "Open the portal of the multiverse!"
pattern = r"[a-m]"
match = re.findall(pattern, string)
print(match)


d = "I was born on June 24"
a = r"(\w+) (\d+)"
c = re.search(a,d)
if c:
    print("Search Range:",(c.start (),c.end ()))  # Gives the position where the match starts and stops.
    print("Match", c.group(0))  # Returns the full match
    print("Month", c.group(1))  # Returns the first item on the match
    print("Day", c.group(2)) # Returns the second item on the match 
else:
    print("Could'nt find match!")


sen = "The multiverse of things!"
regex = r"\bTh"
result = re.search(regex, sen)
print(result.re) # Returns the RegEX used in the search
print(result.string)  # Gives back the original string