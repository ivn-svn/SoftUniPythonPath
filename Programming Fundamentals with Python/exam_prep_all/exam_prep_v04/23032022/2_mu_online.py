# https://judge.softuni.org/Contests/Practice/Index/2028#1
health = 100
bitcoins = 0
#
rooms = input().split("|")
counter = 0
for room in rooms:
    cmd = room.split(" ")[0]
    amount = int(room.split(" ")[1])
    if cmd == "potion":
        if health + amount > 100:
            amount = 100 - health
            health += amount
        else:
            health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif cmd == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        monster = cmd
        attack = amount
        health -= attack
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            room = rooms.index(room) + 1
            print(f"Best room: {room}")
            break
        else:
            print(f"You slayed {monster}.")

    counter += 1

if counter == len(rooms):
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")