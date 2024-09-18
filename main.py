import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'NYU_ShuttleScraper - Abdur Rahman (ar7165@nyu.edu)'
}

url = 'https://www.nyu.edu/life/travel-and-transportation/university-transportation/routes-and-schedules.html'

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table')

        if table:
            rows = table.find_all('tr')

            # Loop through each row in the table
            for row in rows:
                ths = row.find_all('th')
                if ths:  
                    headers = [th.text.strip() for th in ths if th.text.strip()]  # Filter out empty headers
                    if headers:
                        print("Headers:", headers)
                else:  # Handle table data rows
                    cols = row.find_all('td')
                    data = [col.text.strip() for col in cols if col.text.strip()]  # Clean and ignore empty columns
                    if data:  
                        print(data)
        else:
            print("No table found on the page.")
        
        print("Data extraction successful.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(3)
