import re
text= 'My home town is a big town'
pattern = 'town'
match_obj=re.search(pattern,text)
span =match_obj.span()
print(span)