import os
import glob
import pandas as pd


def combiner():
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    return combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
