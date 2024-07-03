def sort_dict_by_values(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Example usage:
print(sort_dict_by_values({"apple": 3, "banana": 1, "cherry": 2}))  # Output: {'banana': 1, 'cherry': 2, 'apple': 3}
