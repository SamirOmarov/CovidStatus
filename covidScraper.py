from country import Country
from bs4 import BeautifulSoup
import requests

website_url = requests.get('https://thevirustracker.com').text

soup = BeautifulSoup(website_url, "lxml")
# print(soup.prettify())


table = soup.find('table', {'class': 'table-striped'})
links = table.findAll('a')  # To extract Country/Titles


regions = []
titles = []


for link in links:
    temp = link.text
    regions.append(temp)

# delete empty link texts
for val in regions:
    if val != '':
        titles.append(val)

# titles = []
total = []
newCases = []
deaths = []
newDeaths = []
recovered = []
active = []
serious = []

for row in table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 8:
        total.append(cells[1].find(text=True))
        newCases.append(cells[2].find(text=True))
        deaths.append(cells[3].find(text=True))
        newDeaths.append(cells[4].find(text=True))
        recovered.append(cells[5].find(text=True))
        active.append(cells[6].find(text=True))
        serious.append(cells[7].find(text=True))

# print(titles)
# print(total)

keys = ['country_name', 'total_case', 'new_cases', 'total_deaths',
        'new_deaths', 'total_recovered', 'active', 'serious']

database = []

for id in range(len(titles)):
    country = Country(titles[id], total[id], newCases[id],
            deaths[id], newDeaths[id], recovered[id])
    database.append(country)

# print(database[1])

