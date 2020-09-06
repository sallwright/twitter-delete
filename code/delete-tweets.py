import json, tweepy, os
from datetime import datetime, timedelta

def get_api():

    consumer_key = os.environ.get('API_KEY')
    consumer_secret = os.environ.get('API_SECRET_TOKEN')
    access_token_key = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    return tweepy.API(auth)

def get_delete_from_date(delete_from_date):     
    if delete_from_date:
        delete_from_date = datetime.strptime(delete_from_date, '%Y-%m-%d')
    else:
        delete_from_date = datetime.now() - timedelta(days=365)
    
    return delete_from_date

def run_delete(delete_from_date=False,exclude_favourited=True):

    api = get_api()
    delete_from_date_formatted = get_delete_from_date(delete_from_date)

    for status in tweepy.Cursor(api.user_timeline).items():
        if status.created_at <= delete_from_date_formatted:
            if exclude_favourited:    
                if not status.favorited:
                    print("Tweet text: {}".format(status.text))
                    print("Tweet created: {}".format(status.created_at))
                    api.destroy_status(status.id)
            else:
                print("Tweet text: {}".format(status.text))
                print("Tweet created: {}".format(status.created_at))
                api.destroy_status(status.id)

if __name__ == "__main__":
    run_delete("2017-01-01")