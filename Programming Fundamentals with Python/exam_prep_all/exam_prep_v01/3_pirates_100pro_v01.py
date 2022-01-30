# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End

# https://judge.softuni.org/Contests/Practice/Index/2302#2


def disband_town(city, cities_wealth, cities_population):
    if cities_population[city] <= 0 or cities_wealth[city] <= 0:
        del cities_wealth[city]
        del cities_population[city]
        events_list.append(f"{city} has been wiped off the map!")
    return cities_wealth, cities_population


def check_negative(g):
    if g < 0:
        events_list.append(f"Gold added cannot be a negative number!")
        return True
    else:
        return False


def prewar_cities_state(city, population, gold, cities_wealth, cities_population):
    if check_negative(gold):
        pass
    else:
        if city in cities_wealth.keys():
            cities_wealth[city] += gold
            cities_population[city] += population
        else:
            cities_wealth[city] = gold
            cities_population[city] = population
        return cities_wealth, cities_population


def war_peace_events_func(command, cities_wealth, cities_population, do_what, city):  # same as prewar func but
    # with 'do_what' variable

    if city in cities_wealth.keys():
        if do_what == "Prosper":

            gold = int(command[2])
            #
            if not check_negative(gold):
                check_negative(gold)
                cities_wealth[city] += gold
                total_gold = cities_wealth[city]
                events_list.append(f"{gold} gold added to the city treasury. {city} now has {total_gold} gold.")
        elif do_what == "Plunder":

            population = int(command[2])
            gold = int(command[3])
            if not check_negative(gold):
                check_negative(gold)
                cities_wealth[city] -= gold
                cities_population[city] -= population
                events_list.append(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
            cities_wealth, cities_population = disband_town(city, cities_wealth, cities_population)
    return cities_wealth, cities_population


command = ''
# Events Dicts
events_list = []
statistics_list = []

# Events Variables
city = ''
population = 0
gold = 0

# State of cities dictionaries
cities_wealth = {}
cities_population = {}


sail = False
end = False
while not sail:
    command = input().split('||')
    if "Sail" in command:
        sail = True
        break
    else:
        city = command[0]
        population = int(command[1])
        gold = int(command[2])
    #
    cities_wealth, cities_population = prewar_cities_state(city, population, gold, cities_wealth, cities_population)



# A 'While' cycle to gather Events data:
while not end:
    command = input().split('=>')
    if "End" in command:
        end = True
        break
    else:
        # TODO: Check if war_peace function is appropriate for this purpose \/
        do_what = command[0]
        city = command[1]
        cities_wealth, cities_population = war_peace_events_func(command, cities_wealth, cities_population, do_what,
                                                                 city)

count = len(cities_wealth.keys())
for i in events_list:
    print(i, end='\n')
print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
# print(cities_wealth, cities_population)
for (key, value) in cities_wealth.items():
    city = key
    gold = cities_wealth[city]
    people = cities_population[city]
    print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")
# TODO: Create a function to finally print what's left on the map, or announce the total extermination:
#
# Printable function:
#

#
#
# print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
