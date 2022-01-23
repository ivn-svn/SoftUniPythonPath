while True:
    txt = input()
    output1 = [int(s) for s in txt.split() if s.isdigit()]
    for x in output1:
        print(x, end=' ')