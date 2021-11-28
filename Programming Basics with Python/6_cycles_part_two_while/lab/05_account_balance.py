transactions_count = int(input())
transactions_made = 0
account_balance = 0
while transactions_made < transactions_count:
    amount = float(input())
    if amount < 0:
        print('Invalid operation!')
        break
    transactions_made += 1
    account_balance += amount
    print(f'Increase: {amount:.2f}')
print(f'Total: {account_balance:.2f}')