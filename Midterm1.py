class TextAnalyzer:
    def __init__(self, input_path, output_path, ignored_path, min_word_len = 0, 
                 max_word_len = None , consec_words = 1, sorted = None):
        self._input_path = input_path
        self._output_path = output_path
        self._ignored_path = ignored_path
        self._min_word_len = min_word_len
        self._max_word_len = max_word_len
        self._consec_words = consec_words
        self._sorted = sorted
    
    def line_count(self):
        with open(self._input_path, 'r') as input_file:
            return len(input_file.readlines())
        
    def sentence_count(self):
        num_sentence = 0
        with open(self._input_path, 'r') as input_file:
            for line in input_file:
                num_sentence += line.count('.')
                num_sentence += line.count('!')
                num_sentence += line.count('?')
        return num_sentence

    def word_counter(self):
        word_count = 0
        with open(self._input_path, 'r') as input_file , open(self._ignored_path, 'r') as ignore_file:
            split_input = input_file.read().split()
            split_ignore = ignore_file.read().split()
            for word in split_input:
                if word.strip('?!.,') not in split_ignore:
                    word_count +=1
        return word_count


    def consec_words_counter(self):
        if self._consec_words == 1:
            return self.word_counter()
        with open(self._input_path, 'r') as input_file , open(self._ignored_path, 'r') as ignore_file:
            split_input = input_file.read().split()
            split_ignore = ignore_file.read().split()
            for ignored_word in split_ignore:
                while ignored_word in split_input:
                    split_input.remove(ignored_word)
            split_input_punc_removed = []
            for element in split_input:
                split_input_punc_removed.append(element.strip('?!.,\():;'))
            consec_list = [split_input_punc_removed[i:i + self._consec_words] for i in range(0, len(split_input_punc_removed))]
            output_dict = {}
            for phrase in consec_list:
                output_dict[" ".join(phrase)] = " ".join(split_input_punc_removed).count(" ".join(phrase))
            if self._sorted == 'Asc':
                return dict(sorted(output_dict.items(), key=lambda item: item[1]))
            elif self._sorted == 'Desc':
                 return dict(sorted(output_dict.items(), key=lambda item: item[1] , reverse= True))
            return output_dict





test = TextAnalyzer(r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_input.txt' , 'D:\\' ,
                    r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_ignore.txt'  , consec_words = 2 , sorted= 'Asc')

print(test.consec_words_counter())
