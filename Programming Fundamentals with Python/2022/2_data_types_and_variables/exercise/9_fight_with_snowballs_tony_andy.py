n = int(input()) # integer, the number of snowballs being made by Tony and Andi.
snowball_value = 0
value_formulae = 0
#
snowball_weight_list = []
snowball_time_list = []
snowball_quality_list = []
value_formulae_list = [] # a list to hold the results from the snowball_formula function generated in the for loop
ints_list = [] # a list to hold the results of sorting out the value_formulae_list list.
def snowball_formula(a, b, c):
        value_formulae = (a / b) ** c
        return int(value_formulae)
for snowballs in range(1, n + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    # function to fill in the list of value_formulae
    value_formulae = snowball_formula(snowball_weight, snowball_time, snowball_quality)
    # Dicts \/
    snowball_weight_list.append(snowball_weight)
    snowball_time_list.append(snowball_time)
    snowball_quality_list.append(snowball_quality)
    value_formulae_list.append(value_formulae)
#
ints_list = sorted(value_formulae_list, reverse=True)
snowball_value = ints_list[0] # take the element on top of the list (largest int from the list)
lists_iterable = value_formulae_list.index(snowball_value)
#
snowball_weight = snowball_weight_list[lists_iterable]
snowball_time = snowball_time_list[lists_iterable]
snowball_quality = snowball_quality_list[lists_iterable]
#
print(f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})")