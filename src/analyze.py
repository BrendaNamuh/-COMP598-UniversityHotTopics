import pandas as pd
import argparse
import json
# Creates json file with the number of times each hot topic appears in the annotaed file

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outfile')
parser.add_argument('-i', '--coded_file', required=True)
args = parser.parse_args()

# "Hot Topics"
result = {'course-related': '0', 'food-related': '0', 'residence-related': '0', 'other': '0'}


def get_count(coded_file):
    df = pd.read_csv(coded_file, sep='\t', header=0)  # convert infile to dataframe
    count = df['coding'].value_counts()

    for category in list(result.keys()):
        letter = category[:1] # course-related -> c
        if letter in count.index:
            result[category] = int(count[letter])
    return result

def main():
    count_result = get_count(args.coded_file)
    if args.outfile:
        with open(args.outfile,'w') as outfile:
            json.dump(count_result,outfile)
    print(result)



if __name__ == '__main__':
    main()


