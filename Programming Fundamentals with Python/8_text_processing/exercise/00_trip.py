# Now that you have planned out your tour, you are ready to go! Your next task is to mark all the points on the map that
# you are going to visit.
# You will be given a string representing some places on the map. You have to filter only the valid ones. A valid
# location is:
#     • Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
#     • After the first "=" or "/" there should be only letters (the first must be upper-case, other letters could be
# upper or lower-case)
#     • The letters must be at least 3
# Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.
# After you have matched all the valid locations, you have to calculate travel points. They are calculated by summing
# the lengths of all the valid destinations that you have found on the map.
# In the end, on the first line, print: "Destinations: {destinations joined by ', '}".
# On the second line, print "Travel Points: {travel_points}".
import re
user_input = input()
pattern = r"=([A-Z]{1}[A-z][A-z]+)=|\/([A-Z]{1}[A-z][A-z]+)\/"
lengths = []
matches = re.findall(pattern, user_input)
destinations = []
destinations_joined = ""
for match in matches:
    for m in match:
        if m:
            lengths.append(len(m))
            destinations.append(m)
            # print(match)
travel_points = sum(lengths)


destinations_joined = ", ".join(destinations)
print(f"Destinations: {destinations_joined}")
print(f"Travel Points: {travel_points}")