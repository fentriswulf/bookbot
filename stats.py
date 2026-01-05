def get_num_words(texts):
    words = texts.split()
    return len(words)

def count_characters(text):
    counts = {}
    for ch in text:
       ch = ch.lower()
       if ch not in counts:
           counts[ch] = 1
       else: counts[ch] = counts[ch] + 1 
    return counts

def sort_letters(counts):
    result = []
    for ch in counts:
        result.append({"char": ch, "num": counts[ch]})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(d):
    return d["num"]
