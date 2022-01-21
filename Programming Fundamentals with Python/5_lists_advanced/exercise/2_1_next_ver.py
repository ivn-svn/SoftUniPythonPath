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
joinednodot = ''
next_ver = ''
next_verlist = ''
#
current_ver_list = current_ver.split('.')
# string to hold the joined values of ''.join(current_ver_list)
joinednodot = ''.join(current_ver_list)
# print(joinednodot)
next_ver = int(joinednodot) + 1
next_verlist = list(str(next_ver))
next_ver = '.'.join(next_verlist)
print(next_ver)
