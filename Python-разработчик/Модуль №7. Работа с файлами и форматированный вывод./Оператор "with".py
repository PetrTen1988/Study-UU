class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name) as file:
                list_of_words = []
                rslt = {}
                for line in file:
                    exclude = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    tmp_w = ''.join(ch for ch in line if ch not in exclude)
                    tmp_str = tmp_w.split(' ')
                    for words in tmp_str:
                        if words.endswith('\n'):
                            words = words[:-1]
                            list_of_words.append(words.lower())
                        else:
                            list_of_words.append(words.lower())

                    rslt[name] = list_of_words
                    all_words.update(rslt)
        return all_words

    def find(self, word):
        output = {}
        self.word = word
        wrd = word.lower()
        list_of_files = list(self.file_names)
        list_to_search = self.get_all_words()
        for name in list_of_files:
            tmp = {}
            tmp2 = {}
            if wrd in list_to_search[name]:
                for_dict = list(list_to_search[name])
                tmp[name] = for_dict.index(wrd) + 1
                output.update(tmp)
            else:
                tmp2[name] = (f'There is no "{wrd}" in file "{name}"')
                output.update(tmp2)
        return  output

    def count(self,word):
        output = {}
        self.word = word
        wrd = word.lower()
        list_of_files = list(self.file_names)
        list_to_search = self.get_all_words()
        for name in list_of_files:
            tmp = {}
            tmp2 = {}
            count = 0
            for elem in list_to_search[name]:
                if elem == wrd:
                    count += 1
                    tmp[name] = f'Word "{wrd}" was met in file "{name}" {count} times.'
                    output.update(tmp)
                else:
                    tmp2[name] = f'There is no word "{wrd}" in file "{name}".'
                    output.update(tmp2)
        return output



finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего







# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего