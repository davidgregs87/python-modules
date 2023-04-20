def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

# Example usage
n = 5
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
