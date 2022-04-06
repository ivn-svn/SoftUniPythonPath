capacity = int(input())
user_count = 0
cmd = input()

user_sent_received = dict()

def remove_user(user_sent_received, user):
    del user_sent_received[user]
    return user_sent_received

while cmd != "Statistics":
    line = cmd.split("=")

    if line[0] == "Add":
        user = line[1]
        sent = int(line[2])
        received = int(line[3])
        if user not in user_sent_received.keys():
            user_sent_received[user] = []
            user_sent_received[user].append(sent)
            user_sent_received[user].append(received)

    elif line[0] == "Message":
        sender = line[1]
        receiver = line[2]
        if sender and receiver in user_sent_received.keys():
            user_sent_received[sender][0] += 1
            user_sent_received[receiver][1] += 1
            if sum(user_sent_received[sender]) >= capacity:
                user = sender
                user_sent_received = remove_user(user_sent_received, user)
                print(f"{sender} reached the capacity!")
            elif sum(user_sent_received[receiver]) >= capacity:
                user = receiver
                user_sent_received = remove_user(user_sent_received, user)
                print(f"{receiver} reached the capacity!")



    elif line[0] == "Empty":
        username = line[1]
        if username == "All":
            for usr in user_sent_received.keys():
                del user_sent_received[usr]
        else:
            user_sent_received = remove_user(user_sent_received, user, capacity)
    cmd = input()
user_count = len(user_sent_received.keys())
print(f"Users count: {user_count}")
for (k,v) in user_sent_received.items():
    print(f"{k} - {sum(v)}")
