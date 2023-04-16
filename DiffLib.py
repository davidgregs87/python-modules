import difflib as dl
import sys
import keyword as key
s1 = ['python','java','c++','PHP']
s2 = ['python','perl','c','PHP']
dl.context_diff(s1,s2)
for diff in dl.context_diff(s1,s2):
    print(diff) # prints out the result to shows us the difference and compare the two set of lists


words = dl.get_close_matches("give",["live","sin","glee"])  # Returns 'live' as the closet match to the string 'give'
print(words)

d1 = ['python\n','java\n','c++\n','PHP\n']
d2 = ['python\n','perl\n','c\n','PHP\n']
sys.stdout.writelines(dl.context_diff(d1,d2, fromfile='before.py', tofile= 'after.py'))

"""Compares two string and instead of printing out the result on the terminal, the result is being written to an
HTML file."""
x1 = "abcef"
x2 = "bhejw"
d = dl.HtmlDiff()
ans = d.make_file(x1,x2)
with open("diff.html", "w") as f:
    for lines in ans.splitlines():
        print(lines, file=f)


with open("after.txt") as f:
    file1_line = f.readlines()
with open("before.txt") as f:
    file2_line = f.readlines()
    d = dl.Differ()
    ans = list(d.compare(file1_line,file2_line))
    ans = '\n'.join(ans)
    print(ans)

s = dl.__builtins__
print(s)
a = dl.__file__
print(a)

match = dl.get_close_matches("", key.kwlist)
print(match)