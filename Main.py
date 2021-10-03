import pandas
import DataStructures
from DataStructures import ClaimOrNews
from DataStructures import TweetFileData
import TwitterAPIHandler


def get_tweet_file_data_list(filepath: str, claim_or_news: ClaimOrNews, list_of_tweet_ids):
    to_return = []
    df = pandas.read_csv(filepath)
    for index, row in df.iterrows():
        tweet_id = row["tweet_id"]
        if not list_of_tweet_ids.__contains__(tweet_id):
            continue
        if claim_or_news == ClaimOrNews.CLAIM:
            news_index = row["claim_id"]
        else:
            news_index = row["news_id"]
        real_or_fake = DataStructures.convert_str_to_real_or_fake(row["real_or_fake"])
        tweet_file_data = TweetFileData(news_index, tweet_id, claim_or_news, real_or_fake)
        to_return.append(tweet_file_data)
    return to_return


def get_list_of_tweet_ids(filepath: str):
    to_return = []
    file = open(filepath, "r")
    for line in file:
        to_return.append(line.strip())
    file.close()
    return to_return


def main():
    print("Starting program")
    claim_or_news = ClaimOrNews.CLAIM
    filepath_to_csv = "unifiedCSVs\\raw_claim_twitter.csv"
    filepath_to_tweet_ids = ""
    list_of_tweet_ids = get_list_of_tweet_ids(filepath_to_tweet_ids)
    tweet_file_data_list = get_tweet_file_data_list(filepath_to_csv, claim_or_news, list_of_tweet_ids)

    output_file_path = "twitterAPIData\\claim_twitter.csv"
    output_file = open(output_file_path, "w+")

    index = 0
    max_list_length = 500
    iterations = int(len(tweet_file_data_list) / max_list_length)
    remainder = len(tweet_file_data_list) - (iterations * max_list_length)
    print("Number of tweets: " + str(tweet_file_data_list))
    for i in range(0, iterations):
        print("Index: " + str(index))
        list_to_get = tweet_file_data_list[index: index+max_list_length]
        twitter_api_data_list = TwitterAPIHandler.get_list_of_tweet_api_data(list_to_get)
        for twitter_api_data in twitter_api_data_list:
            output_file.write(twitter_api_data.to_file_string())
            print(twitter_api_data.to_file_string())
        index += max_list_length
    list_to_get = tweet_file_data_list[index: index + remainder]
    twitter_api_data_list = TwitterAPIHandler.get_list_of_tweet_api_data(list_to_get)
    for twitter_api_data in twitter_api_data_list:
        output_file.write(twitter_api_data.to_file_string())
        print(twitter_api_data.to_file_string())

    output_file.close()
    print("Finished program")
