import argparse

class Parser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__()
        self.add_argument("-u", type=str, help="The url to be fuzzed.", required=True)
        group = self.add_mutually_exclusive_group(required=True)
        group.add_argument("-p", type=str, help="Path containing a wordlist.")
        group.add_argument("-s", type=str, help="String containing substrings to be visited. The substrings are delimited by semiclon's.")
    
    def get_args(self):
        return self.parse_args()