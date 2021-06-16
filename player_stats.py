#DEFINITELY IMPLEMENT

# rank
# role
# champion
# result
# kills
# deaths
# assists
# kda
# cs total
# game time
# cs/min
# gold

#SUGGESTIONS

# gold income per min
# TOTAL stats(champs played total, champ stats, average kdas? etc... maybe on seperate page but same file if possible?

class PlayerStats:
    def __init__(self, role, champion, victory, kills, deaths, assists, kda, time_float, time_string, cs_total, cs_per_min, champ_physical_damage, champ_magic_damage, gold):
        self.role = role
        self.champion = champion
        self.victory = victory
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.kda = kda
        self.time_float = time_float
        self.time_string = time_string
        self.cs_total = cs_total
        self.cs_per_min = cs_per_min
        self.champ_physical_damage = champ_physical_damage
        self.champ_magic_damage = champ_magic_damage
        self.gold = gold

    def __repr__(self):
        return (
            f"Role: {self.role}\n"
            f"Champion: {self.champion}\n"
            f"Victory: {self.victory}\n"
            f"Kills: {self.kills}\n"
            f"Deaths: {self.deaths}\n"
            f"Assists: {self.assists}\n"
            f"KDA: {self.kda}\n"
            f"Time (milliseconds): {self.time_float}\n"
            f"Time (string): {self.time_string}\n"
            f"Total CS: {self.cs_total}\n"
            f"CS per min: {self.cs_per_min}\n"
            f"Total Physical Champion Damage: {self.champ_physical_damage}\n"
            f"Total Magic Champion Damage: {self.champ_magic_damage}\n"
            f"Gold: {self.gold}\n"
        )
        
        