# Да се напише програма, която чете парола (един ред с произволен текст), въведена от потребителя и
# проверява дали въведеното съвпада с фразата &quot;s3cr3t!P@ssw0rd&quot;. При съвпадение да се изведе
# &quot;Welcome&quot;. При несъвпадение да се изведе &quot;Wrong password!&quot;.
password = input(str())
if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")
