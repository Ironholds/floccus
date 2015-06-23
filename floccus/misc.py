import datetime

"""
Construct the file path to a particular day's cirrus logs on stat1002. Uses yesterday if no date is specified.
"""
def get_filepath(date = None):
  if date is None:
    date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
  parsed_date = date.strftime("%Y%m%d")
  path = "/a/mw-log/archive/CirrusSearchRequests.log-" + parsed_date + ".gz"
  return path
