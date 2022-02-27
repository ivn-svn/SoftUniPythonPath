cmd = ''
endcycle = False
# Name variables
name = ''
username = ''
current_name = ''
new_name = ''
# Indexing
index = 0
item_idx = 0
collection = 0
count_blacklisted = 0
lost_list = 0
# Lists of people:
lost_list = 0
blacklist_list = 0
# possible commands:
blacklist = 'Blacklist'
error = 'Error'
change = 'Change'


def idxval(idx, col):
    if idx >= 0 and idx < col:
        return True
    else:
        return False


friends_list = input().split(', ')
collection = len(friends_list)

while cmd.lower() != 'report':
    cmd = input()
    cmd_split = cmd.split(' ')
    if blacklist in cmd_split:
        current_name = cmd_split[1]
        if current_name in friends_list:
            item_idx = friends_list.index(current_name)
            friends_list[item_idx] = 'Blacklisted'
            print(f"{current_name} was blacklisted.")
            blacklist_list += 1
        elif current_name not in friends_list:
            print(f"{current_name} was not found.")
    elif error in cmd_split:
        item_idx = int(cmd_split[1])
        if item_idx <= collection - 1:
            current_name = friends_list[item_idx]
            if current_name in friends_list and current_name != 'Blacklisted' and current_name != 'Lost' and idxval(
                    item_idx, collection):
                friends_list[item_idx] = 'Lost'
                print(f"{current_name} was lost due to an error.")
                lost_list += 1
            elif current_name not in friends_list:
                print(f"{current_name} was not found.")
    elif change in cmd_split:
        item_idx = int(cmd_split[1])
        if item_idx <= collection - 1:
            current_name = friends_list[item_idx]
            new_name = cmd_split[2]
            if current_name in friends_list and idxval(item_idx,
                                                       collection) and current_name != 'Blacklisted' and current_name != 'Lost':
                friends_list[item_idx] = new_name
                print(f"{current_name} changed his username to {new_name}.")

print(f"Blacklisted names: {blacklist_list}")
print(f"Lost names: {lost_list}")
print(' '.join(friends_list))
