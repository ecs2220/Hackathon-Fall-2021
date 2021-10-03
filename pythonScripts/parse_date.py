import pandas as pd
import re
from datetime import datetime

dates = []
#take in output of dates.py, which has nicely cleaned up the raw_dates
df = pd.read_csv('out.csv')
#print(df.dtypes)

months = ['april', 'may', 'june']  # for some reason these are the only months written in letter form in urls
# print(df["news_url"][0])

for ind in df.index:
    #print(ind)
    if (str(df["date"][ind]) != "nan"):
        # keep the date column outputted by dates.py file
        dates.append(df["date"][ind])
    elif (str(df["raw_date"][ind]) != "nan"):
        # if there's already a raw publish date, we'll take that
        dates.append(df["raw_date"][ind])
        # none of the rest of this if is useful; it's just for comparison's sake to make sure publish date aligns w/ url
        url = df["news_url"][ind]
        match = re.search(r"(2020)[-/]?([\d][\d]?)[-/]?([\d][\d]?)[^\d]", url)
        if match:
            print('both', re.search(r"(2020)[-/]?([\d][\d]?)[-/]?([\d][\d]?)[^\d]", url).group(0), df["raw_date"][ind])
        else:
            print('not in url', df["raw_date"][ind])
        # print(df["publish_date"][ind])
    else:
        url = df["news_url"][ind]
        if (df["fact_check_url"][ind] == "sciencedaily.com"):
            # their dates are very weird: 200821 = 8/21/2020
            date_match = re.search((r"/(20)([\d][\d])([\d][\d])"), url)
            if date_match:
                #print('url only', date_match.group(0), url)


                    year = 2020
                    month = int(date_match.group(2))
                    day = int(date_match.group(3))

                    the_date = datetime(year, month, day)
                    dates.append(the_date.strftime("%m-%d-%Y"))
            else:
                #they have some articles from 2019
                date_match = re.search((r"/(19)([\d][\d])([\d][\d])"), url)
                if date_match:
                    year = 2019
                    month = int(date_match.group(2))
                    day = int(date_match.group(3))

                    the_date = datetime(year, month, day)
                    dates.append(the_date.strftime("%m-%d-%Y"))
                else:
                    dates.append('')
        elif (df["fact_check_url"][ind] == "who.int"):
            # they use dd-mm-yyyy; and they're the only ones
            date_match = re.search(r"([\d][\d]?)-([\d][\d]?)-(2020)", url)
            if date_match:
                year = 2020
                month = int(date_match.group(2))
                day = int(date_match.group(1))
                the_date = datetime(year, month, day)
                dates.append(the_date.strftime("%m-%d-%Y"))
                #print('url only', the_date.strftime("%m-%d-%Y"), url)
            else:
                # sometimes they're normal
                date_match = re.search(r"(2020)/([\d][\d]?)/([\d][\d]?)[^\d]", url)
                if date_match:
                    year = int(date_match.group(1))
                    month = int(date_match.group(2))
                    day = int(date_match.group(3))
                    the_date = datetime(year, month, day)
                    dates.append(the_date.strftime("%m-%d-%Y"))
                    #print('url only', the_date.strftime("%m-%d-%Y"), url)
                else:
                    dates.append('')
        elif (str(url) != "nan"):


            date_match = re.search(r"(2020)[-/a-z]?[-/a-z]?([\d][\d])[-/]?([\d][\d])[^\d]", url)
            if date_match:
                # print()
                # print('url only', date_match.group(0), url)
                year = int(date_match.group(1))
                # if date_parts[1] <= 12
                month = int(date_match.group(2))
                day = int(date_match.group(3))
                the_date = datetime(year, month, day)
                dates.append(the_date.strftime("%m-%d-%Y"))
                #print('url only', the_date.strftime("%m-%d-%Y"), url)
            else:
                # some cdc dates are in this awful format: 091320 = 9/13/20
                if (df["fact_check_url"][ind] == "cdc.gov"):
                    date_match = re.search(r"([\d][\d])([\d][\d])20", url)
                    if date_match:
                        year = 2020
                        month = int(date_match.group(1))
                        day = int(date_match.group(2))
                        the_date = datetime(year, month, day)
                        dates.append(the_date.strftime("%m-%d-%Y"))
                        #print('url only', the_date.strftime("%m-%d-%Y"), url)
                    else:
                        dates.append('')
                else:
                    # for the few articles that have a month name in the url
                    if ("april" in url):
                        date_match = re.search(r"(april)-([\d][\d])[^\d]*", url)
                    elif ("may" in url):
                        date_match = re.search(r"(may)-([\d][\d])[^\d]*", url)
                    elif ("june" in url):
                        date_match = re.search(r"(june)-([\d][\d])[^\d]*", url)
                    else:
                        date_match = []

                    if date_match:
                        year = 2020
                        month = datetime.strptime(date_match.group(1), "%B").month
                        day = int(date_match.group(2))
                        the_date = datetime(year, month, day)
                        dates.append(the_date.strftime("%m-%d-%Y"))
                        print('url only', the_date.strftime("%m-%d-%Y"), url)
                    else:

                        dates.append('')
        else:
            dates.append('')

df["date"] = dates
# print(df["date"])
print("Dates stored")
df.to_csv('news_with_dates.csv')
print("csv created")

'''for date in df["date mm-dd-yyyy"]:
    if date:
        print(date)'''

# print(df["news_url"])
