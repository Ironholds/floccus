import regexes
import re

"""
A generic function for getting the first match to a regular expression. Returns an empty string if there was no match.
"""
def generic_get(regex, row):
  match_result = re.search(regex, row)
  if(match_result is None):
    return ""
  return match_result.group(0)

"""
Extract a query from a row
"""
def get_query(row):
  return generic_get(regexes.get_query_regex, row)

"""
Extract the index names from a row (returns a list)
"""
def get_indexes(row):
  return generic_get(regexes.get_indexes, row).split(",")

"""
Extract a wiki from a row
"""

def get_wiki(row):
  return generic_get(regexes.get_wiki_regex, row)

"""
Extract a machine from a row
"""

def get_machine(row):
  return generic_get(regexes.get_machine_regex, row)


"""
Extract the elasticsearch processing time from a row. -1 is returned if it wasn't identifiable.
"""
def get_elasticsearch_time(row):
  result = generic_get(regexes.get_elasticsearch_time_regex, row)
  try:
    result = int(result)
  except:
    result = -1
  return result

"""
Extract the total processing time from a row. -1 is returned if it wasn't identifiable.
"""
def get_total_time(row):
  result = generic_get(regexes.get_total_time_regex, row)
  try:
    result = int(result)
  except:
    result = -1
  return result

"""
Extract the total result count from a row. -1 is returned if it wasn't identifiable
"""
def get_total_results_count(row):
  result = generic_get(regexes.get_total_results_regex, row)
  try:
    result = int(result)
  except:
    result = -1
  return result

"""
Extract the returned result count from a row. -1 is returned if it wasn't identifiable
"""
def get_returned_results_count(row):
  result = generic_get(regexes.get_returned_results_regex, row)
  try:
    result = int(result)
  except:
    result = -1
  return result

"""
Extract the offset of returned results. -1 is returned if it wasn't identifiable
"""
def get_result_offset(row):
  result = generic_get(regexes.get_result_offset_regex, row)
  try:
    result = int(result)
  except:
    result = -1
  return result

"""
Extract the machine that ran the request
"""
def get_machine(row):
  return generic_get(regexes.get_machine_regex, row)

"""
Extract the UUID of the request runner
"""
def get_executor(row):
  return generic_get(regexes.get_executor_regex, row)

"""
Extract the suggestion provided, if any
"""
def get_suggestion(row):
  return generic_get(regexes.get_suggestion_regex, row)
