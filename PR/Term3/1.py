import numpy as np

my_array = np.arange(10, 70, 2)
print(f'my_array = {my_array}')
print()

def show_matrix(mat):
    s = ""
    for line in mat:
        for e in line:
            s = s+" "+str(int(e))
        s = s+"\n"
    print(s)

A = my_array.reshape(6,5)
A = A.transpose()
print(f'TR_A = ')
show_matrix(A)

A = A * 2.5
A[0] -= 5
print(f'A after * and - = ')
show_matrix(A)

B = np.random.randint (0, 10, (6, 3))
print(f'B = ')
show_matrix(B)

row_sums = A.sum(axis=1)
vector_a = row_sums[:, None]
print(f'len vector a = {len(vector_a)}')
print()

column_sums = B.sum(axis=0)
vector_b = column_sums[:, None]
print(f'len vector b = {len(vector_b)}')
print()

C = np.dot(A,B)
print(f'C =')
show_matrix(C)

A = np.delete(A,2,1) #(матрица, номер строки/столбца с 0, направление 0/1)
print(f'A (5х5) =')
show_matrix(A)

add_B = np.random.randint(10, 20, size=(6,3))
B = np.concatenate([B, add_B], axis=1)
print(f'B (6х6) =')
show_matrix(B)

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
print(f'det_A = {det_A}, det_B = {det_B}')
print()

print(np.linalg.inv(A) if det_A != 0 else "NO INV FOR A")
print(f'INV B = {np.linalg.inv(B)}' if det_B != 0 else "NO INV FOR B")
print()

print(f'A in 6 = {np.linalg.matrix_power(A, 6)}')
print()

print(f'B in 14 = {np.linalg.matrix_power(B, 14)}')
print()

print("Variant_4")
a = np.array([[2.3, 0, -3.4, -12], [2.6, 8.4, -9, 3], [1.3, 4.5, -17, 2], [1.8, 0, 15, 16]])
b = np.array([-14, 0.4, -3.6, 17.4])
x = np.linalg.solve(a, b)

print(f'Solve = {x}')
print(np.allclose(np.dot(a, x), b))
