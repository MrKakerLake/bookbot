def get_book_text (filepath):
    with open (filepath) as f:
        text = f.read()
    return text 


def main():
    from stats import sorted_list
    from stats import num_words
    from stats import get_characters
    book_text = get_book_text("books/frankenstein.txt")
    word_count = num_words(book_text)
    characters = get_characters(book_text)
    sorted_chars = sorted_list(characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            num = char_dict["num"]
            print(f"{char}: {num}")
    print("============= END ===============")

main()