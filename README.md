# Quantum Mechanics Library in Python

This repository contains a Python library for quantum mechanics calculations inspired by the book *"The Theoretical Minimum: Quantum Mechanics"* by Leonard Susskind and Art Friedman. The library provides the basic tools for quantum mechanical calculations, including vectors, operators, inner products, and various quantum principles. This is still under development and lacks a lot of features. As I'm still in the learning process I might have made mistakes in the conceptual or programming part of things so any corrections or feedback are greatly appreciated.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Current Development](#current-development)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To use the library, simply clone this repository to your local machine and install the necessary dependencies.

### Clone the Repository
```bash
git clone https://github.com/thatSuvrat/quantum_mechanics
cd quantum-mechanics
```

### Install Dependencies
This library requires Python 3.7 or higher, and the following packages:
- `numpy`: For numerical computations

You can install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Make sure you have `numpy` installed:
```bash
pip install numpy
```

## Usage

### Defining Vectors (Kets and Bras)

The library defines quantum state vectors (Kets) and their corresponding Bras, which are used to perform various operations like inner products and conjugation.

```python
from vectors import Ket, Bra

# Creating a Ket vector |ψ⟩
ket = Ket([1 + 1j, 0, -1j])

# Conjugating a Ket to get the corresponding Bra ⟨ψ|
bra = ket.conjugate()

# Inner product ⟨ψ|φ⟩ between two vectors
inner_prod = inner_product(bra, ket)
print("Inner Product:", inner_prod)
```

### Operators and Hermitian Conjugates

Operators can be defined as matrices, and their Hermitian conjugates can be calculated for various operations.

```python
from operators import Operator

# Define an operator (example: Pauli-X)
pauli_x = Operator([[0, 1], [1, 0]])

# Hermitian conjugate of the operator
pauli_x_dagger = pauli_x.hermitian_conjugate()

# Applying the operator to a Ket
result = pauli_x.apply(ket)
print("Result of applying Pauli-X:", result)
```

## Features

- **Bra and Ket vectors**: Define quantum state vectors as column (Ket) and row (Bra) vectors.
- **Inner product**: Calculate the inner product between a Bra and a Ket.

## Current Development

This library is still under development, and more features will be added in the future, including:

- Quantum principles (superposition, entanglement, etc.)
- Uncertainty principle calculations
- Particle dynamics and Schrödinger equation solvers
- Quantum gates and circuits

## Contributing

Contributions are welcome! If you have any improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

### How to contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
