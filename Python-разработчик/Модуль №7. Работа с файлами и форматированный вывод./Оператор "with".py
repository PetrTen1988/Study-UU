class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        final_rslt = {}
        for name in self.file_names:
            with open(name) as file:
                list_of_words = []
                rslt = {}
                for line in file:
                    tmp_str = line.split(' ')
                    for words in tmp_str:
                        if words.endswith('\n'):
                            words = words[:-1]
                            list_of_words.append(words)
                        else:
                            list_of_words.append(words)

                    rslt[name] = list_of_words
                    final_rslt.update(rslt)
        return final_rslt



finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words()) # Все слова









# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего