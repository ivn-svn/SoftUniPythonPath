from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace

class HorseRaceApp:
    def __init__(self):
        self.__horses = []
        self.__jockeys = []
        self.__horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        # Check if the horse with the same name already exists
        for horse in self.__horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        # Add the horse based on its type
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
        else:
            return

        self.__horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        # Check if the jockey with the same name already exists
        for jockey in self.__jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.__jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        # Check if the horse race of the same type already exists
        for race in self.__horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.__horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        # Find the jockey
        jockey = None
        for j in self.__jockeys:
            if j.name == jockey_name:
                jockey = j
                break

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        # Find the last available horse of the given type
        horse = None
        for h in reversed(self.__horses):
            if type(h).__name__ == horse_type and not h.is_taken:
                horse = h
                break

        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        # Check if the jockey already has a horse
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        # Assign the horse to the jockey
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        # Find the horse race
        race = None
        for r in self.__horse_races:
            if r.race_type == race_type:
                race = r
                break

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        # Find the jockey
        jockey = None
        for j in self.__jockeys:
            if j.name == jockey_name:
                jockey = j
                break

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        # Check if the jockey has a horse
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        # Check if the jockey has already been added to the horse race
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        # Add the jockey to the horse race
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        # Find the horse race
        race = None
        for r in self.__horse_races:
            if r.race_type == race_type:
                race = r
                break

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        # Check if there are at least two participants
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        # Find the winner
        winner_jockey = max(race.jockeys, key=lambda jockey: jockey.horse.speed)
        winner_speed = winner_jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {winner_speed}km/h is {winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}."
