import os
import requests
#import urllib.request
from bs4 import BeautifulSoup

# Get driver names
drivers_url = 'https://www.formula1.com/en/drivers.html'
response = requests.get(drivers_url)

soup = BeautifulSoup(response.text, "html.parser")

driver_names_unformatted = soup.findAll('a', attrs={"class":"driver"})
driver_names = [name.text.replace('\t','').replace('\n', ' ').strip() for name in driver_names_unformatted]

with open('driver_names.txt', 'w') as my_file:
    for name in driver_names:
        my_file.write(f'{name},')

# Get team names
teams_url = 'https://www.formula1.com/en/teams.html'
response = requests.get(drivers_url)

soup = BeautifulSoup(response.text, "html.parser")

team_names_unformatted = soup.findAll('a', attrs={"class":"team"})
team_names = [name.text.replace('\t','').replace('\n', ' ').strip() for name in team_names_unformatted]

with open('team_names.txt', 'w') as my_file:
    for name in team_names:
        my_file.write(f'{name},')
