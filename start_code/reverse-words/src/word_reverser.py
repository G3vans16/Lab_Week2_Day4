def spinWords(string):
    words = string.split()
    new_word_list = []
    for word in words:
        if len(word) >= 5:
            reversed_word = word[::-1]
            new_word_list.append(reversed_word)
        else: new_word_list.append(word)
    new_string = ' '.join(new_word_list)
    return new_string