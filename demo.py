import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://zeenews.india.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    # Replace these with the actual HTML tags and classes on the website
    article_elements = soup.find_all('div',class_='news_description')
    # print(article_elements)
    for article in article_elements[:100]:
        title_element = article.find('a')
        # title_element = article.find('h2')
        # content_element = article.find('div', class_='content')
        # tag = article.find('div',class_='bread_crum')
        # classification_element = tag.find('a',id_='section_title')

        # Check if all elements are found before extracting data
        if title_element :
        # and content_element and classification_element:
            title = title_element.text.strip()
            # content = content_element.text.strip()
            # classification = classification_element.text.strip()

            data.append({'Title': title})
            # , 'Content': content, 'Classification': classification})

    if data:
        df = pd.DataFrame(data)
        df.to_csv('news_data.csv', index=False)
        print("Scraping and CSV creation completed successfully!")
    else:
        print("No data was collected. Check HTML tags and classes in the script.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
