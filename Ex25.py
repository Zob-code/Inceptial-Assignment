def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """"Prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



# you can run the file in the terminal using python command
#  open the python palette , then import the file name and then do the operations


sentence = "all good things happens to those who will"

print(break_words(sentence))
all_words = break_words(sentence)
print(sort_words(all_words))

print_first_word(all_words)
print_last_word(all_words)
