import csv
import requests
from bs4 import BeautifulSoup

def scrape():
    # Make an HTTP GET request to the website
    url = 'http://www.acclaimedmusic.net/year/alltime_albums.htm'
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the album information
    table = soup.find('table')

    # Create a CSV file to store the data
    with open('albums.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Rank', 'Artist', 'Album', 'Genre','Year'])

        # Iterate over the rows in the table
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 5:
                # Write the data for each row to the CSV file
                writer.writerow([cells[0].text, cells[1].text, cells[2].text, cells[3].text, cells[4].text])