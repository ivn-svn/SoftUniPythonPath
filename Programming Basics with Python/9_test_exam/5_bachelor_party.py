honorary = int(input())
# User Input
# guest_number_5plus = 0
# guest_number_5minus = 0
rest_sum = 0
covert = 0
cost_per_group = 0
guest_number_count = 0
#
command = str("The restaurant is full")
guest_number = 0
# get_command = ''
#while 1 < honorary < 4500:
#
while guest_number != command:
    try:
        guest_number = int(input())
    except:
        break
    if guest_number < 5:
        covert = 100
    elif guest_number >= 5:
        covert = 70
    guest_number_count += guest_number
    cost_per_group += (guest_number * covert)
    #
if cost_per_group < honorary:
    print(f"You have {guest_number_count} guests and {cost_per_group} leva income, but no singer.")
elif cost_per_group >= honorary:
    rest_sum = cost_per_group - honorary
    print(f"You have {guest_number_count} guests and {rest_sum} leva left.")
