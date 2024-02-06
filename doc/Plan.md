# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).
*   [ ] **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


### Instructions
    
* I will create a crawler function that will go through a URL and note other links in that page and go through all the URLS recursivly.
* The crawler will check a few things before it goes, it will ensure that the depth of the current url is greater than or equal to the max depth
* it will check if the URL is already in the set of visited links,
* it will check if the URL is valid
* once all checks were passed, the crawler function will continue,
* it will print the URL it visited with the appropriate number of spaces
* it will add the URL to the visited set
* then it will call its self with the next URL

* I will also need to create a users manual, this will include how to use the program, common errors and other notes of the program

* I will need to parse through the user input to ensure it is valid, and to check for maxDepth.

### This program

* This program will go through all links from a given website, then check all the links from those websites to a set depth
* This program will need to ensure that all URLs are valid, it will also need to check if the url has been visited.
* A good solution will not crash unexpectedly and it will parse through all data before it goes to that URL

* I already know how to
  * create a recursive function
  * parse through data and clean it 
  * validate user input
  * check if data is in a list

* I dont know how to
  * Use the new libraries
  * use a set, I assume it is almost the same as a list.
  
### Data

* The crawler fucntion will take in the URL it needs to check, the depth it is at, the maxDepth, and the set of visited sites.
* New URLs will be collected as the crawler goes

* The output will be a print message of the URL it is currently on, this will be tabbed according to the depth it is at.
* it will print a final message of the runtime and how many unique sites it visited.

### Algorithms

* this will need an algorithm to go through all the links recursivly.

## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.
*   [ ] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*

### crawler
purpose of function parameters are self documenting
bad input should raise an exception with proper exeption handeling according to the exception heierarchy
good input should cause the program to run with no errors

def crawl(URL, depth, maxdepth, visited)
  if depth valuse is greater than max depth return
  elif url in visited return
  elif url is invalid return
  print(space * depth) # space is defined as '    ' (four spaces)
  append visited (url)
  Visit URL with the requests library
  if an error occured
    print the exception raised
    return
  Scan for anchor tags with beautifulsoup
  check for errors again
  for each anchor tag
    check for an href attribute; if not exist, continue
    new_URL = string in the href attribute
    remove any fragments if neccessary
    if new_url is relative, make it absolute
    crawl(new_URL, depth+1, maxDepth, visited)
  finally: 
    print(time ran: nowTime - startTime, Unique sites visited: len(visited))

def main()

(takes sys args,)
if len sys args == 1
  print(usage
elif len sys args == 2
  maxDepth = 3
  arg 2 = URL
else
  arg 2 = URL & arg 3 = maxDepth

Depth = 0
visited = ([])
start time = time.time()
crawler(URL, Depth, maxDepth, visited)

## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.

I ran the program using the URL for wikipidea and it ran as expected.
I ran the program using the amazon URL and got an error because my connection timed out, this was expected.
Keyboard interupt works as expected, and it displays the correct messages when done.
I am able to change the maxDepth as expected


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab.
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.

I think my code is written quite well and it is easy to understand
I don't understand the server we are supposed to use to test the program. So none of my tests include that.
A bug would be easy to find because the code is so short and simple

I think that my documentation is easy to understand, I used plain english to plan the code.
I think anyone can look at this project with no knowlage of what it is and they would be able to use it because of the documentation

I think a new feature for this project would be easy to add because this project is already so simple

This program might not work if URLs formatting changes for whatever reason. But it would be an easy update to make.