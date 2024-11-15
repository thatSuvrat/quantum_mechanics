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


def inner_product(bra, ket):
    if isinstance(bra, Bra) and isinstance(ket,Ket):
        return np.vdot(bra.vector, ket.vector)
    else:
        raise ValueError("Product requires one Bra and one Ket vector")

if __name__ == "__main__":
    psi_bra = Bra([1+1j, 0, -1j])
    psi_ket = psi_bra.conjugate()
    

    try:
        inner_prod = inner_product(psi_bra, psi_ket)
        print("Inner Product ⟨ψ|ψ⟩:", inner_prod)
    except ValueError as e:
        print(e)

    try:
        inner_prod = inner_product(psi_ket,psi_ket) # Should raise an error
        print("Inner Product ⟨ψ|ψ⟩:", inner_prod)
    except ValueError as e:
        print(e)