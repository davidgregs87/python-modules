import os
#print(os.getcwd())
os.chdir("C:\\Users\\udohd\\my music")
print(os.getcwd())
for i in os.listdir():
    print(i)
    f_name,f_ext = os.path.splitext(i)
    print(f_name)
    f_title = (f_name.split("-"))
    print(f_title)
    print("#{}-{}".format(f_ext,f_title))
  