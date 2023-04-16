import textwrap

texts = "The textwrap module provides some convenience functions, as well as TextWrapper, the class that does all the work.If youre just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of TextWrapper for efficiency.Wraps the single paragraph in text (a string) so every line is at most width characters long. Returns a list of output lines, without final newlines. Optional keyword arguments correspond to the instance attributes of TextWrapper, documented below."

word = textwrap.TextWrapper(width=40)
new_word = word.wrap(text=texts)
for print_text in new_word:
    print(print_text)  # Wraps the text above to become more readable and attractive


