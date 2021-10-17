def scan(input):
    lexicon = {
        "north": "direction",
        "south": "direction",
        "east": "direction",
        "west": "direction",
        "down": "direction",
        "up": "direction",
        "left": "direction",
        "right": "direction",
        "back": "direction",
        "go": "verb",
        "stop": "verb",
        "kill": "verb",
        "eat": "verb",
        "the": "stop",
        "in": "stop",
        "of": "stop",
        "from": "stop",
        "at": "stop",
        "it": "stop",
        "bear": "noun",
        "princess": "noun",
        "cabinet": "noun",
        "space": "noun",
        "honey": "noun"
    }
    sentence = []
    words = input.split()

    for word in words:
        if word.isdigit():
            word = int(word)
            sentence.append(("number", word))
        elif word in lexicon.keys():
            sentence.append((lexicon[word.lower()], word))
        else:
            sentence.append(("error", word))

    return sentence
