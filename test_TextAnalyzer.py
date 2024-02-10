from Midterm1 import TextAnalyzer

class TextAnalyzerTest:
    def setup_method(self):
        self.st = TextAnalyzer(r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_input.txt',
                               r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_ignore.txt',
                               r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test.json'
                               )

    def test_line_count(self):
        assert self.st.line_count() >= 0
    
