import requests
from lxml import html

# The URL of the page you want to scrape
url = 'YOUR_TARGET_URL_HERE'

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page with lxml
    tree = html.fromstring(response.content)
    
    # The provided XPath
    xpath = '//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[1]/h2'
    
    # Use the XPath to extract the content
    content = tree.xpath(xpath)
    
    # Print the extracted content
    print('Extracted content:', content)
else:
    print('Failed to retrieve the page. Status code:', response.status_code)
