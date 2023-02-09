book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_letters(text)
    chars_list = dictionary_to_list(chars_dict)
   
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")
    print()

    for item in chars_list:
        print(f"The '{item[0]}' character was found '{item[1]}' times")



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
        elif lowered not in letter_count and lowered.isalpha():
            letter_count[lowered] = 1
    return letter_count

def dictionary_to_list(dictionary):
    sorted_list = list(dictionary.items())
    print(sorted_list)
    sorted_list.sort(key = lambda i:i[1], reverse = True)
    return sorted_list
    
    

main()