import enum


class ClaimOrNews(enum.Enum):
    CLAIM = 0
    NEWS = 1


class RealOrFake(enum.Enum):
    REAL = True
    FAKE = False


def convert_str_to_real_or_fake(convert_str: str):
    if convert_str == "real":
        return RealOrFake.REAL
    elif convert_str == "fake":
        return RealOrFake.FAKE
    else:
        raise ValueError


class TweetData:
    def __init__(self, news_index: int,
                 tweet_id: int,
                 claim_or_news: ClaimOrNews,
                 real_or_fake: RealOrFake,
                 ):
        self.__news_index__ = news_index
        self.__tweetId__ = tweet_id
        self.__claim_or_news__ = claim_or_news
        self.__real_or_fake__ = real_or_fake
        self.__date_str__ = None

    def get_news_index(self):
        return self.__news_index__

    def get_tweet_id(self):
        return self.__tweetId__

    def claim_or_news(self):
        return self.__claim_or_news__

    def real_or_fake(self):
        return self.__real_or_fake__

    def get_date_str(self):
        return self.__date_str__

    def set_date_str(self, date_str: str):
        self.__date_str__ = date_str


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

