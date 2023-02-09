book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words)
    chars_dict = get_num_letters(text)
    print(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(string):
    words_list = string.split()
    return len(words_list)

def get_num_letters(string):
    letter_count = {}
    for character in string:
        lowered = character.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        elif lowered not in letter_count:
            letter_count[lowered] = 1
    return letter_count
    

main()