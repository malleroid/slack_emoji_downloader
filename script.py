import json
import requests


def main():
    targets = load_json()
    download_emoji(targets)


def load_json():
    file = open('./emoji.json', 'r')
    data = json.load(file)

    return data['emoji']


def download_emoji(target_array):
    for target in target_array:
        response = requests.get(target['url']).content

        with open('./tmp/' + target['name'] + '.png', 'wb') as f:
            f.write(response)


if __name__ == "__main__":
    main()
