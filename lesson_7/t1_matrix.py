class Matrix:
    def __init__(self, mat: list):
        self.mat = mat

    def __add__(self, other):

        if isinstance(self.mat[0], int):
            new_mat = []
            for i in range(len(self.mat)):
                new_mat.append(self.mat[i]+other.mat[i])
        else:
            new_mat = [[] for _ in range(len(self.mat))]
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    new_mat[i].append(self.mat[i][j] + other.mat[i][j])
        return Matrix(new_mat)

    def __str__(self):
        return f'Матрица:\n{self.mat}'


b = Matrix([1, 2, 3])
a = Matrix([11, 12, 13])
print(a)
print(b)
c = b + a
print(c)
