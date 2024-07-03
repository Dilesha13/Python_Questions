"""Problem 2: List Comprehensions
   Given a list of integers, write a function to return a list of squares of even numbers only."""

def even_squares(lst: list) -> list:
    #create a list of squares of even numbers
    return [x**2 for x in lst if x % 2 == 0]

# Example usage:
print(even_squares([1, 2, 3, 4, 5]))  # Output: [4, 16]