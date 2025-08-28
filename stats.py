def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def count_words(file_path):
    num_words = get_book_text(file_path).split()
    return len(num_words)

def count_characters(file_path):
    text = get_book_text(file_path).lower()
    dict_chars = {}
    for char in text:
        if char not in dict_chars:
            dict_chars[char] = 1
        else:
            dict_chars[char] += 1
    return dict_chars

def sort_dict(d):
    char_list = []
    for char in d:
        char_list.append({"char": char, "num": d[char]})
    char_list = sorted(char_list, key=lambda x: x["num"], reverse=True)
    return char_list