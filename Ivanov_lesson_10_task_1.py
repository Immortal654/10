class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.matrix, other.matrix)])


rows = int(input("Введите количество строк и столбцов матрицы: "))
cols = rows

matrix1 = Matrix([[i * j for j in range(rows)] for i in range(cols)])
matrix2 = Matrix([[i * j for j in range(rows)] for i in range(cols)])

print('First matrix:\n', matrix1, end='\n\n')
print('Second matrix:\n', matrix2, end='\n\n')
print('Summ of first and second matrix:\n', matrix1 + matrix2)
