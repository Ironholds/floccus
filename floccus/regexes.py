import re

"""
A regular expression for identifying if a row is valid in a trivial way - it checks for a valid timestamp. A row is
valid if it has one and only one timestamp. Used in check_valid (see checks.py)
"""
check_valid_regex = re.compile("^\d{4}-\d{2}-\d{2}")

"""
A regular expression for identifying if a row returned 0 total results. Used in check_zero (see checks.py)
"""
check_zero_regex = re.compile("Found 0 total results")

"""
A regular expression for extracting queries from rows. Used in get_query (see gets.py)
"""
get_query_regex = re.compile("(?<= search for ').*(?=' against .*wiki_content took)")
