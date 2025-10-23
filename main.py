from stats import get_num_words, letter_count, sort_dictionary

def get_book_text(filepath):
    with open(filepath, "r") as f:
        string = f.read()
    return string

def main():
    text = get_book_text("books/frankenstein.txt")
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