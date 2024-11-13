from vectors import Bra, Ket, inner_product
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