#!/usr/bin/python3  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

from bs4 import BeautifulSoup  	  	  
from urllib.parse import urlparse, urljoin, urldefrag  	  	  
import requests  	  	  
import sys  	  	  
import time  	  	  


def crawl(url, depth, maxDepth, visited):
    if depth >= maxDepth:
        return

    visited.append(url)
    print(f"Depth {depth}: {url}")

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")

        if href is not None:
            nextUrl = urljoin(url, href)

            if nextUrl not in visited:
                crawl(nextUrl, depth + 1, maxDepth, visited)


if __name__ == "__main__":

    ## If no arguments are given...
    if len(sys.argv) < 2:
        print("Please enter a URL to begin this program, refer to ../doc/Manual.md for more details", file=sys.stderr)
        exit(0)
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        maxDepth = 3
    else:
        url = sys.argv[1]
        maxDepth = int(sys.argv[2])

    if not urlparse(url).netloc:
        print("The URL entered is not an absolute URL. Please enter an absolute URL.", file=sys.stderr)
        exit(0)

    visited = []
    startTime = time.time()
    depth = 0

    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{'s' if maxDepth != 1 else ''}")

    try:
        crawl(url, depth, maxDepth, visited)
    except KeyboardInterrupt:
        print("Crawling interrupted by user.")
