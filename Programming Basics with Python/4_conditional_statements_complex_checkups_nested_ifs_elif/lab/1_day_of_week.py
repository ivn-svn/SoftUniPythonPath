weekday = int(input())
#
weekday1 = ['Day', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if weekday in range(1, 8):
    print(weekday1[weekday])
else:
    print('Error')