def add_matrix(mat=[[]]):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("{:d}".format(mat[i][j]),
                  end=" " if j - len(mat[i]) == -1 else " ")
        print()

mat = [
    [2,4,3],
    [5,6,7],
    [9,1,4]
]
add_matrix(mat)


tri=[1]
a = tri[-1]
for x in range(len(a) -1):
    print(x)
