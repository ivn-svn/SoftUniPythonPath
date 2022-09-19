# There is a party at SoftUni. Many guests are invited, and there are two types of them: 
# 
# Regular and VIP. When a guest comes, 
# check if they exist on any of the two reservation lists.
#
# On the first line, you will receive the number of guests – N. 
# 
# On the following N lines, you will be receiving 
# their reservation codes. 
# 
# All reservation codes are 8 characters long, and all VIP numbers will start with a digit. 
# Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
#
# In the end, print the number of guests who did not come to the party and their reservation numbers:
# •	The VIP guests must be first.
# •	Both the VIP and the Regular guests must be sorted in ascending order.
import re 

n = int(input())

uninvited = set()
invited = set()

vip_guests = set()
reg_guests = set()

vip_regx = "(\b[0-9]\w{7})"
reg_regx = "(\b[A-z]\w{7})"
#
uninvited = set()
for i in range(0, n): 
    invited.add(input()) 

cmd = input()

while cmd != "end":
    find_vip = re.findall(vip_regx, cmd)
    find_reg = re.findall(reg_regx, cmd)

    if find_vip:
        if find_vip in invited:
            vip_guests.add(find_vip)
    if find_reg:
        if find_reg in invited:
            reg_guests.add(find_reg)

    cmd = input()

for invitee in invited:
    if invitee in vip_guests and invitee in reg_guests:
        pass
    else:
        uninvited.add(invitee)


print(len(uninvited))

for unwanted in uninvited:
    print(unwanted)