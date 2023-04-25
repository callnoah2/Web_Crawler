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
hit control c "^c" to exit the program early

## Final message
When finished, the program will give the runtime and how many unique links it has opened.

## Common errors:
Starting URL is not absolute
    this causes the program to end early, to fix this, modify the URL to be absolute
URL in page is no longer valid
    This causes the program to catch an error and continue
Server Runtime,
    the server may time out and case the program to end early, to fix this, restart the server