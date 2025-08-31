from stats import get_book_text, num_of_words, get_count_of_characters

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = num_of_words(book_text)
    print(f"{word_count} words found in the document")
    char_count = get_count_of_characters(book_text)
    print(char_count)

main()