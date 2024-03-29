from Midterm1 import TextAnalyzer
import pytest

class TextAnalyzerTest:
    def setup_method(self):
        self.st = TextAnalyzer(r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_input.txt',
                               r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_ignore.txt',
                               r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test.json'
                               )

    def test_line_count(self):
        assert self.st.line_count() >= 0
        
        with pytest.raises (TypeError):
            self.st  = TextAnalyzer (r'C:\Users\Mojtaba\Downloads\Linux\rufus-4.4p.exe', 
                                     r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test_ignore.txt',
                                    r'C:\Mojo\Prog\Python\JSharif\Exercise 3\test.json'
                                    )
            self.st.line_count()
            
    
