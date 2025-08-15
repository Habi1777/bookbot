def count_words_in_string(s):
    word_list = s.split() # due to split using all whitespaces as the default seperator when the sep parameter is left blank, it will take care of splitting every word and special character into their own value
    return len(word_list)

def count_characters(s):
    characters = {}
    for char in s:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    return characters

def dictionary_to_sorted_list(x):
    """
    Returns:
        A list of dictionaries that have been sorted, the keys for the dictionary are "char" and "num"
    """
    converted_list = [{"char": char_key, "num": num_val} for char_key, num_val in x.items()] # using list comprehensions to one line the creation of a list, creation of new dictionaries, and appending the values 
    converted_list.sort(reverse=True, key=lambda d: d["num"])
    return converted_list