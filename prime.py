def is_prime(n):
    """
    Check if a number is a prime number.

    A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
    This function uses a trial division method to determine if the number is prime.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Check if the number is less than or equal to 1
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    # Check if the number is 2 or 3
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    
    # Check if the number is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime
    
    # Check for factors from 5 to the square root of n
    # We check i and i + 2 to skip even numbers and multiples of 3
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False  # If n is divisible by any of these numbers, it is not prime
    
    # If no factors were found, the number is prime
    return True
#q: what does the function above do?
#a: checks if a number is prime or not
#q: what is the time complexity of the function above?
#a: O(sqrt(n))
#q: what is the space complexity of the function above?
#a: O(1)

# create a function to do 5 unit tests of the code above
def test_is_prime():
    # test when n is 0
    assert is_prime(0) == False
    # test when n is 1
    assert is_prime(1) == False
    # test when n is 2
    assert is_prime(2) == True
    # test when n is 3
    assert is_prime(3) == True
    # test when n is 4
    assert is_prime(4) == False
    print("All test cases pass")