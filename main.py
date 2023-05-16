from parser import Parser
from fuzzer import Fuzzer

parser = Parser()
args = parser.get_args()

fuzzer = Fuzzer(args)
fuzzer.fuzz()