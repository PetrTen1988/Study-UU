def single_rout_word(root_word, *other_words):
    same_words = []

    for elem in other_words:

        if elem.lower().__contains__(root_word.lower()) or root_word.lower().__contains__(elem.lower()):
            same_words.append(elem)
    print(same_words)

single_rout_word('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

print('---------------------------------')

single_rout_word('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')