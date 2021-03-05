# TwitterBotTemplate
Python/Tweepy: Twitter Bot REPLY Template: receivedtweets = api.mentions_timeline

You might need to: pip install tweepy

Any Python 3x should work

I aim to make 50 bots which response to questions, so the reply() function does the actual reply, then Fav, then retweet
(I put these into if statements to check if they had already been RT'd etc, because the api is otherwise unreliable IMO)

Other functions here are read_last_seen() / store_last seen() , these just ensure you dont repetitively respond to the same question every time it runs.
max_tweet_size() will cut the tweet down if above 280 chars

api_call() is set so that I can call a different API to the twitter api, here is where I will make each bot different


If you wish to copy this and get stuck, then the code originally came from: https://www.youtube.com/watch?v=ewq-91-e2fw&t=1s




