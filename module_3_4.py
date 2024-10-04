

def  single_root_words(root_word,  *other_words):
    same_words = []

    root_word = root_word.lower()
    for i in other_words:
        if root_word in i.lower():
            same_words.append(i)
        if i.lower() in root_word:
            same_words.append(i)

    return same_words

resuit1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
resuit2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(resuit1)
print(resuit2)