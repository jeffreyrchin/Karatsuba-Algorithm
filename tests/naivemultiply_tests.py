from src.naivemultiply import naive_multiply

def test_naive_multiply():
   tests = [
       (2, 3),
       (12, 34),
       (1234, 5678),
       (9999, 9999),
       (12345678, 87654321),
       (123456789012345, 987654321098765),      # large numbers
       (0, 12345),
       (12345, 0),
       (9, 8),                                   # single-digit
       (10**15, 10**15),                         # very large powers of 10
       (-1234, 5678),                            # negative × positive
       (1234, -5678),                            # positive × negative
       (-1234, -5678)                            # negative × negative
   ]
   for a, b in tests:
       expected = a * b
       result = naive_multiply(a, b)
       print(f"{a} × {b} = {result}  |  Correct: {result == expected}")

# Run tests
test_naive_multiply()