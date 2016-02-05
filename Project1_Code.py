import unittest
import sys

def Main():
    
    tweet1 = "Excuses never look good on people #youpickedme #bambam"
    #print("Tweet1: ",tweet1)
    tweet2 = "Straight from @ufc President @danawhite: @JonnyBones vs. @dc_mma 2 is happening."
    #print("Tweet2: ",tweet2)
    tweet3 = ("@usantidoping  showing up early before my first cup of coffee! Good talk! #cleanfighter")
    #print("Tweet3: ",tweet3)
    tweet4 = ("filler")
    #print("Tweet4: ",tweet4)
    tweet5 = ("filler")
    #print("Tweet5: ",tweet5)
    Tweet_Scanner(tweet1)
    #Tweet_Scanner(tweet2)
    #Tweet_Scanner(tweet3)
    #Tweet_Scanner(tweet4)


def Tweet_Scanner(tweet):
    topic = []
    mention = []
    referenced_URL = []
    topicCounter = 0
    mentionCounter = 0
    referenced_URLCounter = 0
    charCounter = list(tweet)
    tweet_ary = tweet.split(' ')
    for n in tweet_ary:
        if n.find('#') == 0:
            topic.append(n)
            topicCounter += 1
        if n.find('@') == 0:
            mention.append(n)
            mentionCounter += 1
        if 'http' in n or 'https' in n:
            referenced_URL.append(n)
            referenced_URLCounter += 1
    print('Topics: ', topic)
    print (topicCounter)
    print("Mentions: ", mention)
    print(mentionCounter)
    print("Referenced URLs: ", referenced_URL)
    print(referenced_URLCounter)
    print('\n')
        
class Test(unittest.TestCase): 
    def Test_Tweet_Scanner(self):
        self.assertEqual(Tweet_Scanner(tweet1).topic, '#youpickedme')
        self.assertEqual(Tweet_Scanner(tweet1).topic, '#bambam')
unittest.main()
    
Main()
