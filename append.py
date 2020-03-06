import tweepy
import yaml


def load_data():
    f = open("secrets.yaml")
    community = yaml.safe_load(f)
    process = community["bots"]
    return process


def append_profile(process):
    for x, y in process.items():
        auth = tweepy.OAuthHandler(y["CONSUMER_KEY"], y["CONSUMER_SECRET"])
        auth.set_access_token(y["ACCESS_TOKEN"], y["TOKEN_SECRET"])
        api = tweepy.API(auth)
        test = api.lookup_users(user_ids=[y["USER_ID"]])
        for user in test:
            print(user.description)
            api.update_profile(description="{} #TwitterBot".format(user.description))


def main():
    process = load_data()
    append_profile(process)


if __name__ == "__main__":
    main()
