class TextAnalyzer:
    def __init__(self, input_path, output_path, ignored_path, min_word_len = 0, 
                 max_word_len = None , consec_words = 1, sorted = None):
        self.input_path = input_path
        self.output_path = output_path
        self.ignored_path = ignored_path
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len
        self.consec_words = consec_words
        self.sorted = sorted
    
    def analyze(self):
        with open(self.input_path, 'r') as input_file:
            input_file.read()