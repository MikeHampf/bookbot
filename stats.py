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