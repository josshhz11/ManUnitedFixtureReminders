# 'Manchester United Weekly Fixture Updates'

'Manchester United Weekly Fixture Updates' is a Python script that automatically sends an email to myself every Monday with a table detailing the Manchester United Fixtures of the upcoming week. This script was made for my personal use, having learnt some web-scraping and wanting to try it out with a real-life application, helping me keep track of the upcoming football matches for the week for the football club I support, Manchester United.

## How does this script work?
There is 3? parts to this script, whereby I will explain how each works below.

### 1. Web Scraping using Selenium and BeautifulSoup
For this first step, we have to import a few libraries as shown below.

`from selenium import webdriver`

 `from bs4 import BeautifulSoup`
 
BeautifulSoup is used to scrape content on html pages. It is done by inspecting the source code from the page and using the elements in the code to find the content to be scraped.
However, most websites are loaded using Javascript, which means the page needs to be dynamically loaded before the content you want to scrape shows up. Hence, selenium is used to automatically load the web page using Chrome in this case (can also be Firefox or other web browsers) with the help of a Chrome driver. To do so, a [chrome driver](https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/) of the same version as the chrome application needs to be installed on the computer.

The website we will use to scrape the data for Manchester United Fixtures will be [ESPN](https://www.espn.com/soccer/team/fixtures/_/id/360/manchester-united). Add all the items scraped to a dictionary 'fixture_item' where the items scraped are: 'Fixture', 'Day', 'Date', 'Competition'.

### 2. Extracting the data using Pandas

Thereafter, add all the items scraped, in the 'fixture_item' dictionary, into a pandas dataframe. Convert all the datetime values to the same standardized pandas format, so all values can be compared to one another. The values obtained would be: the datetime of all the fixtures in the dataframe and the timestamp of the present datetime that the script is running. These values would then be compared to a timedelta function of 7 days, whereby if the fixture datetime is within 7 days of the script running (on a Monday), the fixture would be extracted into another dataframe. This is done as follows:

`solution = df.loc[(df.Date - present_date) <= pd.Timedelta(days = 7)]`

(df here refers to the dataframe, thus df.Date means the dates of all fixtures in the df)

### 3. Automating an email to be sent to you using the smtplib

### 4. Scheduling the script using schedule library

## Final Result!
![Final Result](/images/Final_Result.jpeg)
