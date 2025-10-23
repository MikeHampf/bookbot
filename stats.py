def get_num_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return f"Found {num_words} total words"

def letter_count(text):
    letters = {}
    for i in range(0,len(text)):
        if text[i].lower() in letters:
            letters[text[i].lower()] += 1
        else:
            letters[text[i].lower()] = 1
    return letters

def sort_dictionary(letters):
    sorted_letters = sorted(letters.items() ,key=lambda x : x[1], reverse=True)
    return sorted_letters