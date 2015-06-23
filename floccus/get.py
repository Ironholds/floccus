"""
Extract a query from a row
"""
def get_query(row):
  return generic_get(get_query_regex, row)

"""
Extract the elasticsearch processing time from a row. -1 is returned if it wasn't identifiable.
"""
def get_elasticsearch_time(row):
  result = generic_get(get_elasticsearch_time_regex, row)
  try:
    result = int(result)
  except:
    result = -1
  return result

"""
Extract the total processing time from a row. -1 is returned if it wasn't identifiable.
"""
def get_total_time(row):
  result = generic_get(get_total_time_regex, row)
  try:
    result = int(result)
  except:
    result = -1
  return result
