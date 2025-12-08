# The Karatsuba multiplcation algorithm implemented in Python 3.

def karatsuba(x, y):
    # Handling of negative numbers:
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)
    
    # Calculate the digit-length of the larger number:
    n = max(len(str(x)), len(str(y)))
    
    # Base case:
    if n < 10:
       return x * y

    # Calculate the split position:
    m = n // 2

    # Split x and y in half:
    high_x = x // 10**m
    low_x = x % 10**m
    high_y = y // 10**m
    low_y = y % 10**m
    
    # Perform three recursive multiplications:
    z1 = karatsuba(low_x, low_y)
    z2 = karatsuba(high_x + low_x, high_y + low_y)
    z3 = karatsuba(high_x, high_y)

    # Combine z1, z2, and z3 using the general Karatsuba formula:
    return sign * ((z3 * 10**(2 * m)) + ((z2 - z3 - z1) * 10**m) + z1)