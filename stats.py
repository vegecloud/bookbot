def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def dict_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def dict_char(dict_of_counts):
    dict_list = []
    for char in dict_of_counts:
        dict_list.append({"char": char, "num": dict_of_counts[char]})
    
    def sort_on(dict):
        return dict["num"]

    dict_list.sort(reverse=True, key=sort_on) # sort list by descending values
    return dict_list