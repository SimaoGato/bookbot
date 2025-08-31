from stats import get_book_text, num_of_words, get_count_of_characters, sort_dict

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = num_of_words(book_text)
    # print(f"{word_count} words found in the document")
    char_count = get_count_of_characters(book_text)
    sorted_char_count = sort_dict(char_count)
    # print(char_count)
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {book_path}...\n"
    "----------- Word Count ----------\n"
    f"Found {word_count} total words\n"
    "--------- Character Count -------")
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()