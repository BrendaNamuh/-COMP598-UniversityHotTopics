import requests
import argparse
import json

## Get arguments
parser = argparse.ArgumentParser()  # holds info
parser.add_argument('-o', '--outfile', type=str, required=True)  # tells how to parse
parser.add_argument('-s', '--subreddit', type=str, required=True)
args = parser.parse_args()  # parses

# Global Variables
url = 'https://www.reddit.com/r/' + args.subreddit + '/new.json?limit=100'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# Gets 100 newest post from subreddit
def get_newest_posts(subreddit):
    r = requests.get(url, headers=headers)  # get page object. Response stream?
    root_element = r.json()
    with open(args.outfile, 'w') as outfile:
        for i, post in enumerate(root_element['data']['children'][:100]):
            line = json.dumps(post)
            outfile.write(line + '\n')



def main():
    get_newest_posts(args.subreddit)


if __name__ == '__main__':
    main()
