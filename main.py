from stats import get_num_words, count_characters, sort_letters, sort_on
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    counts = count_characters(text)
    sorted_chars = sort_letters(counts)

    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

    print("============= END ===============")

main()