import re 

n = int(input())

uninvited = set()
invited = set()

vip_guests = set()
reg_guests = set()

vip_regx = r"(\b[0-9]\w{7})"
reg_regx = r"(\b[A-z]\w{7})"
#
uninvited = set()
for i in range(0, n): 
    invited.add(input()) 

cmd = input()

while cmd != "END":
    find_vip = re.findall(vip_regx, cmd)
    find_reg = re.findall(reg_regx, cmd)

    if find_vip:
        if find_vip[0] in invited:
            vip_guests.add(find_vip[0])
    if find_reg:
        if find_reg[0] in invited:
            reg_guests.add(find_reg[0])

    cmd = input()

for invitee in invited:
    if invitee in vip_guests or invitee in reg_guests:
        pass
    else:
        uninvited.add(invitee)


print(len(uninvited))
newuninvited = []

for j in uninvited:
    newuninvited.append(j)

newuninvited = newuninvited.sort()

for unwanted in newuninvited:
    if unwanted:
        print(unwanted)