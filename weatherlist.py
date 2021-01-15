#automatedweatherlist

import csv

# 1 import mailing_list from csv
Col1 = "Email"
Col2 = "City"
Col3 = "State"

mailing_list = {Col1:[], Col2:[], Col3:[]}
csvfile = csv.reader(open('mailing_list.csv','r'))
for row in csvfile:
  mailing_list[Col1].append(row(0))
  mailing_list[Col1].append(row(1))
  mailing_list[Col1].append(row(2))


# 2 assign mailing_list data to email, city and state vars
# 3 scheduler to mail everyday at noon
# 4 get api data using cit and state vars
# 5 mail to each person in mailing list
