import tweepy # for tweeting
import secrets # shhhh

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_direct_message(self, status):

        author = status.author.screen_name
        api.send_direct_message(user=author, text='response')

        return True

    def on_status(self, status):

        author = status.author.screen_name
        statusID = status.id

        print(status.text + "\n")

        api.update_status('response')
        api.send_direct_message(user=author, text='Just sent a Tweet')

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

def main():
    global api
    try:
        # set auth variables
        auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
        # auth.secure = True
        auth.set_access_token(secrets.access_token, secrets.access_token_secret)

        # create a new api
        api = tweepy.API(auth, wait_on_rate_limit=True)

        print(api.me().name)
        listener = MyStreamListener()
        stream = tweepy.Stream(auth, listener)
        stream.userstream()

    except BaseException as e:
        print("Error in main()", e)