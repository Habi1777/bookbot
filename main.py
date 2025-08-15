import sys
import traceback
import os
from stats import count_words_in_string, count_characters, dictionary_to_sorted_list

def get_book_text(f):
    with open(f) as book:
        book_contents = book.read()
        return book_contents

def main():
    try:
        if len(sys.argv) == 2:
            book_location = sys.argv[1]
            if os.path.exists(book_location):
                print("============ BOOKBOT ============")
                print(f"Analyzing book found at {book_location}...")
                print("----------- Word Count ----------")
                print(f"Found {count_words_in_string(get_book_text(book_location))} total words")
                print("--------- Character Count -------")
                for item in dictionary_to_sorted_list(count_characters(get_book_text(book_location))):
                    if item["char"].isalpha():
                        print(f"{item["char"]}: {item["num"]}")
                print("============= END ===============")
            else: 
                raise FileNotFoundError
        else:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    except FileNotFoundError:
        sys.exit("File does not exist")
    except EOFError:
        sys.exit("manually stopped code with ctrl+d for linux or ctrl+z for windows")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()