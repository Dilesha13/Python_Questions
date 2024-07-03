def count_words(file_path: str) -> int:
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return 0

# Example usage:
file_path = 'problem_3/textfile.txt'
print(count_words(file_path))  # Update this line with the correct path
