# Create a program that calculates the water needed to put out a "fire cell", based on the given information about its
# "fire level" and how much it gets affected by water.
#
# First, you will be given the level of fire inside the cell with the integer value of the cell,
# which represents the needed water to put out the fire.  They will be given in the following format:

# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire
# for each fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.

fire_cells = input().split('#')
water_supply = int(input())
effort = 0
cells = []
total_fire = 0
fire_values = []

def valid_yn(f_rang, f_val):
    if f_rang.lower() == "high" and 81 <= f_val <= 125:
        return True
    elif f_rang.lower() == "medium" and 51 <= f_val <= 80:
        return True
    elif f_rang.lower() == "low" and 1 <= f_val <= 50:
        return True


for cell in fire_cells:
    if water_supply >= 0:
        fire_range = cell.split(' = ')[0]
        fire_value = int(cell.split(' = ')[1])
        if valid_yn(fire_range, fire_value):
            cells.append(fire_value)
            effort += fire_value * 0.25
            total_fire += fire_value
            fire_values.append(f" - {fire_value}")
            water_supply -= fire_value
print("Cells:")
for fires in fire_values:
    print(fires)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
