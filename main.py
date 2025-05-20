from stats import get_book_text, character_count, list_of_dicts
import sys

def main():
    book = get_book_text(sys.argv[1])
    count = character_count(sys.argv[1])
    sorted = list_of_dicts(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()


#main()


