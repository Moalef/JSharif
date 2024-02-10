import json
import tkinter as tk
from tkinter.filedialog import askopenfilename , asksaveasfile , askdirectory


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
                word_stripped = word.strip('?!.,')
                if self._max_word_len:
                    if word_stripped not in split_ignore and len(word_stripped)>= self._min_word_len and len(word_stripped)<= self._max_word_len:
                        word_count +=1
                        continue
                if word_stripped not in split_ignore and len(word_stripped)>= self._min_word_len:
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


    def longest_words(self):
        with open(self._input_path, 'r') as input_file , open(self._ignored_path, 'r') as ignore_file:
            split_input = input_file.read().split()
            split_ignore = ignore_file.read().split()
            lengths_dict = {}
            for word in split_input:
                if word.strip('?!.,') not in lengths_dict.keys() and word not in split_ignore:
                    lengths_dict[word.strip('?!.,')] = len(word)
        return dict(sorted(lengths_dict.items(), key=lambda item: item[1] , reverse= True))

            

    def ignored_words(self):
        with open(self._ignored_path, 'r') as ignore_file:
            split_input = ignore_file.read().split()
        return split_input


    def avg_number_of_characters(self):
        with open(self._input_path, 'r') as input_file , open(self._ignored_path, 'r') as ignore_file:
            split_input = input_file.read().split()
            split_ignore = ignore_file.read().split()
            lengths_list = []
            for word in split_input:
                if word not in split_ignore:
                    lengths_list.append(len(word))
        return sum(lengths_list)/len(lengths_list)


    def create_output(self):
        final_output_dict = {}
        final_output_dict['Number of Lines'] = self.line_count()
        final_output_dict['Number of Sentences'] = self.sentence_count()
        final_output_dict['Number of Words'] = self.word_counter()
        final_output_dict['Number of occurrences of consecutive words'] = self.consec_words_counter()
        final_output_dict['Longest Words List'] = self.longest_words()
        final_output_dict['Ignored Words List'] = self.ignored_words()
        final_output_dict['Average Words Length'] = self.avg_number_of_characters()

        with open(self._output_path, "w") as outfile:
            json.dump(final_output_dict, outfile)



if __name__ == '__main__':
        
    window = tk.Tk()
    window.title("Text Analyzer")
    window.geometry("700x700") 


    def open_input_file():
        
        global filepath_input
        filepath_input = askopenfilename (filetypes=[ ('text files', '*.txt')])
        if not filepath_input:
            return
        status_input.config(text = f"received - {filepath_input}")


    def open_ignore_file():
        
        global filepath_ignore
        filepath_ignore = askopenfilename (filetypes=[ ('text files', '*.txt')])
        if not filepath_ignore:
            return
        status_ignore.config(text = f"received - {filepath_input}")

    def save_output():
        global filepath_output
        filepath_output = asksaveasfile(defaultextension=".json",filetypes=[("JSON Files","*.json")])
        status_output.config(text = "Received")


    def run():
        try:
            obj = TextAnalyzer(filepath_input, filepath_output.name, filepath_ignore, min_word_len_ent.get(),
                            max_word_len_ent.get(), consec_words_ent.get(), order.get())
            obj.create_output()
            status_run.config(text = "Done!")

        except Exception as e:
            print(e)
            status_run.config(text = f"Error {e}")





    status_input = tk.Label(text = "Input File")
    btn_open_input = tk.Button(window, text="Open Input Text File", command=open_input_file)


    status_ignore = tk.Label(text = "Ignore File")
    btn_open_ignore = tk.Button(window, text="Open Ignore Words File", command=open_ignore_file)

    btn_Save = tk.Button(window, text="Save Output File", command=save_output)
    status_output = tk.Label(text = "")

    min_word_len_ent = tk.IntVar(value=0)
    lbl_get_min_word = tk.Label(window, text = 'Enter Minimum Word Length (Default= 0)')
    min_word_len = tk.Entry(window, textvariable = min_word_len_ent )

    max_word_len_ent = tk.IntVar(value= None)
    lbl_get_max_word = tk.Label(window, text = 'Enter Maximum Word Length (Optional)')
    max_word_len = tk.Entry(window, textvariable = max_word_len_ent )

    consec_words_ent = tk.IntVar(value = 1)
    lbl_get_consec_word = tk.Label(window, text = 'Number of Consecutive Words to Count (Optional)')
    consec_words = tk.Entry(window, textvariable = consec_words_ent )

    lbl_radio = tk.Label(window, text = 'Choose Order (Optional)')
    order = tk.StringVar( value= None)
    r1 = tk.Radiobutton(window, text="Ascending", variable=order, value= 'Asc' )
    r2 = tk.Radiobutton(window, text="Descending", variable=order, value= 'Desc')

    btn_run = tk.Button(window, text="Analyze Text Now", command=run)
    status_run = tk.Label(text = "")



    btn_open_input.grid(row=0, column=0, sticky="ew", padx=5, pady=0)
    status_input.grid(row=0, column=1, sticky="ew" , padx=5, pady=0)
    btn_open_ignore.grid(row=1, column=0, sticky="ew" , padx=5, pady=0)
    status_ignore.grid(row=1, column=1, sticky="ew" , padx=5, pady=0)
    btn_Save.grid(row=2, column=0, sticky="ew", padx=5, pady=15)
    status_output.grid(row=2, column=1, sticky="ew" ,padx=5, pady=0)
    lbl_get_min_word.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    min_word_len.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
    lbl_get_max_word.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
    max_word_len.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
    lbl_get_consec_word.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
    consec_words.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
    lbl_radio.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
    r1.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
    r2.grid(row=8, column=0, sticky="ew", padx=5, pady=5)
    btn_run.grid(row=9, column=0, sticky="ew", padx=5, pady=5)
    status_run.grid(row=10, column=0, sticky="ew", padx=5, pady=5)

    window.mainloop()
