d = {'Woodii': '7.00', 'Welwitschia': '7.00', 'Arnoldii': '0.00'}
print(list(d.values()).count('7.00'))
print(sorted(d.items(), key=lambda x: x[1], reverse=True))