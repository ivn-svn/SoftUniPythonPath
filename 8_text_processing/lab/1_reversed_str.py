text = input()
while text != "end":
    text = input()
    text_reversed = ""
    for ch in reversed(text):
        text_reversed += ch
    print(text + " = " + text_reversed)