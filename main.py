def main():
    book_path = "github.com/gnomeocracy/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_dictionary  = get_character_dictionary(text)
    sorted_list = dictionary_to_sorted_list(character_dictionary)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character wound found {item['num']} times")
    
    print("--- End report ---")

def sort_on(sorted):
    return sorted["num"]

def dictionary_to_sorted_list(num_chars_dictionary):
    ordered_list = []
    for ch in num_chars_dictionary:
        ordered_list.append({"char": ch, "num": num_chars_dictionary[ch]})
    ordered_list.sort(reverse = True, key = sort_on)
    return ordered_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_dictionary(text):
    characters = {}
    for character in text:
        lowered = character.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

main()

#github.com/gnomeocracy/bookbot/books/frankenstein.txt