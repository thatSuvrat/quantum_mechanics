import numpy as np

class Ket:
    def __init__(self, vector):
        # Store the vector as a complex numpy array for easy manipulation
        self.vector = np.array(vector, dtype=np.complex128).reshape(-1, 1)
        
    def __repr__(self):
        return f"|ψ⟩: {self.vector}"
    
    def conjugate(self):
        # Return a Bra version (conjugate transpose)
        return Bra(self.vector.conj())

class Bra:
    def __init__(self, vector):
        # Store the vector as a complex numpy array for easy manipulation
        self.vector = np.array(vector, dtype=np.complex128).reshape(1, -1)
        
    def __repr__(self):
        return f"⟨ψ|: {self.vector}"
    
    def conjugate(self):
        # Return a Ket version (conjugate transpose)
        return Ket(self.vector.conj())
    
    def __mul__ (self,other):
        if isinstance(other, Ket):
            return np.dot(self.vector, other.vector)[0][0]
        else:
            pass


def inner_product(bra, ket):
    if isinstance(bra, Bra) and isinstance(ket,Ket):
        return np.vdot(bra.vector, ket.vector)
    else:
        raise ValueError("Product requires one Bra and one Ket vector")
    

from math import sqrt

U = Ket([1,0]) # up 
D = Ket([0,1]) # down

R = Ket([1/sqrt(2), 1/sqrt(2)]) # right
L = Ket([1/sqrt(2), -1/sqrt(2)]) # left
I = Ket([1/sqrt(2), 1j/sqrt(2)]) # in
O = Ket([1/sqrt(2), -1j/sqrt(2)]) # out


# Testing the statement written in the book 
# if __name__ == "__main__":
#     inner_prod = inner_product(O.conjugate(),U) * inner_product(U.conjugate(), O)
#     print(inner_prod) # It provides output 1/2 as shown in the book


__all__ = ["Bra", "Ket", "inner_product", 'U', 'D', 'R', 'L', 'I', 'O']
if __name__ == "__main__":
    pass
    # psi_bra = Bra([1+1j, 0, -1j])
    # psi_ket = psi_bra.conjugate()
    

    # try:
    #     inner_prod = inner_product(psi_bra, psi_ket)
    #     print("Inner Product ⟨ψ|ψ⟩:", inner_prod)
    # except ValueError as e:
    #     print(e)

    # try:
    #     inner_prod = inner_product(psi_ket,psi_ket) # Should raise an error
    #     print("Inner Product ⟨ψ|ψ⟩:", inner_prod)
    # except ValueError as e:
    #     print(e)