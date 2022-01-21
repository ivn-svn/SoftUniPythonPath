# SoftUni Parking
# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. 
# It can only receive users' data, but it doesn't know what to do with it. 

# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# 	•	"register {username} {license_plate_number}":
# 	•	The system only supports one car per user at the moment, so if a user tries to register another 
# license plate using the same username, the system should print: "ERROR: already registered with plate number
#  {license_plate_number}"
# 	•	If the check above passes successfully, the user should be registered, so the system should print: 
#  "{username} registered {license_plate_number} successfully"
# 	•	"unregister {username}":
# 	•	If the user is not present in the database, the system should print: "ERROR: user {username} not found"
# 	•	If the check above passes successfully, the system should print: "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license plates in the format: 
# 	•	"{username} => {license_plate_number}"
# Input
# 	•	First line: n - number of commands - integer
# 	•	Next n lines: commands in one of the two possible formats:
# 	•	Register: "register {username} {license_plate_number}"
# 	•	Unregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.
#
n = int(input())
user_input = ''
username_plate_db = {}
for i in range(0, n):
    user_input = input()
    user_input = user_input.split(' ')
    if 'unregister' in user_input:
        username = user_input[1]
        if username in username_plate_db.keys():
            del username_plate_db[username]
            print(f'{username} unregistered successfully')
        elif username not in username_plate_db.keys():
            print(f'ERROR: user {username} not found')

    elif 'register' in user_input:
        action = user_input[0]
        username = user_input[1]
        plate_number = user_input[2]
        if plate_number in username_plate_db.values():
            print(f'ERROR: already registered with plate number {plate_number}')
        elif plate_number not in username_plate_db.values():
            username_plate_db[username] = plate_number
            print(f'{username} registered {plate_number} successfully')
for (keys, values) in username_plate_db.items():
    print(f'{keys} => {values}')