
import os
import json
dir_path = os.path.dirname(os.path.abspath(__file__))

# database
from tierDB import *
db = tierDB()

# def countTiers(value):
#     tierResults = []
#     r = db.find("item", values_list[0])
#     print(r)
    



# read values
with open("./static/values.json", 'r') as f:
    values = json.load(f) 

# print('values', values)
values_list = []
tiers = ["D", "C", "B", "A", "S"]

for value in values:
    print(value['name'])
    values_list.append(value["name"])
    tot = 0
    for score, tier in enumerate(tiers):
        c = db.countTier(value['name'], tier)
        # print(r)
        print('    ', tier, c, c*(score+1))
        tot+=c*(score+1)
    print('    Score = ', tot)
    print('    Avg,  = ', tot/5)

# countTiers(values_list[0])


