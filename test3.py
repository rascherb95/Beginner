import csv
import numpy as np
import pandas as pd


mailing_list = []






with open('mailinglist.csv', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        mailing_list.append(row)

print(mailing_list)
