# How to read a file
with open ("factors.txt", 'r') as file:
    var = file.read()
print(var)
file.close()
pass

# How to append a file
with open ("factors.txt", 'a') as file:
    var = file.write("\nFind the factors of the following numbers")
print(var)
file.close()
pass