# Code a Lower Triangular Matrix and Optimize it in row-major form
class LowerTriangularMatrix:
    def __init__(self, matrix):
        """
        takes a 2-D lower tri matrix
        """
        self.lt_matrix = []
        self.size = len(matrix)

        # optimize this matrix
        for i in range(self.size):
            for j in range(self.size):
                if i >= j:
                    self.lt_matrix.append(matrix[i][j])

    def get_index(self, i, j):
        return int(i * (i+1)/2 + j)

    def get_value(self, i, j):
        if i > self.size - 1 or j > self.size - 1:
            return -1
        if i < j:
            return 0
        else:
            # for 0 based indexed matrices
            index = int(i * (i+1)/2 + j)
            return self.lt_matrix[index]

    def print_matrix(self):
        # Using this optimized_matrix we can recreate the original matrix
        print("\nOriginal matrix\n")

        for i in range(self.size):
            for j in range(self.size):
                if i < j:
                    print(0, end=" ")
                else:
                    print(self.lt_matrix[self.get_index(i, j)], end=" ")
            print("\n")


if __name__ == "__main__":
    matrix = [[2, 0, 0], [1, 3, 0], [5, 6, 9]]
    lt_matrix = LowerTriangularMatrix(matrix)

    print(lt_matrix.lt_matrix)

    print("A[1][2]", lt_matrix.get_value(1, 1))

    lt_matrix.print_matrix()
