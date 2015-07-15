import datetime
import os.path
import csv
from collections import Counter

"""
Construct the file path to a particular day's cirrus logs on stat1002. Uses yesterday if no date is specified.
"""
def get_filepath(date = None):
  if date is None:
    date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
  parsed_date = date.strftime("%Y%m%d")
  path = "/a/mw-log/archive/CirrusSearchRequests.log-" + parsed_date + ".gz"
  return path


"""
Write out a counter
"""

def write_counter(counter, date, file):
  if(os.path.exists(file) == False):
    with open(file, "wb") as tsv_file:
      write_obj = csv.writer(tsv_file, delimiter = "\t")
      write_obj.writerow(["date","variable","value"])
  with open(file, "ab") as tsv_file:
    write_obj = csv.writer(tsv_file, delimiter = "\t")
    for entry in counter:
      write_obj.writerow([str(date), entry, counter[entry]])
