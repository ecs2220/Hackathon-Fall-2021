# Columbia Data Science Hackathon Entry

## Claim Analysis:
Can refuting fake news make a difference over time?

## News Analysis:
Comparing the spread of real and fake news.

## Main.py
Used to initiate run.
Gets tweet_ids to be pulled from Twitter API from csv files.
Pulls tweets.
Logs tweet API data in new csv.

## TwitterAPIHandler.py
Handles Twitter API interaction: sends GET request with
list of 100 tweet_ids for tweets we want to pull.
Data including publication timestamp, like_count,
reply_count, and retweet_count.

## dates.py and parsed_date.py
Dates.py used to format and extract mm-dd-yyyy from urls in dataset

