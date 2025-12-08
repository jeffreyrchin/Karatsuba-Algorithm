# The grade-school multiplcation algorithm implemented in Python 3.

def naive_multiply(x, y):
    # Handling of negative numbers:
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)

    # Base case:
    if x == 0 or y == 0:
        return 0

    # Reverse the digits of x and y:
    sx = str(x)[::-1]
    sy = str(y)[::-1]
    
    # Initialize the result array:
    res = [0] * (len(sx) + len(sy))

    # Perform digit-wise multiplications:
    for i, dx in enumerate(sx):
        for j, dy in enumerate(sy):
            res[i + j] += int(dx) * int(dy)
            res[i + j + 1] += res[i + j] // 10
            res[i + j] %= 10

    # Trim leading zeros:
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    # Convert result array to an integer
    result = int("".join(str(d) for d in reversed(res)))
    return sign * result

# Command-line interface:
import sys
if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(naive_multiply(x, y))