"""Problem 3: File I/O
   Write a function that reads a text file, counts the number of words in it, and returns the count."""

def count_words(file_path: str) -> int:
    # Try to open the file at the given path
    try:
        with open(file_path, 'r') as file:
            # Read the entire text from the file
            text = file.read()
            # Split the text into individual words
            words = text.split()
            # Return the number of words
            return len(words)
    # If the file is not found, catch the FileNotFoundError exception
    except FileNotFoundError:
        # Print an error message with the file path
        print(f"The file at {file_path} was not found.")
        # Return 0 as the word count
        return 0

# Example usage:
file_path = 'problem_3/textfile.txt'
print(count_words(file_path))  # Update this line with the correct path