import json
import requests

file = open('./emoji.json', 'r')
data = json.load(file)

targets = data['emoji']

for emoji in targets:
    response = requests.get(emoji['url']).content

    with open('./tmp/' + emoji['name'] + '.png', 'wb') as f:
        f.write(response)
