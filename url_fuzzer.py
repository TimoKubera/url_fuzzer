import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", type=str, help="The url to be fuzzed.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-p", type=str, help="Path containing a wordlist.")
group.add_argument("-s", type=str, help="String containing substrings to be visited. The substrings are delimited by semiclon's.")
args = parser.parse_args()

wordlist = []
if args.p:
    with open(args.p) as f:
        for line in f:
            wordlist += line
elif args.s:
    wordlist = args.s.split(";")

try:
    for line in wordlist:
        url = args.u + "/" + line
        r = requests.get(url)
        if r.status_code < 400:
            print("The url is available: " + url)
except Exception as e:
    print(str(e))