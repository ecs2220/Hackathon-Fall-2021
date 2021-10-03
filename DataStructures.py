import enum


class ClaimOrNews(enum.Enum):
    CLAIM = "claim"
    NEWS = "news"


class RealOrFake(enum.Enum):
    REAL = "real"
    FAKE = "fake"


def convert_str_to_real_or_fake(convert_str: str):
    if convert_str == "real":
        return RealOrFake.REAL
    elif convert_str == "fake":
        return RealOrFake.FAKE
    else:
        raise ValueError


class TweetFileData:
    def __init__(self, news_index: int,
                 tweet_id: int,
                 claim_or_news: ClaimOrNews,
                 real_or_fake: RealOrFake,
                 ):
        self.__news_index__ = news_index
        self.__tweet_id__ = tweet_id
        self.__claim_or_news__ = claim_or_news
        self.__real_or_fake__ = real_or_fake

    def get_news_index(self):
        return self.__news_index__

    def get_tweet_id(self):
        return self.__tweet_id__

    def claim_or_news(self):
        return self.__claim_or_news__

    def real_or_fake(self):
        return self.__real_or_fake__


class TweetAPIData:
    def __init__(self, tweet_file_data: TweetFileData,
                 epoch_time: float,
                 date_str: str,
                 content: str,
                 hash_tags: list,
                 like_count: int,
                 retweet_count: int,
                 reply_count: int,
                 user_id: str,
                 is_reply: bool):
        self.__news_index__ = tweet_file_data.get_news_index()
        self.__tweet_id__ = tweet_file_data.get_tweet_id()
        self.__claim_or_news__ = tweet_file_data.claim_or_news()
        self.__real_or_fake__ = tweet_file_data.real_or_fake()
        self.__epoch_time__ = epoch_time
        self.__date_str__ = date_str
        self.__content__ = content
        self.__hash_tags__ = hash_tags
        self.__like_count__ = like_count
        self.__retweet_count__ = retweet_count
        self.__reply_count__ = reply_count
        self.__user_id__ = user_id
        self.__is_reply__ = is_reply

    def get_news_index(self):
        return self.__news_index__

    def get_tweet_id(self):
        return self.__tweet_id__

    def claim_or_news(self):
        return self.__claim_or_news__

    def real_or_fake(self):
        return self.__real_or_fake__

    def get_epoch_time(self):
        return self.__epoch_time__

    def get_date_str(self):
        return self.__date_str__

    def get_tweet_content(self):
        return self.__content__

    def get_hash_tags(self):
        return self.__hash_tags__

    def get_like_count(self):
        return self.__like_count__

    def get_retweet_count(self):
        return self.__retweet_count__

    def get_reply_count(self):
        return self.__reply_count__

    def get_user_id(self):
        return self.__user_id__

    def is_reply(self):
        return self.__is_reply__

    def to_file_string(self):
        return str(self.__tweet_id__) + "," \
               + self.__date_str__ + "," \
                + str(self.__epoch_time__) + "," \
                + self.__content__.replace(",", " ") + "," \
                + "|".join(self.__hash_tags__) + "," \
                + str(self.__like_count__) + "," \
                + str(self.__retweet_count__) + "," \
                + str(self.__reply_count__) + "," \
                + str(self.__user_id__) + "," \
                + str(self.__is_reply__) + "," \
                + str(self.__real_or_fake__) + "," \
                + str(self.__claim_or_news__)


class NewsData:
    def __init__(self,
                 news_id: int,
                 real_or_fake: RealOrFake,
                 date_str: str,
                 fact_check_url: str,
                 title: str,
                 news_title: str,
                 content: str,
                 abstract: str,
                 meta_keywords: list):
        self.__news_id__ = news_id
        self.__real_or_fake__ = real_or_fake
        self.__fact_check_url__ = fact_check_url
        self.__date_str__ = date_str
        self.__title__ = title
        self.__news_title__ = news_title
        self.__content__ = content
        self.__abstract__ = abstract
        self.__meta_keywords__ = meta_keywords

    def get_news_id(self):
        return self.__news_id__

    def real_or_fake(self):
        return self.__real_or_fake__

    def get_fact_check_url(self):
        return self.__fact_check_url__

    def get_date_str(self):
        return self.__date_str__

    def get_title(self):
        return self.__title__

    def get_news_title(self):
        return self.__news_title__

    def get_content(self):
        return self.__content__

    def get_abstract(self):
        return self.__abstract__

    def get_meta_keywords(self):
        return self.__meta_keywords__

