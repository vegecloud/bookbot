import sys
from stats import count_words, dict_count, dict_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1] # use command line 2nd argument (the .txt file to extract from)
    text = get_book_text(filepath) # extract all texts from .txt file 
    word_counts = count_words(text) # obtain total count of words
    dict_counts = dict_count(text) # obtain dictionary of counts for each char
    list_counts = dict_char(dict_counts) # obtain list of dictionary of counts

    print(
        '============ BOOKBOT ============\n',
        f'Analyzing book found at {filepath}\n',
        '----------- Word Count -----------\n',
        f'Found {word_counts} total words\n',
        '--------- Character Count ---------'
    )

    for character in list_counts:
        if character['char'].isalpha():
            print(f'{character['char']}: {character['num']}')

# main program

main()