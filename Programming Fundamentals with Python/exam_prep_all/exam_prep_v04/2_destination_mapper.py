import re

user_input = input()

pattern = re.compile("=([A-Z]{1}[A-z]+)=|\/([A-Z]{1}[A-z]+)\/")
locations = []
travel_points = 0

matches = re.findall(pattern, user_input)
for match_ in matches:
    for match in match_:
        if match != '' and len(match) >= 3:
            travel_points += len(match)
            locations.append(match)
            # print(locations)

printable = ', '.join(locations)

print(f"Destinations: {printable}")
print(f"Travel Points: {travel_points}")