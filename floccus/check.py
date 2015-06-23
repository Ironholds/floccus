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
