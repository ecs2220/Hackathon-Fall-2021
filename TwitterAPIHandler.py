import requests
import json
import datetime
from DataStructures import TweetAPIData

bearer_token_edwardsturt_app1 = "AAAAAAAAAAAAAAAAAAAAANJWHQEAAAAAMaM5vS7iAXBQNTIFWrd%2BozAxWEY%3D6oV0ao4YJQojl0becTMxhWXPHV9wz9IiLUhToGpz5PBtV30uCT"

params = {"tweet.fields": "text,author_id,created_at,public_metrics,entities,in_reply_to_user_id"}


def get_session():
    with requests.Session() as s:
        s.headers.update({"Authorization": "Bearer {}".format(bearer_token_edwardsturt_app1)})
        return s


session = get_session()


def get_list_of_tweet_api_data(tweet_file_data_list: list):
    global session
    to_return = []
    tweet_file_data_map = {}

    tweet_id_list = []
    for index in range(0, len(tweet_file_data_list)):
        tweet_file_data = tweet_file_data_list[index]
        tweet_file_data_map.update({tweet_file_data.get_tweet_id(): tweet_file_data})
        tweet_id_list.append(tweet_file_data.get_tweet_id())
    tweet_id_list_string = ",".join(tweet_id_list)

    params.update({"ids": tweet_id_list_string})
    params.update({"ids": "1252630938770649089,1243968198111789058"})
    response = session.get("https://api.twitter.com/labs/2/tweets", params=params)
    print(response.status_code)
    print(response.headers)
    print(response.text)
    twitter_json = json.loads(response.text)

    print(json.dumps(twitter_json, indent=2))
    data_array = twitter_json["data"]
    for tweet_data in data_array:
        tweet_id = tweet_data["id"]
        created_at = tweet_data["created_at"]
        epoch_time = convert_created_at_to_epoch_time(created_at)
        date_str = convert_created_at_to_date_str(created_at)
        content = tweet_data["text"]
        hashtags = get_hashtags_from_tweet_data(tweet_data)
        like_count = tweet_data["public_metrics"]["like_count"]
        retweet_count = tweet_data["public_metrics"]["retweet_count"]
        reply_count = tweet_data["public_metrics"]["reply_count"]
        user_id = tweet_data["author_id"]
        is_reply = is_a_reply(tweet_data)

        tweet_api_data = TweetAPIData(tweet_file_data_map.get(tweet_id), epoch_time, date_str, content,
                                      hashtags, like_count, retweet_count, reply_count, user_id,
                                      is_reply)
        to_return.append(tweet_api_data)
    return to_return


def is_a_reply(data):
    if data["in_reply_to_user_id"] is not None and data["in_reply_to_user_id"] != "":
        return False
    return True


def get_hashtags_from_tweet_data(data):
    to_return = []
    hashtag_entities = data["entities"]["hashtags"]
    for entity in hashtag_entities:
        to_return.append(entity["tag"])
    return to_return


def convert_created_at_to_epoch_time(time_str: str):
    dt = datetime.datetime.strptime(time_str + " UTC", "%Y-%m-%dT%H:%M%S.%fZ %Z")
    print(dt.now())
    return dt.timestamp() * 1000


def convert_created_at_to_date_str(time_str: str):
    dt = datetime.datetime.strptime(time_str + " UTC", "%Y-%m-%dT%H:%M%S.%fZ %Z")
    print(dt.strftime("%m-%d-%Y"))
    return dt.strftime("%m-%d-%Y")
