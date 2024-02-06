# Recursive Web Crawler User Manual

## beginning the program
enter the program by calling src/crawler.py [URL] [OPTIONAL: Max Depth]
replace the brackets with the URL and a new max depth if wanted
with no new Max Depth, it defaults to 3
with no URL, program will give a brief usage message and refer to the User's manual

## When the program has started
After the program has been started, it will continue until all links in the range of the depth have all been visited,
program will display the URL it is on and any errors that have occured

## To quit
To stop the program early, simply press Ctrl+C in the terminal.

## Final message
When the program has finished running, it will display the total runtime and the number of unique links that were opened during the crawl.

## Common errors:
Starting URL is not absolute: This can cause the program to terminate early. To fix this, ensure that the starting URL is an absolute URL.
URL in page is no longer valid: This can cause the program to catch an error and continue.
Server runtime: The server may time out and cause the program to terminate early. To fix this, restart the server.