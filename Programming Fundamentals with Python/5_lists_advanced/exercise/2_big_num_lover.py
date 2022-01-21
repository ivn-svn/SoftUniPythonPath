# You really like big numbers, so you always find a way to form one from numbers given to you
# You will receive a single line containing numbers separated by a single space. Form the biggest number possible
# from them by sorting them as strings.
datalist = input().split(' ')
datasort = sorted(datalist, reverse = True)
biggest = ''.join(datasort)
print(biggest)