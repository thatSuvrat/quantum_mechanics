''' This is the calculation shown at the end of Lecture 3 in the book.'''


from vectors import *
from linear_operators import create_operator
from numpy import sin, cos, pi
# print(pi)

# Uncomment all of this to check the exercise in lecture:
# theta = pi/6 # This should work for any value of theta. For calculating I used 30° or π/6
# operator = create_operator(sin(theta), 0, cos(theta))
# eigenvalues, eigenvectors = operator.Eigen()

# for i in range(2):
#     print(f"λ{i+1} = {int(eigenvalues[i])}")
#     print(f" |λ{i+1}> = {eigenvectors[i].vector}\n")
    
# '''Page 86 What the calculation shows us '''
# print("What the calculation in book shows")
# print(f"λ1 = 1")
# print(f" |λ1> = {[[cos(theta/2)], [sin(theta/2)]]} \n")

# print(f"λ2 = -1")
# print(f" |λ2> = {[[-sin(theta/2)], [cos(theta/2)]]} \n")


# ''' Page 87'''
# p1 = inner_product(eigenvectors[0].conjugate(), U) * inner_product(U.conjugate(), eigenvectors[0])
# p2 = inner_product(eigenvectors[1].conjugate(), U) * inner_product(U.conjugate(), eigenvectors[1])

# print(f" P(+1) = Computation: {p1} \n Book: {cos(theta/2) ** 2} \n")
# print(f" P(-1) = Computation: {p2} \n Book: {sin(theta/2) ** 2}")

# ''' The values match but the datatypes currently don't match. I'm not fixing datatypes for just this test run...... '''

# # ket = Ket([1,2])
# # print(type(ket.vector))
# # print(eigenvectors[0].vector)


# # Exercise 3.4 To be solved by students
# theta = pi/2
# phi = pi/4

# nx = sin(theta)*cos(phi)
# ny = sin(theta)*sin(phi)
# nz = cos(theta)

# m = create_operator(nx, ny, nz)
# vals, vecs = m.Eigen()

# for i in range(2):
#     print(f"λ{i+1} = {int(vals[i])}")
#     print(f" |λ{i+1}> = {vecs[i].vector}\n")