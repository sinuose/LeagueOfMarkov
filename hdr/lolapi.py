import requests
import json

# Fetch all real-time data from the League Client

class LiveData():
    def __init__(self):
        self.allgamedata = self.GET_CurrentMatchData()

    def GET_CurrentMatchData():
        '''
        This fetchs all the game data every ping. This may not be useful...
        '''
        url = "https://127.0.0.1:2999/liveclientdata/allgamedata"
        try:
            response = requests.get(url)
            data = response.json()
            return data
        except requests.exceptions.RequestException:
            print("Game client not running or API not accessible.")
            return None
    

