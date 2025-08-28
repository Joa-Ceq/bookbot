from stats import *
import sys
# FILE_PATH = "books/frankenstein.txt"

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
FILE_PATH = sys.argv[1]
def main():
    num = count_words(FILE_PATH)
    #print(f"{num} words found in the document")
    chars = count_characters(FILE_PATH)
    # print(chars)
    sorted_chars = sort_dict(chars)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {FILE_PATH}...\n----------- Word Count ----------\nFound {num} total words\n--------- Character Count -------")
    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
        
    
main()