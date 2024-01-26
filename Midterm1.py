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
    
    def _line_count(self):
        with open(self._input_path, 'r') as input_file:
            return len(input_file.readlines())
        
    def _sentence_count(self):
        num_sentence = 0
        with open(self._input_path, 'r') as input_file:
            for line in input_file:
                num_sentence += line.count('.')
                num_sentence += line.count('!')
                num_sentence += line.count('?')
        return num_sentence

    def _word_counter(self):
        word_count = 0
        with open(self._input_path, 'r') as input_file , open(self._ignored_path, 'r') as ignore_file:
            split_input = input_file.read().split()
            split_ignore = ignore_file.read().split()
            for word in split_input:
                if word.strip('?!.,') not in split_ignore:
                    word_count +=1
        return word_count





test = TextAnalyzer(r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_input.txt' , 'D:\\' ,
                    r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_ignore.txt' )

print(test._word_counter())
