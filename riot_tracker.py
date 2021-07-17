import requests
import json

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

    #MATCH V5 API
    
    def get_match_history(self, puuid, num_games):
        match_list = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count={num_games}&api_key={self.api_key}").json()
        return match_list

    def get_match(self, match_id):
        match_dict = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}").json()
        return match_dict
