def get_book_text(fp):
    with open(fp) as f:
        content = f.read()
    return content

def num_of_words(text):
    words = text.split()
    return len(words)

def get_count_of_characters(text):
    char_dict = {}
    lowercase_text = text.lower()
    for c in lowercase_text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict