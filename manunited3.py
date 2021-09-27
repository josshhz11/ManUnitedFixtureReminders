# Libraries for web-scraping
from selenium import webdriver
from bs4 import BeautifulSoup
# Libraries for table dataframe, datetime, scheduling program frequency and sleep, respectively
import pandas as pd
import datetime
import schedule
import time
# Libraries for sending email
import smtplib as smtp
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def program_code():
    # Web scraping Man United fixtures into pandas dataframe

    if (len(sys.argv) != 2 and len(sys.argv) != 3):
        raise Exception('Usage: python3 manunited3.py {email password} (&)')

    PATH = '/Users/josshhz11/Downloads/chromedriver'
    url = 'https://www.espn.com/soccer/team/fixtures/_/id/360/manchester-united'

    driver = webdriver.Chrome(PATH)
    driver.get(url)
    soup_file = driver.page_source
    soup = BeautifulSoup(soup_file, 'html.parser')

    matches = soup.find_all('tr', class_='Table__TR Table__TR--sm Table__even')

    fixture_list = []
    # loops over each product grabbing details we want to know of each product
    for match in matches:
        rows_of_matches = match.select('td')

        # date e.g. Sat, Sep 25 [7:30 PM]
        date = rows_of_matches[0].div.text
        # Remove comma in date text so 
        date = date.replace(',', '')
        # date_with_year 
        time = rows_of_matches[4].a.text

        day = date.split(' ', 1)[0]

        # just_date e.g. Sep 25 [7:30 PM]
        just_date = date.split(' ', 1)[1]
        
        
        # Obtain the month date as text i.e. 'Sep'
        month_name = just_date.split(' ', 1)[0]
        # Convert the month date text to month date in int; add numerical month to date_dict, add day to date_dict
        month_number = datetime.datetime.strptime(month_name, '%b')
        # Not the most foolproof code since scraped dates do not have year, and this is only because remaining fixtures for this 2021/2022 season
        # last from September 2021 to October 2022
        if month_number.month >= 9:
            just_date = just_date + ' 2021'
        else:
            just_date = just_date + ' 2022'


        home_team = rows_of_matches[1].div.a.text
        away_team = rows_of_matches[3].div.a.text
        competition = rows_of_matches[5].span.text
            

        fixture_item = {
            'Fixture': home_team + ' vs ' + away_team,
            'Day': day,
            'Date': just_date + ' ' + time,
            'Competition': competition
        }
        
        fixture_list.append(fixture_item)

    df = pd.DataFrame(fixture_list)
    df['Date'] = pd.to_datetime(df.Date)
    #print(df)
    # present date timestamp
    present_date = pd.Timestamp('today')
    
    # Obtaining a table for all matches for the upcoming week if scheduled every Monday
    solution = df.loc[(df.Date - present_date) <= pd.Timedelta(days = 7)]
    
    # Converting table to html format to pass into email
    html_table = solution.to_html()
    sender = "automationsn1per0@gmail.com"
    recipient = "liquidstew2k@gmail.com"
    subject = 'Manchester United Fixtures'

    # Create message container - the correct MIME type is mixed/alternative.
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    description = 'The table below shows the Manchester United fixtures for this upcoming week.\r\r\n'

    # Attach body text (both description and upcoming fixtures table) to msg
    msg.attach(MIMEText(description, 'plain'))
    msg.attach(MIMEText(html_table, 'html'))

    # Convert entire body text as string to be put into email (has some html in it)
    body = msg.as_string()

    # Initialize SMTP email server
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    # For safety of email password, input password into command line after 'python3 manunited3.py'
    server.login('automationsn1per0@gmail.com', sys.argv[1])

    server.sendmail(sender, recipient, body)

    server.quit()

schedule.every().monday.at('21:00').do(program_code)

while 1:
    schedule.run_pending()
    time.sleep(1)