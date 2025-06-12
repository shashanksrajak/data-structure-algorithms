# Code a diagnoal matrix in optimal way

class DiagonalMatrix:
    def __init__(self, matrix):
        """
        takes a 2-D diagonal matrix
        """
        self.diagonal_matrix = []
        self.size = len(matrix)
        # optimize this matrix
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    self.diagonal_matrix.append(matrix[i][j])

    # def __getattribute__(self, name):
    #     print("hola")
    def get_value(self, i, j):
        if i > self.size - 1 or j > self.size - 1:
            return -1
        if i != j:
            return 0
        else:
            return self.diagonal_matrix[i]


def func():
    # diagonal matrix
    matrix_2d = [[2, 0, 0], [0, 1, 0], [0, 0, 4]]

    # print in matrix format
    print("Diagonal matrix in original format")
    for row in matrix_2d:
        for num in row:
            print(num, end=" ")
        print("\n")

    optimized_matrix = []

    # optimize this matrix
    for i in range(len(matrix_2d)):
        for j in range(len(matrix_2d)):
            if i == j:
                optimized_matrix.append(matrix_2d[i][j])

    print("Optimized matrix", optimized_matrix)

    # Using this optimized_matrix we can recreate the original matrix
    print("Original matrix\n")

    for i in range(len(matrix_2d)):
        for j in range(len(matrix_2d)):
            if i == j:
                print(optimized_matrix[i], end=" ")
            else:
                print(0, end=" ")
        print("\n")


if __name__ == "__main__":
    # func()
    # diagonal matrix
    matrix_2d = [[2, 0, 0], [0, 6, 0], [0, 0, 4]]
    diagonal_matrix = DiagonalMatrix(matrix_2d)
    print("opimized form", diagonal_matrix.diagonal_matrix)

    print("D[1][1]", diagonal_matrix.get_value(1, 1))
    print("D[4][1]", diagonal_matrix.get_value(4, 1))
    print("D[1][2]", diagonal_matrix.get_value(1, 2))
