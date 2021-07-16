import json

# Loads the json file
f_in = open('dialogues_001.json')
multi_woz = json.loads(f_in)

f_out = open('out')
f.write(multi_woz)
