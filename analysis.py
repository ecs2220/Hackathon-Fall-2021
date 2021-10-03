# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Analysis of Data
# 
# Plotting time!!!
# 
# Twitter Data Format:
# - tweet_id: int
# - date: str (MM-DD-YYYY)
# - epochtime: long (in milliseconds)
# - content: str 
# - hashtags: list(string)
# - like_count: int
# - retweet_count: int
# - reply_count: int
# - user: str
# - is_reply: boolean
# - real_or_fake: boolean
# - news_or_claim: boolean
# - \+
# - real_or_fake
# - date
# - claim_id
# - tweet_id
# - **or**
# - news_id
# - date
# - real_or_fake
# - tweet_id
# %% [markdown]
# ## Claim Analysis:
# Can refuting fake news make a difference over time?

# %%
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# %%
df_claim_twitter_api = pd.read_csv("twitterAPIData/claim_twitter.csv")
df_claim_twitter_local = pd.read_csv("data/unifiedCSVs/raw_claim_twitter.csv")

df_claim = df_claim_twitter_local.drop(columns=["date", "real_or_fake"]).merge(df_claim_twitter_api, left_on='tweet_id', right_on='tweet_id')

df_claim


# %%
# Count of real and fake tweets per day sumed over all claims
# Also relative plots



sns.set_theme(style="whitegrid")
ax = sns.barplot(x="Day", y="Frequency", data=tips)
plt.title('Frequency of Real and Fake Tweets for all Claims per Day')


# %%
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="Day", y="Frequency", data=tips)
plt.title('Relative Frequency of Real and Fake Tweets for all Claims per Day')


# %%
# Count of real and fake tweets per claim
# Also relative plots

sns.set_theme(style="whitegrid")
ax = sns.barplot(x="Day", y="Frequency", data=tips)
plt.title('Relative Frequency of Real and Fake Tweets for all Claims per Day')


# %%
# Real and fake tweets average likes over time
# Real and fake tweets average retweets over time

# %% [markdown]
# ## News Analysis:
# Comparing the spread of real and fake news.

# %%
# For the top x real and fake news, compare the relative frequency of posts over time
# For the top x real and fake news, compare the number of likes over time
# For the top x real and fake news, compare the number of retweets over time


