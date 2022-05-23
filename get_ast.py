import json
import pprint

from libs.recursives import Recursive

def do(data):
    for chd_key, chd_values in data.items():
        if chd_key == "type":
            print(chd_values)
        if chd_key == "children":
            for child in chd_values:
                do(child)




def main():
    with open("./self-made-datasets/4-abstracted-asts:github:jsonl:xz/64a68714c31d2bdc30fae3529bb0c998af9797c6.json", mode="r") as f:
        data = json.load(f)
    # pprint.pprint(data)
    do(data)

if __name__ == "__main__":
    main()
