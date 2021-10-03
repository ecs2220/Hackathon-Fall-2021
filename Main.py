import pandas
import DataStructures
from DataStructures import ClaimOrNews
from DataStructures import TweetFileData
import time
import TwitterAPIHandler


def get_tweet_file_data_list(filepath: str, claim_or_news: ClaimOrNews, list_of_tweet_ids):
    to_return = []
    seen_tweet_ids = []
    #df = pandas.read_csv(filepath)
    chunk = pandas.read_csv(filepath, chunksize=1000000)
    df = pandas.concat(chunk)
    counter = 0
    for index, row in df.iterrows():
        tweet_id = str(row["tweet_id"])
        print(counter)
        counter += 1
        if not list_of_tweet_ids.__contains__(tweet_id):
            continue
        if seen_tweet_ids.__contains__(tweet_id):
            continue
        if claim_or_news == ClaimOrNews.CLAIM:
            news_index = str(row["claim_id"])
        else:
            news_index = str(row["news_id"])
        real_or_fake = DataStructures.convert_str_to_real_or_fake(str(row["real_or_fake"]))
        tweet_file_data = TweetFileData(news_index, tweet_id, claim_or_news, real_or_fake)
        seen_tweet_ids.append(tweet_id)
        to_return.append(tweet_file_data)
    return to_return


def get_list_of_tweet_ids(filepath: str):
    to_return = []
  #  df = pandas.read_csv(filepath)
    chunk = pandas.read_csv(filepath, chunksize=1000000)
    df = pandas.concat(chunk)
    for index, row in df.iterrows():
        to_return.append(str(row["tweet_id"]))
    return to_return


def main():
    print("Starting program")
    claim_or_news = ClaimOrNews.NEWS
    filepath_to_csv = "data\\unifiedCSVs\\raw_news_twitter.csv"
    filepath_to_tweet_ids = "data\\toPull\\news_twitter_ids.csv"
    list_of_tweet_ids = get_list_of_tweet_ids(filepath_to_tweet_ids)
    tweet_file_data_list = get_tweet_file_data_list(filepath_to_csv, claim_or_news, list_of_tweet_ids)

    output_file_path = "twitterAPIData\\news_twitter.csv"
    output_file = open(output_file_path, "w+", encoding="utf-8")

    index = 0
    max_list_length = 100
    iterations = int(len(tweet_file_data_list) / max_list_length)
    remainder = len(tweet_file_data_list) - (iterations * max_list_length)
    print("Number of tweets: " + str(len(tweet_file_data_list)))
    counter = 0
    for i in range(0, iterations):
        print("Index: " + str(index))
        list_to_get = tweet_file_data_list[index: index+max_list_length]
        twitter_api_data_list = TwitterAPIHandler.get_list_of_tweet_api_data(list_to_get)
        for twitter_api_data in twitter_api_data_list:
            output_file.write(twitter_api_data.to_file_string())
            print(twitter_api_data.to_file_string())
        index += max_list_length
        counter += 1
        if counter == 850:
            print("Sleeping for 15 minutes")
            time.sleep(15 * 60)
            counter = 0
    list_to_get = tweet_file_data_list[index: index + remainder]
    twitter_api_data_list = TwitterAPIHandler.get_list_of_tweet_api_data(list_to_get)
    for twitter_api_data in twitter_api_data_list:
        output_file.write(twitter_api_data.to_file_string())
        print(twitter_api_data.to_file_string())

    output_file.close()
    print("Finished program")


main()
