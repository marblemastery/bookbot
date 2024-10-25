def main():
    # Establish a path to the book
    book_path = "books/frankenstein.txt"
    
    # Stores the book's text in a string using get_boox_text function
    text = get_book_text(book_path)
    
    # Stores the number of individual words in the book in an int using get_num_words function
    num_words = get_num_words(text)
    
    # Stores the count of individual letters in the book in a dictionary using get_character_repetition function
    num_letters = get_character_repetition(text)
    
    print_report(book_path, num_words, num_letters)

# Takes text and splits it into words
def get_num_words(text):
    words = text.split()
    return len(words)

# Takes the book's path and opens it to store in text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Takes text and counts the letters in it    
def get_character_repetition(text):
    from collections import Counter
    lowercase_text = text.lower()
    letters_only = ""
    for char in lowercase_text:
        if char.isalpha():
            letters_only = letters_only + char
    letter_count = Counter(letters_only)
    letter_list = []
    for letter, count in letter_count.items():
        letter_list.append({"letter": letter, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

# Generates a report on the book
def print_report(book_path, num_words, num_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for what_letter in num_letters:
        print(f"The '{what_letter['letter']}' character was found {what_letter['num']} times")
    print("--- End report ---")


    return

main()

