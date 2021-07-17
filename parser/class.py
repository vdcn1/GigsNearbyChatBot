import json
import sys
# Loads the json file
f_in = open('dialogues_001.json', 'r')
multi_woz = json.loads(f_in.read())

orig_stdout = sys.stdout

with open('dataset1.csv', 'w') as f:
    sys.stdout = f

    print("ActiveIntent,Utterance")
    for line in multi_woz:
        if 'attraction' in line["services"]:
            for turn in line["turns"]:
                for frame in turn["frames"]:
                    if 'attraction' in frame["service"]:
                        if 'state' in frame:
                            if 'active_intent' in frame['state']:
                                if frame['state']['active_intent'] != 'NONE':
                                    print(frame['state']['active_intent'], end=',')
                                    if turn['speaker'] == 'USER':
                                        print('"{}"'.format(turn['utterance']))
    sys.stdout = orig_stdout
