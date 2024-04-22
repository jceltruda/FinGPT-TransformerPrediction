import jsonlines
import json


with open("../data/djia_stock_test_output.json", "r") as f:
    djia_test_output = json.load(f)
    print(len(djia_test_output))