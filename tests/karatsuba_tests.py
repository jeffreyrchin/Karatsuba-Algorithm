from src.karatsuba import karatsuba

def test_karatsuba():
   tests = [
       (2, 3),
       (12, 34),
       (1234, 5678),
       (9999, 9999),
       (12345678, 87654321),
       (123456789012345, 987654321098765),    # large numbers
       (0, 12345),
       (12345, 0),
       (9, 8),                                 # single digit
       (1000000000000000, 1000000000000000)    # 10^15 * 10^15
   ]
   for a, b in tests:
       expected = a * b
       result = karatsuba(a, b)
       print(f"{a} × {b} = {result}  |  Correct: {result == expected}")
       
# Run tests
test_karatsuba()