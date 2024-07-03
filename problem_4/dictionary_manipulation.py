"""Problem 4: Dictionary Manipulation
Write a function that takes a dictionary with string keys and integer values and returns a dictionary sorted by the values."""

def sort_dict_by_values(d: dict) -> dict:
    # Sort dictionary items by value
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Example usage:
print(sort_dict_by_values({"apple": 3, "banana": 1, "cherry": 2}))  
# Output: {'banana': 1, 'cherry': 2, 'apple': 3}