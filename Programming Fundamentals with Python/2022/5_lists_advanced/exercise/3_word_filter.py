input_text = input()
inputsplit = input_text.split(' ')
even_len_words = [print(x, end='\n') for x in inputsplit if len(x) % 2 == 0]
