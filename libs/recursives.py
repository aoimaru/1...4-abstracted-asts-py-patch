import pprint
import json

class Recursive(object):
    @classmethod
    @staticmethod
    def do(data):
        for childs in data:
            if not childs["childlen"]:
                print("type: ", child["type"])
            for child in childs["childlen"]:
                cls.do(child)


