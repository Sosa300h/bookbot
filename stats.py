def get_book_text(file):
    with open (file) as f:
        file_contents = f.read()
    words = file_contents.split()
    number = len(words)
    stringnumber = (f"{number} words found in the document")
    return number

def character_count(file):
    with open (file) as f:
        text = f.read()
    lowered = text.lower()
    words = list(lowered)
    letter_count = {}
    for i in words:
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1
    return letter_count

def list_of_dicts(file):
    dictionary = character_count(file)
    list_added = []
    for i in dictionary:
        list_added.append({"char": i, "num": dictionary[i]})
    list_added.sort(reverse=True, key=sort_on)
    return list_added

def sort_on(dict):
    return dict["num"]
