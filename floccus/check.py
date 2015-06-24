"""
Check whether a row returned zero results or not.
"""
def check_zero(row):
  return generic_check(check_zero_regex, row)

"""
Check whether a row is valid or not.
"""
def check_valid(row):
  return generic_check(check_valid_regex, row)

"""
Check whether a request came from the API.
"""
def check_api(row):
  return generic_check(check_api_regex, row)

"""
Check whether a request came from the web interface.
"""
def check_web(row):
  return generic_check(check_web_regex, row)

"""
Check whether a request was a prefix search request
"""
def check_prefix_search(row):
  return generic_check(check_prefix_search_regex, row)

"""
Check whether a request was a full text request
"""
def check_full_search(row):
  return generic_check(check_full_search_regex, row)
