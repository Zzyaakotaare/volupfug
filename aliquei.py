def to_binary(n):
    """Convert an integer to its binary representation."""
    if isinstance(n, int):
        return bin(n)[2:]  # Use bin() function and strip the '0b' prefix
    else:
        raise ValueError("Input must be an integer.")

# Example usage
number = 10
binary_representation = to_binary(number)
print(binary_representation)  # Output: "1010"
