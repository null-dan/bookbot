def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(characters_dict)

    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document')
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found '{item['num']}' times")

    print('--- End report ---')
    
    # print(f"Number of words: {num_words}")
    # print("Character counts:")
    # for k, v in sorted_dict.items():
    #     print(f"{k}: {v}")

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    characters_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters_dict:
            characters_dict[lowered] += 1
        else:
            characters_dict[lowered] = 1
    return characters_dict


# def get_sorted_dict(characters_dict):
#     sorted_dict = dict((sorted(characters_dict.items())))
#     return sorted_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(characters_dict):
    sorted_list = []
    for ch in characters_dict:
        sorted_list.append({"char": ch, "num": characters_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()


