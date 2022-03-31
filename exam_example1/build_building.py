# ‘Investor {number} gave us {money_given}.’
# Where {money_given} is formatted two digits after the decimal point.
# If at some point we have enough money to build our building we should stop taking investors money and print:
#
# ‘We will manage to build it. Start now! Extra money - {extra_money}.”
# If we didn’t collect enough capital after all investors’ money we must print:
#
# ‘Project can not start. We need {money} more.’
budget = float(input())
m = float(input()) # initial capital
n = int(input()) # number of investors
money = float(input()) # the money the investor has given us
# Output
# If you have enough money at some point
#     • „We will manage to build it. Start now! Extra money - {extra_money}.”
# Where extra_money is the money which has left, formatted two digits after decimal point
# If you do not have enough money after all investors have invested print:
#     • „Project can not start. We need {difference} more.”
# Where {money} is the money you need to reach the planned budget, formatted two digits after decimal point.
#
#
'''while m <= budget:'''
for i in n:
    m += money
if m < budget:
    money = budget - money
    print(f'Project can not start. We need {money} more.')
else:
    extra_money = budget - money
    print(f'We will manage to build it. Start now! Extra money - {extra_money}.')