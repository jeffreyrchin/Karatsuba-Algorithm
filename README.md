# Karatsuba Algorithm

The Karatsuba Algorithm is a fast divide-and-conquer multiplication algorithm with a subquadratic time complexity. It is significantly faster than the grade-school multiplication algorithm, which runs in quadratic time. This repository contains a Python 3 implementation of the Karatsuba algorithm, as well as an implementation of the quadratic grade-school multiplication algorithm to compare performances of each on various test cases.

# Usage

Make sure you are in the root directory before running the following commands. To run the individual functions, execute the following lines of code in your terminal, replacing x and y with integers.

Karatsuba algorithm:
```bash
python src/karatsuba.py x y
```
Grade-school multiplication algorithm:
```bash
python src/naivemultiply.py x y
```

Example:
```bash
python src/karatsuba.py 1234 5678
python src/naivemultiply.py 1234 5678
```

To run the test cases, execute the following lines of code in your terminal:
```bash
python -m tests.karatsuba_tests
python -m tests.naivemultiply_tests
```

# Team Members

* Jeffrey Chin
* Jayraj Magar
* Mayank Bhardwaj
* Vaishnavi Chaughule
