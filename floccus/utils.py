"""
A generic function for getting the first match to a regular expression. Returns an empty string if there was no match.
"""
def generic_get(row, regex):
  match_result = re.search(regex, row)
  if(match_result is None):
    return ""
  return match_result.group(0)

"""
A generic function for checking whether a regular expression matched a row. Returns True or False
"""
def generic_check(row, regex):
  if(re.search(regex, row)):
    return True
  return False
