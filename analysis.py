import re
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def countFrequency():
    with open("tweets.txt", "r") as f:
        text = f.read()

        #Clean the data in the text file
        for char in '-.,\n':
            text = text.replace(char,' ')

        #Check for case sensitivity and split the lines into individual words
            text = text.lower()
            ls = text.split()

        #Count the 10 most frequent words using Counter() and print
        mostFrequent = Counter(ls).most_common(10)
        print("Top 10 Most Frequent Words: \n" + str(mostFrequent))
            
    
def countRTs():
    with open("tweets.txt", "r") as f:
        RT_count = 0
        #Iterate through the text file
        for line in f:
            #Match the content of the lines with the desired phrase and add to a counter
            if "b'RT @" in line:
                RT_count += 1
            else:
                RT_count = RT_count
        #Print the number of total retweets found in the file
        print("\nTotal Number of Retweets")
        print("The total number of retweets is " + str(RT_count))

def vaccineTweets():
    with open("tweets.txt", "r") as f:
        count = 0
        #Iterate through the text file
        for line in f:
            #Match the content of the lines with the desired phrase and add to a counter
            if "vaccine" in line:
                count += 1
            else:
                count = count
        #Print the number of total retweets found in the file
        print("\nVaccine Tweets")        
        print("The total number of tweets mentioning the COVID19 vaccine is " + str(count) + " out of 5000.")

def countHashtags():
    with open("tweets.txt", "r") as f:
        text = f.read()
        regex = "#(\w+)"
 
        # extracting the hashtags using regex
        hashtag_list = re.findall(regex, text)
                
                
        #Count the most frequent hashtags using Counter() and print all hashtags and frequency they occur
        mostFrequent = Counter(hashtag_list).most_common(3)
        print("\nMost Frequent Hashtags: \n" + str(mostFrequent))
    


def mostRTdAcct():
    with open("tweets.txt", "r") as f:
        text = f.read()
        regex = "@(\w+)"
 
        # extracting the hashtags using regex
        hashtag_list = re.findall(regex, text)
                
                
        #Count the most frequently RT'ed accounts using Counter() and print top 10 accounts and frequency of which they were retweeted
        mostFrequent = Counter(hashtag_list).most_common(10)
        print("\nMost Frequently Retweeted Accounts: \n" + str(mostFrequent))

def get_sentiment(sentence):
        try:
            analyzer = SentimentIntensityAnalyzer()
            vs = analyzer.polarity_scores(sentence)

            return(vs['compound'])

        except:
            return -1


def calculateSentimentScore():
    with open("tweets.txt", "r") as f:
        score = 0
        for line in f:
            score = score + get_sentiment(line)
        score = score/5000
    print("\nSentiment \nThe average sentiment score of all 5000 lines is " + str(score))

countFrequency()
countHashtags()
countRTs()
mostRTdAcct()
vaccineTweets()
calculateSentimentScore()
        
