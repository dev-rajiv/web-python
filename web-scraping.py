import requests
from bs4 import BeautifulSoup
import pandas as pd

# for passing additional information with an HTTP request or response.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

# URL of the webpage to scrape
url ="https://www.squareyards.com/new-launch-projects-in-gurgaon"

# Define custom titles for each class
class_names = {
    'Names': 'projectName',
    'Locations': 'locationName',
    'Prices': 'price DSE_NewProjects_D19'
   }

# Fetch the webpage content
response = requests.get(url, headers=headers) 
# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")
# Define an empty dictionary to store data
data = {}
# Extract data from each class 
for title, class_name in class_names.items():
    # Find all elements with the specified classes
        contents = soup.find_all(class_= class_name)
        text = [content.text.strip() for content in contents]
    # Store the extracted data in the dictionary
        data[title]= text
    
# Dictionary to a DataFrame
df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
csv_filename = 'New Launched Project.csv'
df.to_csv(csv_filename, index=False)
print(f'Data saved to {csv_filename}')