import json

with open ('name.json', 'w') as file:
    json.dump({'name':'Johan'}, file)