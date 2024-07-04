def  single_root_words(root_words, *other_words):
    same_words = []
    for words in other_words:
        if root_words.lower() in words.lower():
            same_words.append(words)
        elif words.upper() in root_words.upper():
            same_words.append(words)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
