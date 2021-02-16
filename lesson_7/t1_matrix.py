class Matrix:
    def __init__(self, mat: list):
        self.mat = mat

    def __add__(self, other):
        """ Код не работает с одномерными матрицами, идея была сделать развилку.
        Но не придумал как отличить 1 от 2 мерной матрицы. Проверка через операторы или len списка-в-списке даёт ошибку.
        Как можно проверить размерность матрицы?
        if sum(self.mat):
            new_mat = []
            for i in range(len(self.mat)):
                new_mat.append(self.mat[i]+other.mat[i])
        else:
        """
        new_mat = [[] for _ in range(len(self.mat))]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                new_mat[i].append(self.mat[i][j] + other.mat[i][j])
        return Matrix(new_mat)

    def __str__(self):
        return f'Матрица:\n{self.mat}'

b = Matrix([[1,2,3],[4,5,6]])
a = Matrix([[11,12,13],[14,15,16]])
print(a)
print(b)
c = b + a
print(c)
