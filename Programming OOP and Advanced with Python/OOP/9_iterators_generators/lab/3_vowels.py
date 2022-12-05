class vowels:
    def __init__(self, input_text):
        self.vowels_l = ['a', 'e', 'i', 'u', 'y', 'o']
        self.input_text = list(input_text)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try: 
            while self.index < len(self.input_text):
                
                if self.input_text[self.index] != None:
                    if self.input_text[self.index].lower() in self.vowels_l:
                        value_to_return = self.input_text[self.index]
                        self.index += 1 
                        return value_to_return
            
            raise StopIteration
        except:
            pass

# my_string = vowels("Abcedifuty0o")
my_string = vowels("A\ne\ni\nu\ny\no\n")
for char in my_string:
    print(char)

