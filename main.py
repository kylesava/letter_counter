from collections import Counter

def count_letter_usage(text):
    # Filter out non-alphabetic characters and convert to lowercase
    filtered_text = ''.join(char.lower() for char in text if char.isalpha())
    # Count the letters
    letter_count = Counter(filtered_text)
    return letter_count

def main():
    # Ask the user for input
    user_input = input("Enter a string: ")
    # Get the letter counts
    letter_counts = count_letter_usage(user_input)
    
    # Print the results
    print("\nLetter Usage Count:")
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter}: {count}")

if __name__ == "__main__":
    main()
