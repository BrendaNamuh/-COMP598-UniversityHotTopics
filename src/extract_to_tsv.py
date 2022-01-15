import argparse
import random
import csv
import json

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outfile', type=str, required=True)
parser.add_argument('json_file')
parser.add_argument('num_posts_to_output')
args = parser.parse_args()

# Global variables
lines = open(args.json_file,'r').readlines()


def to_tsv(num_tsv_lines):
    num = int(num_tsv_lines)
    if num > len(lines) : num =len(lines)
    selected_lines = random.sample(lines, num)

    with open(args.outfile,'w') as outfile:
        tsv_writer = csv.writer(outfile, delimiter='\t')
        tsv_writer.writerow(['Name', 'title','coding'])
        for line in selected_lines:
            line = json.loads(line)
            tsv_writer.writerow([line['data']['author_fullname'],line['data']['title']])







if __name__ == '__main__':
    to_tsv(args.num_posts_to_output)
