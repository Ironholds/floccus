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
  path = "/a/mw-log/archive/CirrusSearchRequests/CirrusSearchRequests.log-" + parsed_date + ".gz"
  return(path, str(date))

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

"""
Create a date range you can pythonically loop over to backfill datasets.
"""
def date_range(start_str, end_str):
  start = datetime.datetime.strptime(start_str, "%Y-%m-%d").date()
  end   = datetime.datetime.strptime(end_str, "%Y-%m-%d").date()
  step = datetime.timedelta(days=1)
  result = []
  while start <= end:
      result.append(start)
      start += step
  return result
