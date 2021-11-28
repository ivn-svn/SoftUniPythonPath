username = str(input())
password = str(input())
data = str(input())
while data != password:
    data = input()
print(f"Welcome {username}!")