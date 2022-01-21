import re 
user_input  = input()
pattern = r"\+359[-]2{1}[-]\d{3}[-]\d{4}\b|\+359[\s]2{1}[\s]\d{3}[\s]\d{4}\b"
matches = re.findall(pattern, user_input)
print(" ".join(matches))