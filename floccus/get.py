"""
Extract a query from a row
"""
def get_query(row):
  return generic_get(get_query_regex, row)
