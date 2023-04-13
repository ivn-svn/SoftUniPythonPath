from typing import List
from .player import Player
from .supply import Supply

class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Player) -> str:
        added_players = []
        for player in players:
            if player in self.players:
                continue
            if player.name in [p.name for p in self.players]:
                raise Exception(f"Name {player.name} is already used!")
            self.players.append(player)
            added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies: Supply) -> None:
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str) -> str:
        valid_sustenance_types = ["Food", "Drink"]
        if sustenance_type not in valid_sustenance_types:
            return

        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            return

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        supply = next((s for s in self.supplies[::-1] if isinstance(s, globals()[sustenance_type])), None)
        if not supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina += supply.energy
        if player.stamina > 100:
            player.stamina = 100
        self.supplies.remove(supply)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        first_player = next((p for p in self.players if p.name == first_player_name), None)
        second_player = next((p for p in self.players if p.name == second_player_name), None)
        
        if not first_player or not second_player:
            return

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\nPlayer {second_player_name} does not have enough stamina."
        elif first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        attacker, defender = (first_player, second_player) if first_player.stamina < second_player.stamina else (second_player, first_player)

        damage = attacker.stamina // 2
        defender.stamina -= damage
        if defender.stamina <= 0:
            defender.stamina = 0
            return f"Winner: {attacker.name}"

        attacker, defender = defender, attacker
        damage = attacker.stamina // 2
        defender.stamina -= damage
        if defender.stamina <= 0:
            defender.stamina = 0
            return f"Winner: {attacker.name}"

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player_name}"
        else:
            return f"Winner: {second_player_name}"

