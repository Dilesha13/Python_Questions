def even_squares(lst: list) -> list:
    return [x**2 for x in lst if x % 2 == 0]

# Example usage:
print(even_squares([1, 2, 3, 4, 5]))  # Output: [4, 16]