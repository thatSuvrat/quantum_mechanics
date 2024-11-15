import numpy as np
from vectors import Ket, Bra

class LinearOperator:
    def __init__(self,matrix):
        self.matrix = np.array(matrix, dtype=np.complex128)

        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("Linear Operator Must be a Square Matrix")
    
    def __repr__(self):
        return f"Operator:\n{self.matrix}\n"
    
    def apply(self, ket):
        if not isinstance(ket, Ket):
            raise TypeError("Can only apply to Ket Vector")
        if ket.vector.shape[0] != self.matrix.shape[1]:
            raise ValueError("Dimension Mismatch between Operator and Ket Vector")
        return Ket(np.dot(self.matrix, ket.vector))
    
    def apply_to_bra(self, bra):
        if not isinstance(bra, Bra):
            raise TypeError('Can only apply to Bra Vector')
        
        pass
    
    def HermitianConjugate(self):
        return(LinearOperator(self.matrix.conj().T))
    
    def isHermitian(self):
        return np.allclose(self.matrix, self.matrix.conj().T)
    
    # Adding Arithmetic Operators
    
    def __add__(self, other):
        if not isinstance(other,LinearOperator):
            raise TypeError('Can only add another Linear Operator')
        
        return LinearOperator(self.matrix + other.matrix)
     
    def __sub__(self, other):
        if not isinstance(other, LinearOperator):
            raise TypeError('Can only subtract another Linear Operator')
        
        return LinearOperator(self.matrix - other.matrix)
    
    def __mul__(self, other):
        if isinstance(other, LinearOperator):
            return LinearOperator(np.dot(self.matrix, other.matrix))
        if isinstance(other, (int, float, complex)):
            return LinearOperator(self.matrix * other)
        else:
            raise TypeError('Can only multiply by Linear Operator or Scalar')

    def __rmul__(self, scalar):
        if isinstance(scalar, (int, float, complex)):
            return LinearOperator(self.matrix * scalar)
        else: 
            raise ValueError('Can only multiply by a Scalar')
        
        
        
# Standard Pauli matrices
sigma_x = LinearOperator([[0, 1], [1, 0]])  # Pauli X (flip)
sigma_y = LinearOperator([[0, -1j], [1j, 0]])  # Pauli Y
sigma_z = LinearOperator([[1, 0], [0, -1]])  # Pauli Z
identity = LinearOperator([[1, 0], [0, 1]])  # Identity matrix



if __name__ == '__main__':
    operator = LinearOperator([[1,2j],[1,-2j]])
    # print(sigma_z.apply(U))
    # print(sigma_z.apply(R))
    # print(L)
    
    # print(sigma_z.matrix)
    # print(sigma_z.HermitianConjugate())
    
    # print (sigma_z * (2 + 3j))
    # print(U)
    # print(operator.apply(U))