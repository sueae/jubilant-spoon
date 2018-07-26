import tweepy
import secrets
import json

# create an OAuthHandler instance
auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
# set access token from stored
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

# start using the API
api = tweepy.API(auth)

# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("Connection established")

    def on_disconnect(self,notice):
        print("Connection lost: ", notice)

    #def on_status(self, status):
        #print(status.text)

    def on_direct_message(self, status):
        print("Entered on_direct_message()")
        print(status.text)
        author = status.author.screen_name
        api.send_direct_message(user=author, text='response')

        return True

    def on_data(self, data):
        print("Entered on_data()")
        try:
            print(data.text)
            # Decode the JSON from Twitter
            datajson = json.loads(data)

            #grab the wanted data from the Tweet
            text = datajson['text']
            screen_name = datajson['user']['screen_name']
            tweet_id = datajson['id']
            print(text)
            print(screen_name)
            print(tweet_id)
            # created_at = parser.parse(datajson['created_at'])
            # coordinates = datajson['coordinates']

            #print out a message to the screen that we have collected a tweet
            # print("Tweet collected at " + str(created_at))
            #print datajson
            #insert the data into the MySQL database
            #store_data(created_at, text, screen_name, tweet_id, coordinates)

        except Exception as e:
            print("Failed on_data()", str(e))


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff.

# If the authentication was successful, you should
# see the name of the account print out
print("auth: ", api.me().name)

#myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, MyStreamListener())
myStream.userstream()

# myStream.filter(track=['facebook stock'])

# myStream.filter(follow=["2432479868"])