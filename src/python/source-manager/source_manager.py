import requests

# Space Track: 
# https://www.space-track.org
# tim.ashton.la@gmail.com
# ekjwekrjw234keflkdef43

# Sample Query: https://www.space-track.org/basicspacedata/query/class/boxscore/format/json

class Utils():

    @staticmethod
    def parse_text(raw_text):
        # Parse text here.

        # TODO: I dont like this approach, research a better text parsing solution.
        lines = raw_text.splitlines()
        del lines[:5]

        for line in lines:
            print(line)

        return raw_text

class SourceManager:

    sources = [
        {
            "key": "jplh",
            "name": "JPL Horizons",
            "api_url": "https://ssd.jpl.nasa.gov/api/horizons.api",
            "api_docs": "URL"   
        },
    ]

    def __init__(self):
        self.format = "json"

    def get_data(self):

        # Example commands:
         # MB = Majpr Bodies
         # 499 = Mars

        params = {
            'format': self.format,
            'COMMAND': "499",
            'OBJ_DATA': 'YES',
            'MAKE_EPHEM': 'YES',
            'EPHEM_TYPE': 'OBSERVER',
            'CENTER': '500@399',
            'START_TIME': '2025-01-01',
            'STOP_TIME': '2025-01-03',
            'STEP_SIZE': '3h'
        }

        try:
            response = requests.get("https://ssd.jpl.nasa.gov/api/horizons.api", params=params)

            if response.status_code == 200:
                data = response.json()
            
                print(f"Source: {data["signature"]["source"]} v{data["signature"]["version"]}")

                # TODO: Trying to catch errors from Horizon, i.e. "incorrect units"
                # try:
                #     error = data["error"]
                #     print(f"Error prop: {error}")
                # except AttributeError as e:
                #     print(f"AttributeError: {e}")

                return Utils.parse_text(data["result"])

            else:
                print(f"API call failed with status code: {response.status_code}")
                print(f"Error message: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")