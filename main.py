from stats import get_num_words, letter_count, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath, "r") as f:
        string = f.read()
    return string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(code=1)

    text = get_book_text(sys.argv[1])
    letters = letter_count(text)
    sorted_letters = sort_dictionary(letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        if item[0].isalpha() == True:
            print(f"{item[0]}: {item[1]}")

main()