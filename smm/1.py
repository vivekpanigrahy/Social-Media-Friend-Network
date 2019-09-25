import time
import tweepy
import csv
import random

consumer_key = "TXyXtFqgMD4Kf2aEbrzPs0zLO"
consumer_secret = "qobBILMZY9unjcgg9plgbhigICmm6tylBZ2pB5GlRE2bnDxDRd"
access_key = "1041292564345712640-wf08zTbDUkharn24sATb6LQDqdzlp8"
access_secret = "VOvhaZtMZYqu1D79Zek3gU6iYAJYaikRYCLS5fgkNXOPs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
# user_name1 = ["leroyjv"]
# user_name = "".join(user_name1)
user_name = "leroyjv"
print(user_name)


def get_followers(user_name):
    """
    get a list of all followers of a twitter account
    :param user_name: twitter username without '@' symbol
    :return: list of usernames without '@' symbol
    """
    api = tweepy.API(auth)
    followers = []
    for page in tweepy.Cursor(api.followers, screen_name=user_name, wait_on_rate_limit=True, count=200).pages():
        try:
            followers.extend(page)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)

    return followers


def save_followers_to_csv(data):
    """
    saves json data to csv
    :param data: data recieved from twitter
    :return: None
    """
    HEADERS = ["screen_name"]
    with open(user_name + "_followers.csv", 'w', encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(HEADERS)
        for profile_data in data:
            profile = []

            for header in HEADERS:
                profile.append(profile_data._json[header])
            csv_writer.writerow(profile)


def rng():
    # open the file and convert it to a list
    # generate a random number between 1 and length of the list
    # find next user by accessing that list by that random number
    # next_user = ""
    with open(user_name + "_followers.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        your_list = list(reader)
        randomnumber = random.randint(1, len(your_list))
        next_user = "".join(your_list[randomnumber])
        # print(type(next_user))
    return (next_user)


if __name__ == '__main__':
    i = 0
    while i < 2:
        followers = get_followers(user_name)
        save_followers_to_csv(followers)
        user_name = rng()
        print(user_name)
