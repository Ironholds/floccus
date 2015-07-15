import re

"""
A regular expression for identifying if a row is valid in a trivial way - it checks for a valid timestamp. A row is
valid if it has one and only one timestamp. Used in check_valid (see checks.py)
"""
check_valid_regex = re.compile("^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

"""
A regular expression for identifying if a row returned 0 total results. Used in check_zero (see checks.py)
"""
check_zero_regex = re.compile("Found 0 total results")

"""
A regular expression for extracting queries from rows. Used in get_query (see gets.py)
"""
get_query_regex = re.compile("(?<= search for ').*(?=' against .*wiki_content took)")

"""
A regular expression for checking whether a request came via the API.
"""
check_api_regex = re.compile("Requested via api\\.")

"""
A regular expression for checking whether a request came via the web interface.
"""
check_web_regex = re.compile("Requested via web\\.")

"""
A regular expression for identifying the time elasticsearch spent processing a request
"""
get_elasticsearch_time_regex = re.compile("(?<= and )\\d{1,}(?= Elasticsearch millis.)")

"""
A regular expression for identifying the total time taken to process and return a request
"""
get_total_time_regex = re.compile("(?<= took )\\d{1,}(?= millis and)")

"""
A regular expression for identifying whether a request was a prefix search request
"""
check_prefix_search_regex = re.compile(" prefix search for '")

"""
A regular expression for identifying whether a request was a full-text search request
"""
check_full_search_regex = re.compile(" full_text search for '")

"""
A regular expression for identifying and extracting the total results count
"""
get_total_results_regex = re.compile("(?<=Found )\\d{1,}(?= total results and)")

"""
A regular expression for identifying and extracting the returned results count
"""
get_returned_results_regex = re.compile("(?<= total results and returned )\\d{1,}(?= of them starting at )")

"""
A regular expression for identifying and extracting the results offset
"""
get_result_offset_regex = re.compile("(?<= of them starting at )\\d{1,}(?=.)")

"""
A regular expression for identifying and extracting the machine that ran the query
"""
get_machine_regex = re.compile("(?<=^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} )mw\\d{1,}")

"""
A regular expression for identifying and extracting the executor for the query
"""
get_executor_regex = re.compile("(?<=by executor)(.{16})(?=\.$)")
