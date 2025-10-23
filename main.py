from stats import get_num_words
from stats import letter_count

def get_book_text(filepath):
    with open(filepath, "r") as f:
        string = f.read()
    return string

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(text)} total words")
    print(letter_count(text))

    

main()