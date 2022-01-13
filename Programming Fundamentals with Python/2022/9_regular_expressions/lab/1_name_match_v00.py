import re 
# user_input = input()
user_input =  "Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett"

pattern = r"\b[A-Z][a-z]+\b\s\b[A-Z][a-z]+\b"
matches = re.findall(pattern, user_input)
print(" ".join(matches))