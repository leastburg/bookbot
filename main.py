book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(string):
    words_list = string.split()
    return len(words_list)

main()