import requests
import json

#print(json.dumps(match_list, indent=4, sort_keys=True))

#Prxd
#accountid: oCDXwBo6DGlaVluiTgAlqHMyGfX1Tc3JVHUDKe1okjq0MjH2pd92VRG7
#summmonerid: b9K4O2Kwtg2kI8ix_Hynqj8yPLW2Iaxn3M5tbA0noX0BZuW6
#puuid: r5GeRXmEQwup71kg0AWJguD5hGZxsd14FXjWJjBAIepRFmWm0yjC-WQwJXUgkyx34l1v8QdtjJ7gWg


#CHANGE TO F STRINGS BEFORE DEPLOYING

class RiotTracker:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_account_id(self, name):
        user_info = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + self.api_key).json()
        account_id =  user_info["accountId"]
        return account_id

    def get_summoner_id(self, name):
        user_info = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + self.api_key).json()
        summoner_id = user_info["id"]
        return summoner_id

    def get_puuid(self, name):
        user_info = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + self.api_key).json()
        puuid = user_info["puuid"]
        return puuid;

    #MATCH V4 API
    #LINK https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/oCDXwBo6DGlaVluiTgAlqHMyGfX1Tc3JVHUDKe1okjq0MjH2pd92VRG7?queue=420&api_key=RGAPI-dececa22-beb5-49cc-8328-ce88debcccd9
    
    def get_match_history(self, puuid, num_games):
        match_list = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count={num_games}&api_key={self.api_key}").json()
        print(match_list)
        return match_list

    def get_match(self, match_id):
        match_dict = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}").json()
        return match_dict
