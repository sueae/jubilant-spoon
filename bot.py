import tweepy # for tweeting
import secrets # shhhh

# set auth variables
auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

# create a new api
api = tweepy.API(auth, wait_on_rate_limit=True)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_direct_message(self, status):

        author = status.author.screen_name
        api.send_direct_message(screen_name=author, text='response')

        return True

    def on_status(self, status):

        author = status.author.screen_name
        statusID = status.id

        print(status.text + "\n")

        api.update_status('response')
        api.send_direct_message(screen_name='my username', text='Just sent a Tweet')

        return True

    def on_data(self, status):
        print('Entered on_data()')
        print(status)

        return True

    def on_error(self, status_code):
        print("Error Code: " + str(status_code))
        if status_code == 420:
            return False
        else:
            return True

    def on_timeout(self):
        print('Timeout...')
        return True

# followed_accounts = ['account', 'account']
# followed_ids = []

# for account in followed_accounts:
    # followed_ids.append(str(api.get_user(screen_name=account).id))

if __name__ == '__main__':
    listener = MyStreamListener()
    auth = api.auth
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    stream = tweepy.Stream(auth, listener)
    # stream.filter(follow=followed_ids)