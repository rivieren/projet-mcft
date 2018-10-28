import json

match_lower = {}

with open("match1.json") as json_file:  
    data = json.load(json_file)
    
    events = [data['events'][0]] #in order to keep only the first event

match_lower["gameid"]="0021500061"
match_lower["gamedate"] ="2015-11-04"
match_lower["events"]=events



with open('match_lower.txt', 'w') as outfile:  
    json.dump(match_lower, outfile)
