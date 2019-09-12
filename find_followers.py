import time
import tweepy
import csv

consumer_key = "TXyXtFqgMD4Kf2aEbrzPs0zLO"
consumer_secret = "qobBILMZY9unjcgg9plgbhigICmm6tylBZ2pB5GlRE2bnDxDRd"
access_key = "1041292564345712640-wf08zTbDUkharn24sATb6LQDqdzlp8"
access_secret = "VOvhaZtMZYqu1D79Zek3gU6iYAJYaikRYCLS5fgkNXOPs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

def get_followers(user_name):
    """
    get a list of all followers of a twitter account
    :param user_name: twitter username without '@' symbol
    :return: list of usernames without '@' symbol
    """
    api = tweepy.API(auth)
    followers = []
    for page in tweepy.Cursor(api.followers, screen_name=user_name, wait_on_rate_limit=True,count=200).pages():
        try:
            followers.extend(page)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    return followers


def save_followers_to_csv(user_name, data):
    """
    saves json data to csv
    :param data: data recieved from twitter
    :return: None
    """
    HEADERS = ["name", "screen_name", "description", "followers_count", "followers_count",
               'friends_count', "listed_count", "favourites_count", "created_at"]
    with open(user_name + "_followers.csv", 'w',encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(HEADERS)
        for profile_data in data:
            profile = []
            for header in HEADERS:
                profile.append(profile_data._json[header])
            csv_writer.writerow(profile)


if __name__ == '__main__':
    followers = get_followers("leroyjv")
    save_followers_to_csv("leroyjv", followers)