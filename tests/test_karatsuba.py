from src.karatsuba import karatsuba

def test_karatsuba():
    tests = [
        # Basic small numbers
        (2, 3),
        (5, 7),
        (9, 9),
        (1, 1),
        (0, 0),
        
        # Two-digit numbers
        (12, 34),
        (45, 67),
        (99, 99),
        (10, 10),
        (25, 40),
        
        # Three-digit numbers
        (123, 456),
        (999, 888),
        (100, 200),
        (555, 777),
        
        # Four-digit numbers
        (1234, 5678),
        (9999, 9999),
        (1000, 1000),
        (4567, 8901),
        
        # Large numbers (5-7 digits)
        (12345, 67890),
        (99999, 88888),
        (100000, 200000),
        
        # Very large numbers (8+ digits)
        (12345678, 87654321),
        (123456789, 987654321),
        (123456789012345, 987654321098765),
        (10**15, 10**15),
        (10**20, 10**10),
        
        # Zero cases
        (0, 12345),
        (12345, 0),
        (0, 0),
        (0, 999999999),
        
        # Single-digit numbers
        (1, 9),
        (9, 8),
        (7, 6),
        (3, 3),
        
        # Powers of 10
        (10, 100),
        (1000, 10000),
        (10**5, 10**6),
        (10**10, 10**8),
        
        # Negative numbers
        (-1234, 5678),          # negative × positive
        (1234, -5678),          # positive × negative
        (-1234, -5678),         # negative × negative
        (-99, -99),             # small negative × negative
        (-1, 100),              # negative one
        (-12345678, 87654321),  # large negative × positive
        (0, -5555),             # zero × negative
        
        # Numbers with different digit lengths
        (1, 123456789),         # 1-digit × 9-digit
        (12, 123456),           # 2-digit × 6-digit
        (1234, 12345678),       # 4-digit × 8-digit
        (99, 9999999),          # 2-digit × 7-digit
        
        # Edge cases with 9s
        (9, 9999999999),
        (999, 999999),
        
        # Random challenging cases
        (314159, 271828),       # pi and e digits
        (65536, 65536),         # power of 2
        (87654321, 12345678),   # reverse order
    ]
    
    print("=" * 80)
    print("KARATSUBA MULTIPLICATION TEST SUITE")
    print("=" * 80)
    print(f"Total test cases: {len(tests)}\n")
    
    passed = 0
    failed = 0
    
    for i, (a, b) in enumerate(tests, 1):
        expected = a * b
        result = karatsuba(a, b)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"Test {i:2d}: {a:20d} × {b:20d} = {result:30d}  {status}")
        
        if result != expected:
            print(f"         Expected: {expected}, Got: {result}")
    
    print("\n" + "=" * 80)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("=" * 80)
    
    return failed == 0

# Run tests
if __name__ == "__main__":
    success = test_karatsuba()
    exit(0 if success else 1)