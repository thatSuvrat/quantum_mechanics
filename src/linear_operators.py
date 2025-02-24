import numpy as np
from vectors import Ket, Bra


class LinearOperator:
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=np.complex128)

        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("Linear Operator Must be a Square Matrix")

    def __repr__(self):
        return f"Operator:\n{self.matrix}\n"

    def Apply(self, vector):
        if isinstance(vector, Ket):
            if vector.vector.shape[0] != self.matrix.shape[1]:
                raise ValueError("Dimension Mismatch between Operator and Ket Vector")
            return Ket(np.dot(self.matrix, vector.vector))
        elif isinstance(vector, Bra):
            if vector.vector.shape[1] != self.matrix.shape[1]:
                raise ValueError("Dimension Mismatch between Operator and Bra Vector")
            return Bra(np.dot(vector.vector, self.matrix))
        else:
            raise TypeError("Can only apply to Ket or Bra Vector")
        

    def HermitianConjugate(self):
        return LinearOperator(self.matrix.conj().T)

    def IsHermitian(self):
        return np.allclose(self.matrix, self.matrix.conj().T)

    def Eigen(self):
        eigenvalues, eigenvectors = np.linalg.eig(self.matrix)

        eigenvector_kets = [
            Ket(vec) for vec in eigenvectors.T
        ]  # Turning Eigenvectors to Ket Vectors

        return eigenvalues, eigenvector_kets

    # Adding Arithmetic Operators

    def __add__(self, other):
        if not isinstance(other, LinearOperator):
            raise TypeError("Can only add another Linear Operator")

        return LinearOperator(self.matrix + other.matrix)

    def __sub__(self, other):
        if not isinstance(other, LinearOperator):
            raise TypeError("Can only subtract another Linear Operator")

        return LinearOperator(self.matrix - other.matrix)

    def __mul__(self, other):
        if isinstance(other, LinearOperator):
            return LinearOperator(self.matrix @ other.matrix)
        if isinstance(other, Ket):
            return self.Apply(other)
        if isinstance(other, (int, float, complex)):
            return LinearOperator(self.matrix * other)
        else:
            raise TypeError("Can only multiply by Linear Operator or Scalar")

    def __rmul__(self, right):
        if isinstance(right, (int, float, complex)):
            return LinearOperator(right * self.matrix)
        else:
            raise ValueError("Can only multiply by a Scalar or Bra vector")


# Standard Pauli matrices
SIGMA_X = LinearOperator([[0, 1], [1, 0]])  # Pauli X (flip)
SIGMA_Y = LinearOperator([[0, -1j], [1j, 0]])  # Pauli Y
SIGMA_Z = LinearOperator([[1, 0], [0, -1]])  # Pauli Z
IDENTITY = LinearOperator([[1, 0], [0, 1]])  # Identity matrix


# Defining Function to Create Operator Based on Pauli Matrices
def create_operator(x, y, z):
    return LinearOperator((x * SIGMA_X + y * SIGMA_Y + z * SIGMA_Z).matrix)


class Unitary(LinearOperator):
    def __init__(self, matrix):
        super().__init__(matrix)

        hermitian_conjugate = self.HermitianConjugate()

        # Check if U†U = I
        if not np.allclose(
            (hermitian_conjugate * self).matrix, np.identity(self.matrix.shape[0])
        ):
            raise ValueError("U†U = I not satisfied")

        self.matrix = matrix


HADAMARD = Unitary((1 / np.sqrt(2)) * np.matrix([[1, 1], [1, -1]]))

if __name__ == "__main__":
    operator = LinearOperator([[1, 2j], [1, -2j]])
    # print(sigma_z.apply(U))
    # print(sigma_z.apply(R))
    # print(L)

    # print(sigma_z.matrix)
    # print(sigma_z.HermitianConjugate())

    # print (sigma_z * (2 + 3j))
    # print(U)
    # print(operator.apply(U))

    # eigenvalue, eigenvector = SIGMA_X.Eigen()
    # print('Eigenvalues are: ', eigenvalue)
    # print('Eigenvectors are:' )
    # print(R)
    # print(L)    # for vector in eigenvector:

    # Example of a Unitary matrix (Hadamard gate)
    # Hadamard_matrix = (1/np.sqrt(2)) * np.matrix([[1, 1], [1, -1]])
    # Hadamard = Unitary(Hadamard_matrix)
    # print("Hadamard Gate (Unitary):")
    # print(Hadamard)

    # Example of a non-Unitary matrix (will raise ValueError)
    # non_unitary_matrix = np.array([[1, 0], [0, 2]])

    # This will raise a ValueError because non_unitary_matrix is not unitary
    # Non_Unitary = Unitary(non_unitary_matrix)
    # print(Non_Unitary)

    # for vector in eigenvector:
    #     print(vector)