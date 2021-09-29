# 'Manchester United Weekly Fixture Updates'

'Manchester United Weekly Fixture Updates' is a Python script that automatically sends an email to myself every Monday with a table detailing the Manchester United Fixtures of the upcoming week. This script was made for my personal use, having learnt some web-scraping and wanting to try it out with a real-life application, helping me keep track of the upcoming football matches for the week for the football club I support, Manchester United.

## How can we use this script?

This script requires the installation of numerous applications as well as python libraries. Firstly, a [chrome driver](https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/) with a version the same as the Chrome application installed on your computer should be downloaded. A path in your file explorer/finder to the location of the chrome driver should be initialized in the code.

The python libraries required can be downloaded by running the command-line arguments in the terminal:

`pip install [library name]`

This should be done for the python libraries: selenium, bs4, pandas, datetime, schedule and time. The libraries 'smtplib', 'sys', and 'email.mime' should already be installed in your computer by default.

Next, you require an email account that you'd want to use to send the automated emails. It would be preferred to not use an email with important personal information on it as it would have a lower level of security, since it is being used to automate tasks. For this email account to be valid to use, you need to enable the ['access for less secure apps'](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Mh5zS9ZPAma7M_CaXLxEPVFJZ07y9eaGVEg8U96ww_hpPGPmN48MfAR9Mg3OF0_BFkae8oNH1oSTfzzasMKT98GdwgBA) feature as Google flags this to be a less secure form of login. You should also initialize (an) email recipient(s) for the email to be sent to.

Afterwards, you should be good to go!

## How does this script work?
There is 4 parts to this script, whereby I will explain how each works below.

### 1. Web Scraping using Selenium and BeautifulSoup
For this first step, we have to import a few libraries as shown below.

```
from selenium import webdriver
from bs4 import BeautifulSoup
```
 
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is used to scrape content on html pages. It is done by inspecting the source code from the page and using the elements in the code to find the content to be scraped.
However, most websites are loaded using [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), which means the page needs to be dynamically loaded before the content you want to scrape shows up. Hence, selenium is used to automatically load the web page using Chrome in this case (can also be Firefox or other web browsers) with the help of a Chrome driver. To do so, a [chrome driver](https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/) of the same version as the chrome application needs to be installed on the computer.

The website we will use to scrape the data for Manchester United Fixtures will be [ESPN](https://www.espn.com/soccer/team/fixtures/_/id/360/manchester-united). Add all the items scraped to a dictionary 'fixture_item' where the items scraped are: 'Fixture', 'Day', 'Date', 'Competition'.

### 2. Extracting the data using Pandas

Thereafter, add all the items scraped, in the 'fixture_item' dictionary, into a [pandas](https://pandas.pydata.org/docs/user_guide/index.html) dataframe. Convert all the datetime values to the same standardized pandas format, so all values can be compared to one another. The values obtained would be: the datetime of all the fixtures in the dataframe and the timestamp of the present datetime that the script is running. These values would then be compared to a timedelta function of 7 days, whereby if the fixture datetime is within 7 days of the script running (on a Monday), the fixture would be extracted into another dataframe. This is done as follows:

`solution = df.loc[(df.Date - present_date) <= pd.Timedelta(days = 7)]`

(df here refers to the dataframe, thus df.Date means the dates of all fixtures in the df)

### 3. Automating an email to be sent to you using the smtplib

For this section, we have to firstly convert the extracted fixtures for the upcoming week currently in the pandas dataframe format into a html format so it can be sent in an email. The following libraries required for this section are as follows:
```
import smtplib as smtp
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```
Using the [email.mime](https://docs.python.org/3/library/email.mime.html) library, initialize the MIME type to be either mixed, or alternative, depending on whether the email would contain a mix of plain text and html, or just plain text, respectively. In this case, with the table of fixtures added in the email, the MIME type will be mixed, initialized through the 'MIMEMultipart' function. We can then add the subject, sender and recipient, to the sections of the MIMEMultipart allocated for these variables. MIMEText is used to add the plain text (body of email), as well as the html (table of fixtures). The text is then converted to a string, ready to be sent as a email.

Now, we need to initialize an 'smtp' server through which we will send our email. To do so, we would need to login to the email account of the sender. For security purposes, the password should be keyed in into the command-line argument.

### 4. Scheduling the script using schedule library

## Final Result!
![Final Result](/images/Final_Result.jpeg)
