### DEPENDENCIES ###
import tweepy
import datetime
#
##### SET NAME OF DATABASE FILES ###
FILE_NAME = 'last_seen.txt'  ### This is the file that stores the ID no of the most recently recieved tweet
### BOT SPECIFIC KEYS ### Twitter APP ID: xxxxxxxx
consumer_key = 'xxx'  # API key
consumer_secret = 'xxX'  # API key secret
key =  'xxx' # Access Token
secret = 'xxx'    # Access Token Secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)       # LOGIN
auth.set_access_token(key, secret)                              # LOGIN
api = tweepy.API(auth, wait_on_rate_limit=True, timeout=6)          ### Here we set a timeout
#             ** END OF SETUP STAGE **
##################################################################################################

#get timeline mentions
tweets = api.mentions_timeline()            # note it comes in reverse chronological order, repeated below with variables, so this for testing is now commented out
print(tweets[0].text)                           # so [0] is latest tweet, .text is the text content only

### GET the inbound tweets, print to terminal the message recieved
### This reads the last tweet seen id no. into text file ###
def read_last_seen(FILE_NAME):      # READING             # THIS GETS CALLED BY REPLY()
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())        # reading the last id
    file_read.close()
    return last_seen_id                 # return the last seen id
### This saves the last tweet seen id no. into file ###
def store_last_seen(FILE_NAME, last_seen_id):       # WRITING last seen text to the file so it doesn't repeat       # THIS GETS CALLED BY REPLY()
    file_write = open(FILE_NAME, 'w')     # write clears last id no
    file_write.write(str(last_seen_id))   # writes new id into its place
    file_write.close()
    return

## THIS CONTROLS OUR CRITICAL TWEET WHICH IS A REPLY TO ANY INBOUND TWEET
def reply(FILE_NAME, readableTime):
    receivedtweets = api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
    for tweet in reversed(receivedtweets):      #if '@' in tweet.full_text.lower():           # so only replying if at'd                                           
      try:
        print("Received Tweet with ID: ", str(tweet.id)+ ' ----> ' + tweet.full_text)      
        api.update_status("Hallo "+ "@" + tweet.user.screen_name + " "+ "response received and works " + readableTime, tweet.id)      # HOW TO REPLY TO A TWEET
        print("debugging: try for reply() has reached marker 1")
        store_last_seen(FILE_NAME, tweet.id) # send two variables to this function which writes them down
        print("debugging: try for reply() has reached marker 2")
        status = api.get_status(tweet.id)
        favorited = status.favorited
        if favorited == True:
            print("The authenticated user has retweeted the tweet.") 
        else: 
            print("The authenticated user has not retweeted the tweet.")
            api.create_favorite(tweet.id)                  # Its going to favourite the tweet...
        # api.destroy_favorite(tweet.id)          ## I found to unfavourite it first solved so many bugs
        
        print("debugging: try for reply() has reached marker 3 ***")
        # status = api.get_status(tweet.id) don't repeat this as its an api call and mentioned above (line 47)
        retweeted = status.retweeted
        if retweeted == True:
            print("The authenticated user has retweeted the tweet.") 
        else: 
            print("The authenticated user has not retweeted the tweet.") 
            api.retweet(tweet.id)                          # It's going to retweet the tweet...
        #api.unretweet(tweet.id)                 ## I found to untweet it first solved so many bugs
        
        print("debugging: try for reply() has reached marker 4 ****")
      except:
        print("an error occured in the try statement for reply() ?")

        
        # Here we do something INTERESTING
def api_call(Tweet):       # THIS GETS CALLED BY REPLY(), and the tweet we are responding to is passed in
  try:
    botResponse = "blank"
    pass
  except Exception:
    pass
  finally:    # this block is always executed
    print("This chunk will always execute regardless of try working or not, do something cool")
  return botResponse

def max_tweet_size(botResponse):  # THIS CAN GET CALLED BY REPLY() and ensures the tweet is under size, obv change botResponce = " to tweet.full_text
  botResponse = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223333333333333333333333333333333333333333333333333333333333333333333333444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777788888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999000000000000000000000000000000000000000000000000"
  print(len(botResponse))
  if len(botResponse) > 280:           # 280 characters is the max, might need to adjust for additional text added to tweet later
    botResponse = botResponse[:270]  # cut the message to 230 characters before the hello and timestamp is added (longest hello is 9 characters, timestamp is about 36), just aim to ensure no errors
    print ("//", botResponse) 
    print (len(botResponse)) # This is now cut to 280 max length
  return botResponse

#while True:     # Permament Loop, with a pause for 15 secs ::::   NO LOOP
now = datetime.datetime.now()         ## https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python
print("Current date and time: ")
readableTime = (now.strftime('%Y-%m-%d %H:%M:%S'))
print (readableTime)

reply(FILE_NAME, readableTime)

# time.sleep(15)