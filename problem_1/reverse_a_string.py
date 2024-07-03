"""Problem 1: Reverse a String
   Write a function that takes a string as input and returns the string reversed."""

def reverse_string(s: str) -> str:
    #Reverse the string
    return s[::-1]

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"