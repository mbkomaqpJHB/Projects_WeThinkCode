
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)
'''check what split(d,t) does'''
# print(split(",.? ", "These are indeed interesting, an obvious understatement, times. What say you?"))


def convert_to_word_list(text):
    text = text.lower() #small letters
    words = split(" ,.?;", text) #remove special in characters
    txt = list(filter(lambda x: x != "", words)) #removes empty spaces
    return txt
    

def words_longer_than(length, text):    
    words = convert_to_word_list(text)
    selected_words = []
    for i in words:
        if len(i) > length:
            selected_words.append(i) #add words that are greater than len to the new list        
    return selected_words


def words_lengths_map(text):
    words = convert_to_word_list(text)    
    word_len = list(map(lambda i: len(i), words)) #returns the length of each word in our list
    word_dict = {i:word_len.count(i) for i in sorted(word_len)} #counts the number of matching words/length in the list
    return word_dict
    

def letters_count_map(text):
    text = text.lower()
    alpha = map(chr, range(97, 123))
    alpha_count = {i:text.count(i) for i in alpha}
    return alpha_count
    

def most_used_character(text):
    text = text.lower()
    if text >= "a" and text <= "z":
        letter_count = letters_count_map(text)
        return max(letter_count, key = letter_count.get)  
    else:
        return None
    

# does not run this code in unittest
if __name__ == '__main__':
    words = convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
    print(words,"\n")

    text = input("Enter text: ")
    words = words_longer_than(10, text)
    # words = words_longer_than(10, 'These are indeed interesting, an obvious understatement, times. What say you?')
    print(words,"\n")

    word_lengths = words_lengths_map(text)
    # word_lengths = words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
    print(word_lengths,"\n")

    char_count = letters_count_map(text)
    # char_count = letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
    print(char_count,"\n")

    # popular_char = most_used_character('123')
    popular_char = most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
    print(popular_char)