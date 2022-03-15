# https://judge.softuni.org/Contests/Practice/Index/2303#0.
n = int(input())
hero_name = ''
healthpoints = 0
manapoinnts = 0
cmd = ''
spell_name = ''
hero_mp = {}
hero_hp = {}


def CastSpell(spl, hmp):
    h_name = spl[1]
    mp_needed = int(spl[2])
    spell_n = spl[3]
    if mp_needed <= hmp[h_name]:
        hmp[h_name] -= mp_needed
        print(f"{h_name} has successfully cast {spell_n} and now has {hmp[h_name]} MP!")
    else:
        print(f"{h_name} does not have enough MP to cast {spell_n}!")
    return hmp


def TakeDamage(spl, hhp, hmp):
    h_name = spl[1]
    damage = int(spl[2])
    attacker = spl[3]
    if (hhp[h_name] - damage) > 0:
        hhp[h_name] -= damage
        print(f"{h_name} was hit for {damage} HP by {attacker} and now has {hhp[h_name]} HP left!")
    elif (hhp[h_name] - damage) <= 0:
        hhp[h_name] = 0
        hhp.pop(h_name)
        hmp.pop(h_name)
        print(f"{h_name} has been killed by {attacker}!")
    return hhp, hmp


def Recharge(spl, hmp):
    h_name = spl[1]
    amount = int(spl[2])
    if (hmp[h_name] + amount >= 200):
        amount = 200 - hmp[h_name]
        hmp[h_name] = 200
        print(f"{h_name} recharged for {amount} MP!")
    elif (hmp[h_name] + amount < 200):
        hmp[h_name] += amount
        print(f"{h_name} recharged for {amount} MP!")
    return hmp


def Heal(spl, hhp):
    h_name = spl[1]
    amount = int(spl[2])
    if (hhp[h_name] + amount >= 100):
        amount = 100 - hhp[h_name]
        hhp[h_name] = 100
        print(f"{h_name} healed for {amount} HP!")
    elif (hhp[h_name] + amount < 100):
        hhp[h_name] += amount
        print(f"{h_name} healed for {amount} HP!")
    return hhp


for i in range(0, n):
    user_input = input().split(' ')
    hero_name = user_input[0]
    healthpoints = int(user_input[1])
    manapoinnts = int(user_input[2])
    # Fill the dicts:
    hero_hp[hero_name] = healthpoints
    hero_mp[hero_name] = manapoinnts
cmd = ''
while cmd != 'End':
    cmd = input()
    split = cmd.split(" - ")
    if "CastSpell" in split:
        hero_mp = CastSpell(split, hero_mp)
    elif "TakeDamage" in split:
        hero_hp, hero_mp = TakeDamage(split, hero_hp, hero_mp)
    elif "Recharge" in split:
        hero_mp = Recharge(split, hero_mp)
    elif "Heal" in split:
        hero_hp = Heal(split, hero_hp)

for (k, v) in hero_hp.items():
    hp = hero_hp[k]
    mp = hero_mp[k]
    print(f"{k}\n  HP: {hp}\n  MP: {mp}")
