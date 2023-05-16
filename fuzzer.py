import requests

class Fuzzer():
    def __init__(self, args):
        self.args = args
        self.wordlist = []

    def fuzz(self):
        if self.args.p:
            with open(self.args.p) as f:
                for line in f:
                    self.wordlist.append(line.replace("\n", ""))
        elif self.args.s:
            self.wordlist = args.s.split(";")

        try:
            for line in self.wordlist:
                url = self.args.u + "/" + line
                r = requests.get(url)
                if r.status_code < 400:
                    print("+ The following URL exists: " + url)
                else:
                    print("- The following URL does not exist: " + url)
        except Exception as e:
            print(str(e))