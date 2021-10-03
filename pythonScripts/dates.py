import pandas as pd
import re
from datetime import datetime


# Class variables
df = pd.read_csv("../data/unifiedCSVs/raw_news_articles.csv")
real_row_count = 0
fake_row_count = 0
real_with_dates_count = 0
fake_with_dates_count = 0


# Get numerical month from string abbreviation
def getMonthNumFromStr(month_str):
	if ( month_str == ("JAN" or "Jan" or "January") ):
		return "01"
	elif ( month_str == ("FEB" or "Feb" or "February") ):
	    return "02"
	elif ( month_str == ("MAR" or "Mar" or "March") ):
	    return "03"
	elif ( month_str == ("APR" or "Apr" or "April") ):
	    return "04"
	elif ( month_str == ("MAY" or "May" or "May") ):
	    return "05"
	elif ( month_str == ("JUN" or "Jun" or "June") ):
	    return "06"
	elif ( month_str == ("JUL" or "Jul" or "July") ):
	    return "07"
	elif ( month_str == ("AUG" or "Aug" or "August") ):
	    return "08"
	elif ( month_str == ("SEP" or "Sep" or "September") ):
	    return "09"
	elif ( month_str == ("OCT" or "Oct" or "October") ):
	    return "10"
	elif ( month_str == ("NOV" or "Nov" or "November") ):
	    return "11"
	else:
	    return "12"


# Check for a missing value (i.e. an empty entry in the CVS file)
def isNaN(string):
	return string != string


# Make a date according to a standardized format (i.e. MM-DD-YYYY)
def makeStandardDateFormat(month, day, year):
	if (int(month) < 10 and len(month) == 1):
		month = "0" + month
	if (int(day) < 10 and len(day) == 1):
		day = "0" + day
	return month + "-" + day +  "-" + year


# Iterate through each row in the date column
for index, row in df.iterrows():
	raw_date = row["raw_date"]
	if (row["real_or_fake"] == "real"):
		real_row_count += 1
	else:
		fake_row_count += 1

	# For rows with a non-empty entry in the "raw published date" column, convert
	# the raw date to a standard format and store it in the "date" column
	if not isNaN(raw_date):

		# Check if in datetime format already for easy format conversion (i.e. 2020-04-07T14:59:35)
		if ( re.search("2020[-/][\d]+[-/][\d]+T", raw_date) ):

			# Cleaning Data: Ignore forgotten colons or mistakenly added chars
			raw_date = raw_date[0:19]
			isodate = datetime.fromisoformat(raw_date)
			date = isodate.strftime("%m-%d-%Y")
			if (len(date) > 11):
				print(raw_date)
				print(date)
			df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


		# Else check for intended datetime formats which are missing dashes (i.e. 20200331T17:35:54)
		elif ( re.search("2020[\d]+T[\d]+:", raw_date) ):

			# Cleaning Data: Add dashes where lacking
			cleaned_date = raw_date[0:4] + "-" + raw_date[4:6] + "-" + raw_date[6:17]
			isodate = datetime.fromisoformat(cleaned_date)
			date = isodate.strftime("%m-%d-%Y")
			df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


		# Else check for DD-"Mon"-YY format (i.e. 11-Apr-20)
		elif ( re.search("([\d]+)[-/]([a-zA-Z]+)[-/]([\d]+)", raw_date) ):
			
			parsed_date = re.search("([\d]+)[-/]([a-zA-Z]+)[-/]([\d]+)", raw_date)

			day = parsed_date.group(1)
			year = "2020"
			month = getMonthNumFromStr( parsed_date.group(2) )

			date = makeStandardDateFormat(month, day, year)
			if ( len(date) < 11 ):
				df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


		# Else check for M/D/YY format (i.e. 2/7/20)
		elif ( re.search("([\d]+)[-/]([\d]+)[-/]([\d]+)", raw_date) ):
			
			parsed_date = re.search("([\d]+)[-/]([\d]+)[-/]([\d]+)", raw_date)

			month = parsed_date.group(1)
			day = parsed_date.group(2)
			year = "2020"

			date = makeStandardDateFormat(month, day, year)
			if ( len(date) < 11 ):
				df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


		# Else check for "Mon" DD, YYYY format (i.e. Mar 16, 2020)
		elif ( re.search("([a-zA-Z]+) ([\d]+),", raw_date) ):
			
			parsed_date = re.search("([a-zA-Z]+) ([\d]+),", raw_date)

			day = parsed_date.group(2)
			month = getMonthNumFromStr( parsed_date.group(1) )
			year = "2020"

			date = makeStandardDateFormat(month, day, year)
			df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


		# Else check for DD-"Mon" format (i.e. 15-May)
		elif ( re.search("([\d]+)[-/]([a-zA-Z]+)", raw_date) ):
			
			parsed_date = re.search("([\d]+)[-/]([a-zA-Z]+)", raw_date)

			month = getMonthNumFromStr( parsed_date.group(2) )
			day = parsed_date.group(1)
			year = "2020"

			date = makeStandardDateFormat(month, day, year)
			df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


		# Else check for "Mon" DD YYYY format (i.e. Aug 02 2020)
		elif ( re.search("([a-zA-Z]+) ([\d]+) 2020", raw_date) ):
			
			parsed_date = re.search("([a-zA-Z]+) ([\d]+) 2020", raw_date)

			month = getMonthNumFromStr( parsed_date.group(1) )
			day = parsed_date.group(2)
			year = "2020"

			date = makeStandardDateFormat(month, day, year)
			df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


		# Else check for DD "Mon" YYYY format (i.e. 06 March 2020)
		elif ( re.search("([\d]+) ([a-zA-Z]+) 2020", raw_date) ):
			
			parsed_date = re.search("([\d]+) ([a-zA-Z]+) 2020", raw_date)

			month = getMonthNumFromStr( parsed_date.group(2) )
			day = parsed_date.group(1)
			year = "2020"

			date = makeStandardDateFormat(month, day, year)
			df["date"][index] = date
			if (row["real_or_fake"] == "real"):
				real_with_dates_count += 1
			else:
				fake_with_dates_count += 1


# Print the metrics from the date cleaning of the CVS file
print ("\n\nDATED OBTAINED INFO ......")
print ("Total row count: " + str(fake_row_count + real_row_count))
print ("Fake rows with dabtes obtained: " + str(fake_with_dates_count))
print ("Real rows with dabtes obtained: " + str(real_with_dates_count))
print ("\n")


# Generate an out.csv file with all dates inputted in the proper format. Then the out.csv 
# file will be looked at by parse_date.py, which will try to generate a date for all rows
# which do not have one by inspecting the URL
df.to_csv('out.csv')
