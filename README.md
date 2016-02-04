# COMP-330-Project1
Project 1: Twitter Processing
My understanding of the assignment is that we are to write code with the following functionality:
Read through a tweet given in the code, not fed in by the user
Scan the tweet and pick out:
   Hashtags (#))
   Mentions (@)
   URLs     (http or https)
Count the number of hastags, mentions, and URLs (respectively) and store that information
Store the content of the hastags, mentions, and URLs (respectively) such that one is able to ask for the topic and receive it or ask if a word or phrase is a topic and be told yes or no
Furthermore, we are to write tests for our code to ensure that it works properly and to gain experience with unit testing
I chose to go about this by taking the tweet as a string parameter for a function called "Tweet_Scanner(tweet)" I then split the string at all spaces (' ') giving me a string array in which every
individual word is an array element
The funtion then scans and if any array element starts with a "#" it is stored as a hashtag, an "@" sign it is stored as a mention, or with "http" or "https" it is stored as a URL
Each element is also given a counter which keeps track of how many of each element in contained in any given tweet
We are also to write documentation for our code
Finally, we are to use Git to commit to our code daily to ensure both familiarity with Git and continual progress on the project
