# You're fed up about changing the version of your software manually. ' \
#    'Instead, you will create a little script that will make it for you.
#
#
# You will be given a version as in this example: "1.3.4". You have to find the next version and print it ("1.3.5" from
# the example). The only rule is that the numbers cannot be greater than 9. If that happens, set the current number to 0
# and increase the number before it. For more clarification, see the examples. Note:
# there will be no case where the first number will get greater than 9
# Example
current_ver = input()
next_ver = ''
#
current_ver_list = current_ver.split('.')
for x in range(len(current_ver_list), 0, -1):
    if current_ver_list[x] == '9':
        current_ver_list[x] = '0'
        current_ver_list[x - 1] = str(int(current_ver_list[x - 1]) + 1)
    else:
        current_ver_list[x] = str(int(current_ver_list[x]) + 1)
        next_ver = ''.join(current_ver_list)
        break
print(next_ver)