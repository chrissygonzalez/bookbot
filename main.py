import sys
from stats import count_words, count_chars, get_sorted_char_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    char_count = count_chars(text)
    sorted_char_count = get_sorted_char_dictionaries(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")

    for entry in sorted_char_count:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['count']}")

    print("============= END ===============")

main()