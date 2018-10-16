import urllib.request
import urllib.parse
import re


def search(q):
    query_string = urllib.parse.urlencode({"search_query": q})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results  # returns a list of video IDs
