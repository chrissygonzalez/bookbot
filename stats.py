def count_words(text):
    return len(text.split())

def count_chars(text):
    count = {}
    for char in text:
        l = char.lower()
        if l in count:
            count[l] = count[l] + 1
        else:
            count[l] = 1
    return count

def sort_on(items):
    return items["count"]

def get_sorted_char_dictionaries(dict):
    list = []
    for key in dict:
        list.append({"char": key, "count": dict[key]})

    list.sort(reverse=True, key=sort_on)
    return list