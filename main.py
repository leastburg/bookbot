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


# this retrieves the book text file you would like the program to examine and converts it into one long string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# this turns a string into an array of words, and counts the number of words
def get_num_words(string):
    words_list = string.split()
    return len(words_list)

# this makes a dictionary with a count of how many times each character from the alphabet occurs in a string
def get_num_letters(string):
    letter_count = {}
    for character in string:
        lowered = character.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        elif lowered not in letter_count and lowered.isalpha():
            letter_count[lowered] = 1
    return letter_count

# this turns a dictionary into a sorted list of tuples, sorted by the value rather than the key, in descending order
def dictionary_to_list(dictionary):
    sorted_list = list(dictionary.items())
    sorted_list.sort(key = lambda i:i[1], reverse = True)
    return sorted_list
    
    

main()