from riot_tracker import RiotTracker
from player_stats import PlayerStats
from openpyxl import Workbook
import os

def parse_match(match_dict, puuid):
    #finding what index the player is in the participant array
 
    puuid_list = match_dict["metadata"]["participants"]

    for x in range (0, 10):
        if (puuid_list[x] == puuid):
            idx = x
            break
    
    player_dict = match_dict["info"]["participants"][idx]

    #parsing role

    if player_dict["teamPosition"] == "UTILITY":
        role = "SUPPORT"
    else:
        role = player_dict["teamPosition"]

    champion = player_dict["championName"]
    victory = player_dict["win"]
    kills = player_dict["kills"]
    deaths = player_dict["deaths"]
    assists = player_dict["assists"]
    kda = (kills + assists) / deaths

    #parsing time

    time_milliseconds = match_dict["info"]["gameDuration"] #time in MILLISECONDS MUST CONVERT

    time_minutes = int((time_milliseconds / (1000 * 60) ) % 60)
    time_seconds = int(time_milliseconds / 1000) % 60
    time_string = f"{time_minutes}:{time_seconds}"

    cs_total = player_dict["totalMinionsKilled"] + player_dict["neutralMinionsKilled"]
    cs_per_min = round(cs_total / (time_milliseconds / 60000), 1) #rounded to one decimal place
    champ_physical_damage = player_dict["physicalDamageDealtToChampions"]
    champ_magic_damage = player_dict["magicDamageDealtToChampions"]
    gold = player_dict["goldEarned"]

    #creating PlayerStats object for easy management of spreadsheet

    player_stats = PlayerStats(role, champion, victory, kills, deaths, assists, kda, time_milliseconds, time_string, cs_total, cs_per_min, champ_physical_damage, champ_magic_damage, gold)

    return player_stats
    
def create_spreadsheet(sheet):
    pass

def update_spreadsheet(sheet):
    pass

def main():
    api_key = input("Enter Riot API Key (refer to *github link* if you don't know how to get this): ")
    name = input("Enter summoner name: ")
    file_name = input("Enter file name (if you don't have an existing one, we will automatically create one with this name): ")

    riot_tracker = RiotTracker(api_key)

    puuid = riot_tracker.get_puuid(name)

    match_list = riot_tracker.get_match_history(puuid, 10)

    file_list = os.listdir(".")
    print(file_list)

    fileFound = False

    for file in file_list:
        if file == file_name:
            fileFound = True

    workbook = Workbook()
    sheet = workbook.active

    if (fileFound == False):
        create_spreadsheet(sheet)
    else:
        update_spreadsheet(sheet)
    


if __name__ == "__main__":
    main()
