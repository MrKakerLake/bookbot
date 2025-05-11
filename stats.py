def num_words (text):
    words = text.split()
    return len(words)

def get_characters (text):
    lowercase = text.lower()
    characters = {}
    for character in lowercase:
        if character in characters:
            characters[character]+=1
        else:
            characters[character]=1
    return characters

def sorted_list (characters):
    result_list = []
    for character, count in characters.items():
        char_dict = {"char": character, "num": count}
        result_list.append(char_dict)
    def sort_on(dict):
        return dict["num"]
    result_list.sort(reverse=True, key=sort_on)
    return result_list